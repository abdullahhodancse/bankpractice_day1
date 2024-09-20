# Generated by Django 5.0.6 on 2024-09-05 07:22

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_remove_userbankaccount_phone_useraddress_country'),
        ('transactions', '0003_remove_loanrequestform_transactions_ptr_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transactions',
            name='transaction_type',
            field=models.IntegerField(choices=[(1, 'Deposite'), (2, 'Withdraw'), (3, 'Loan'), (4, 'Loan Paid'), (5, 'Transfer')], null=True),
        ),
        migrations.CreateModel(
            name='Tranfer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Transfer_money', models.DecimalField(decimal_places=2, max_digits=12)),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='transfer', to='accounts.userbankaccount')),
            ],
        ),
    ]
