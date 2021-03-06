# Generated by Django 2.1.4 on 2018-12-22 11:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CreateMerchant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstName', models.CharField(max_length=100)),
                ('lastName', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=100)),
                ('nid', models.CharField(max_length=100)),
                ('dob', models.DateField()),
                ('address', models.TextField(blank=True)),
                ('business_name', models.CharField(max_length=100)),
                ('business_model', models.CharField(choices=[('1', 'New York'), ('2', 'Jackson Heights ')], default='1', max_length=50)),
                ('website', models.CharField(max_length=100)),
                ('fb_page', models.CharField(max_length=100)),
                ('bank_detail', models.CharField(choices=[('1', 'Bank'), ('2', 'Cash '), ('3', 'Wallet ')], default='2', max_length=50)),
                ('account_name', models.CharField(max_length=100)),
                ('account_number', models.CharField(default='a', max_length=100)),
                ('routing', models.CharField(max_length=100)),
                ('branch', models.CharField(max_length=100)),
                ('wallet_type', models.CharField(choices=[('1', 'Bank'), ('2', 'Cash '), ('3', 'Wallet ')], default='2', max_length=50)),
                ('wallet_number', models.CharField(max_length=100)),
                ('cFirstName', models.CharField(max_length=100)),
                ('cLastName', models.CharField(max_length=100)),
                ('cPhnNo', models.CharField(max_length=100)),
                ('cEmail', models.CharField(max_length=100)),
                ('agree', models.BooleanField(default=True)),
            ],
        ),
    ]
