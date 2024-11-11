# Generated by Django 5.1.1 on 2024-11-11 19:23

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Volunteer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('middle_name', models.CharField(blank=True, max_length=50, null=True)),
                ('last_name', models.CharField(max_length=50)),
                ('preferred_name', models.CharField(blank=True, max_length=100, null=True)),
                ('full_name', models.CharField(blank=True, max_length=155)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('date_joined', models.DateTimeField(blank=True, null=True)),
                ('active', models.BooleanField(default=True)),
                ('cell_phone', models.CharField(max_length=128)),
                ('home_phone', models.CharField(blank=True, max_length=128, null=True)),
                ('work_phone', models.CharField(blank=True, max_length=128, null=True)),
                ('date_of_birth', models.DateField(blank=True, null=True)),
                ('job_title', models.CharField(default='AAU Volunteer', null=True)),
                ('ishelters_id', models.IntegerField(editable=False, unique=True)),
                ('ishelters_profile', models.URLField(blank=True, null=True)),
                ('maddie_certifications_received_date', models.DateField(blank=True, null=True)),
                ('ishelters_created_dt', models.DateTimeField(editable=False, null=True)),
                ('application_received_date', models.DateTimeField(auto_now=True)),
                ('address_line_1', models.CharField(max_length=100)),
                ('address_line_2', models.CharField(blank=True, max_length=100, null=True)),
                ('city', models.CharField(max_length=100)),
                ('county', models.CharField(max_length=100, null=True)),
                ('state', models.CharField(max_length=100)),
                ('zipcode', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, unique=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('email', models.EmailField(max_length=254, null=True)),
                ('ishelters_id', models.IntegerField(editable=False, unique=True)),
                ('ishelters_created_dt', models.DateTimeField(editable=False, null=True)),
                ('application_received_date', models.DateTimeField(auto_now=True)),
            ],
            options={
                'constraints': [models.UniqueConstraint(fields=('email',), name='email_null_not_unique', nulls_distinct=True)],
            },
        ),
        migrations.CreateModel(
            name='VolunteerActivity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.DateField()),
                ('description', models.TextField(blank=True, null=True)),
                ('activity_name', models.CharField(max_length=200)),
                ('volunteer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='activities', to='app.volunteer')),
            ],
        ),
        migrations.CreateModel(
            name='VolunteerChildren',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(blank=True, help_text='Detailed description of the Volunteer Pet', null=True)),
                ('updated_at', models.DateField(auto_now=True)),
                ('created_at', models.DateField(auto_now_add=True)),
                ('volunteer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='children', to='app.volunteer')),
            ],
        ),
        migrations.CreateModel(
            name='VolunteerPet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(blank=True, help_text='Detailed description of the Volunteer Pet', null=True)),
                ('updated_at', models.DateField(auto_now=True)),
                ('created_at', models.DateField(auto_now_add=True)),
                ('volunteer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pet', to='app.volunteer')),
            ],
        ),
        migrations.CreateModel(
            name='VolunteerSkill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=10)),
                ('skill', models.CharField(max_length=100)),
                ('volunteer', models.ForeignKey(db_column='volunteer_id', on_delete=django.db.models.deletion.CASCADE, related_name='skills', to='app.volunteer')),
            ],
        ),
        migrations.CreateModel(
            name='VolunteerTeam',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('end_date', models.DateTimeField(blank=True, null=True)),
                ('start_date', models.DateTimeField(blank=True, null=True)),
                ('application_received_date', models.DateTimeField(auto_now=True)),
                ('ishelters_id', models.IntegerField(editable=False, unique=True)),
                ('team', models.ForeignKey(db_column='team_id', editable=False, on_delete=django.db.models.deletion.CASCADE, to='app.team')),
                ('volunteer', models.ForeignKey(db_column='volunteer_id', editable=False, on_delete=django.db.models.deletion.CASCADE, to='app.volunteer')),
            ],
        ),
    ]
