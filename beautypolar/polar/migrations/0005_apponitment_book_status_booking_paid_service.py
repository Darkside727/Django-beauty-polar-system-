# Generated by Django 3.0.7 on 2020-08-09 17:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('polar', '0004_auto_20200805_1614'),
    ]

    operations = [
        migrations.CreateModel(
            name='Book_status',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Booking_paid',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('paid', models.CharField(max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, null=True)),
                ('cost', models.IntegerField(null=True)),
                ('image', models.FileField(null=True, upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Apponitment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date1', models.DateField(null=True)),
                ('time1', models.TimeField(null=True)),
                ('customer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='polar.registration')),
                ('paid', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='polar.Booking_paid')),
                ('service', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='polar.Service')),
                ('status', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='polar.Book_status')),
            ],
        ),
    ]
