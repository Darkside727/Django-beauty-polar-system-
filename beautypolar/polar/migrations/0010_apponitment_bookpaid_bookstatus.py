# Generated by Django 3.0.7 on 2020-08-15 16:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('polar', '0009_auto_20200815_1628'),
    ]

    operations = [
        migrations.CreateModel(
            name='BookPaid',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('paid', models.CharField(max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='BookStatus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('b_status', models.CharField(max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Apponitment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date1', models.DateField(null=True)),
                ('time1', models.TimeField(null=True)),
                ('customer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='polar.registration')),
                ('paid', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='polar.BookPaid')),
                ('service', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='polar.Service')),
                ('status', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='polar.BookStatus')),
            ],
        ),
    ]
