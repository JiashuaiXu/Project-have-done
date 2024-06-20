# Generated by Django 4.2.2 on 2024-04-13 08:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ProfitStatement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('report_date', models.DateField()),
                ('total_revenue', models.DecimalField(decimal_places=2, max_digits=19)),
                ('total_cost', models.DecimalField(decimal_places=2, max_digits=19)),
                ('net_profit', models.DecimalField(decimal_places=2, max_digits=19)),
                ('basic_earnings_per_share', models.DecimalField(decimal_places=2, max_digits=19)),
            ],
            options={
                'db_table': 'profit_statements',
            },
        ),
    ]