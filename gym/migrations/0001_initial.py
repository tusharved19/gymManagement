# Generated by Django 2.2.10 on 2020-05-24 06:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Enquiry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=20)),
                ('Contact', models.CharField(max_length=10)),
                ('EmailId', models.CharField(max_length=30)),
                ('Age', models.CharField(max_length=20)),
                ('Gender', models.CharField(max_length=6)),
            ],
        ),
        migrations.CreateModel(
            name='Equipment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=50)),
                ('Price', models.CharField(max_length=10)),
                ('Unit', models.CharField(max_length=30)),
                ('Date', models.CharField(max_length=20)),
                ('Descripton', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=20)),
                ('Contact', models.CharField(max_length=10)),
                ('EmailId', models.CharField(max_length=30)),
                ('Age', models.CharField(max_length=2)),
                ('Gender', models.CharField(max_length=6)),
                ('Plan', models.CharField(max_length=30)),
                ('Joindate', models.CharField(max_length=10)),
                ('Expiredate', models.CharField(max_length=10)),
                ('InitialAmount', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Plan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=50)),
                ('Amount', models.CharField(max_length=10)),
                ('Duration', models.CharField(max_length=10)),
            ],
        ),
    ]