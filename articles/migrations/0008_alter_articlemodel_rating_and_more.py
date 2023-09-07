# Generated by Django 4.2.4 on 2023-09-07 18:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0007_alter_articlemodel_rating_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articlemodel',
            name='rating',
            field=models.CharField(choices=[('2', '2'), ('1', '1'), ('0', '0'), ('3', '3'), ('4', '4')], max_length=10),
        ),
        migrations.AlterField(
            model_name='categorymodel',
            name='category_name',
            field=models.CharField(choices=[('Sports', 'Sports'), ('Technology', 'Technology'), ('Entertainment', 'Entertainment'), ('Latest', 'Latest'), ('Health', 'Health'), ('Business', 'Business'), ('Science', 'Science')], max_length=20),
        ),
    ]
