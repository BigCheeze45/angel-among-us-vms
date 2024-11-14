from django.dispatch import receiver
from django.db.utils import IntegrityError
from django.contrib.auth.models import Group
from django.db.models.signals import post_migrate
from django.contrib.auth.management import create_permissions

from django.apps import apps

DEFAULT_GROUPS = ["Administrator", "Editor", "Viewer"]


def create_default_groups():
    for item in DEFAULT_GROUPS:
        try:
            Group.objects.get_or_create(name=item)
        except IntegrityError:
            continue


def assign_permissions_to_groups():
    from django.contrib.auth.models import Group, Permission
    create_default_groups()

    # region Administrator Group
    admin_g = Group.objects.filter(name__iexact="Administrator").first()
    # give all permissions to the group
    for permission in Permission.objects.all():
        admin_g.permissions.add(permission.id)
    admin_g.save()
    # endregion

    # region Editor Group
    editor_g = Group.objects.filter(name__iexact="Editor").first()
    # editor can see everything except users
    for permission in Permission.objects.exclude(codename__icontains="user").all():
        editor_g.permissions.add(permission.id)
    editor_g.save()
    # endregion

    # region Viewer Group
    viewer_g = Group.objects.filter(name="Viewer").first()
    # viewer has read only access to Teams & Volunteers
    read_only_no_user = (
        Permission.objects
        # exclude all user related permissions
        .exclude(codename__icontains="user")
        # select view only permissions
        .filter(codename__icontains="view").all()
    )
    for perm in read_only_no_user:
        viewer_g.permissions.add(perm.id)
    viewer_g.save()
    print("Finished assigning permissions")
    # endregion


@receiver(post_migrate)
def create_groups_and_assign_permissions(sender, **kwargs):
    # Ensure that permissions are available by checking if the ContentType is loaded
    if sender.name == "django.contrib.auth":
        app_config = apps.get_app_config("auth")
        create_permissions(app_config, verbosity=0)  
        assign_permissions_to_groups()
