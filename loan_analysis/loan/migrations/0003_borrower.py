# Generated by Django 5.0.3 on 2025-02-09 18:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loan', '0002_lender'),
    ]

    operations = [
        migrations.CreateModel(
            name='Borrower',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('phone', models.CharField(max_length=15)),
                ('loan_amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('purpose', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
