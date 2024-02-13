# Generated by Django 4.0.6 on 2022-07-24 06:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('Allops', '0004_user_fields'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='fields',
        ),
        migrations.RemoveField(
            model_name='user',
            name='mails',
        ),
        migrations.CreateModel(
            name='mails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mail_id', models.EmailField(max_length=254)),
                ('fields', multiselectfield.db.fields.MultiSelectField(choices=[('Internship', 'Internship'), ('Scholarship', 'Scholarship'), ('Apprenticeships', 'Apprenticeships'), ('Training', 'Training'), ('Product Management', 'Product Management'), ('Language', 'Language'), ('Social Good', 'Social Good'), ('Machine Learning/AI', 'Machine Learning/AI'), ('Blockchain', 'Blockchain'), ('Design', 'Design'), ('Web', 'Web'), ('Health', 'Health'), ('AR/VR', 'AR/VR'), ('Gaming', 'Gaming'), ('Fintech', 'Fintech'), ('IoT', 'IoT'), ('DevOps', 'DevOps'), ('Cloud', 'Cloud'), ('Lifehacks', 'Lifehacks'), ('Cybersecurity', 'Cybersecurity'), ('Voice skills', 'Voice skills'), ('Mobile', 'Mobile'), ('Music/Art', 'Music/Art')], max_length=228)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='mail_user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
