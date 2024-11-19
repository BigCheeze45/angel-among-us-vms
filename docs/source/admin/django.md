# Django Admin Site
The Django admin application uses the models to automatically build a site
that you can use to create, view, update, and delete records.

The Django project recommends it only for internal data management
(i.e. just for use by admins), as the model-centric approach is
not necessarily the best possible interface for all users,
and exposes a lot of unnecessary detail about the models.

More information is available in the [Django docs](https://docs.djangoproject.com/en/5.1/ref/contrib/admin/)

## Accessing the Site
The admin site is accessible [localhost:8000/admin](http://localhost:8000/admin).

By default, logging in to the admin requires that the user has the `is_staff` attribute set to True.
You can create one using the `make super` [target](make.md).

## Role Management
Behind the scenes, roles are implemented using [Django's Group](https://docs.djangoproject.com/en/5.1/topics/auth/default/#groups)
models. This means admins can easily and quickly:

* manage users
* create new roles
* change existing role permissions
