# Generated by Django 3.0.4 on 2021-02-21 04:35

from django.conf import settings
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(default='default_profile_pic.png', upload_to='profile_pics')),
                ('password_changed', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='SqlProblem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='full name')),
                ('score', models.IntegerField(default=1)),
                ('type', models.CharField(choices=[('BLIND', 'Blind'), ('IN_BAND', 'In_Band'), ('OUT_BAND', 'Out_Band')], default='BLIND', max_length=10)),
                ('difficult', models.CharField(choices=[('EASY', 'Easy'), ('MEDIUM', 'Medium'), ('HARD', 'Hard')], default='EASY', max_length=7)),
            ],
        ),
        migrations.CreateModel(
            name='UsersProblems',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('problem', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.SqlProblem')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.Profile')),
            ],
            options={
                'unique_together': {('user', 'problem')},
            },
        ),
        migrations.AddField(
            model_name='sqlproblem',
            name='users',
            field=models.ManyToManyField(through='users.UsersProblems', to='users.Profile'),
        ),
        migrations.AddField(
            model_name='profile',
            name='sqlproblems',
            field=models.ManyToManyField(through='users.UsersProblems', to='users.SqlProblem'),
        ),
        migrations.AddField(
            model_name='profile',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]