# Generated by Django 4.0.6 on 2022-07-23 16:26

from django.db import migrations
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('Allops', '0003_opportunity_details_opportunity_location_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='fields',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('Internship', 'Internship'), ('Scholarship', 'Scholarship'), ('Apprenticeships', 'Apprenticeships'), ('Training', 'Training'), ('Product Management', 'Product Management'), ('Language', 'Language'), ('Social Good', 'Social Good'), ('Machine Learning/AI', 'Machine Learning/AI'), ('Blockchain', 'Blockchain'), ('Design', 'Design'), ('Web', 'Web'), ('Health', 'Health'), ('AR/VR', 'AR/VR'), ('Gaming', 'Gaming'), ('Fintech', 'Fintech'), ('IoT', 'IoT'), ('DevOps', 'DevOps'), ('Cloud', 'Cloud'), ('Lifehacks', 'Lifehacks'), ('Cybersecurity', 'Cybersecurity'), ('Voice skills', 'Voice skills'), ('Mobile', 'Mobile'), ('Music/Art', 'Music/Art')], default='none', max_length=20),
        ),
    ]
