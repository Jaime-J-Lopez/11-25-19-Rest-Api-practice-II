# Generated by Django 2.2.7 on 2019-11-25 22:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product', models.CharField(choices=[('savings', 'SAVINGS'), ('checking', 'CHECKING'), ('credit', 'CREDIT')], default=('savings', 'SAVINGS'), max_length=30)),
                ('customer_email', models.EmailField(max_length=100)),
            ],
        ),
    ]
