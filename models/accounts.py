from django.db import models


class Account(models.Model):
    account_id = models.AutoField(primary_key=True, blank=False, null=False)
    account_number = models.IntegerField(blank=False, null=False)
    account_type = models.ForeignKey('AccountType', to_field="account_type_id", blank=False, null=True,
                                     on_delete=models.PROTECT)
    account_open_date = models.DateTimeField(blank=True, null=True)
    firm = models.ForeignKey('Firm', to_field="firm_id", blank=False, null=False, on_delete=models.PROTECT)
    joint_account = models.BooleanField(blank=False, null=False)
    primary_account_holder = models.ForeignKey('Person', to_field='person_id', blank=False, null=True,
                                               on_delete=models.PROTECT)
    household = models.ForeignKey('Households', to_field='household_id', blank=True, null=True,
                                  on_delete=models.PROTECT)
    holds_assets = models.BooleanField(blank=False, null=False)
    account_value = models.DecimalField(max_digits=10, decimal_places=5, blank=False, null=False)
    record_last_updated = models.DateTimeField(blank=True, null=True)


class AccountType(models.Model):
    account_type_id = models.AutoField(primary_key=True, blank=False, null=False)
    account_type = models.CharField(blank=False, null=False)
    pre_tax = models.BooleanField(blank=False, null=False)
    investment = models.BooleanField(blank=False, null=False)


class Firm(models.Model):
    firm_id = models.AutoField(primary_key=True, blank=False, null=False)
    firm_name = models.CharField(blank=False, null=False)


class AccountSecurities(models.Model):
    account_id = models.ForeignKey('Accounts', to_field="account_id", blank=False, null=True,
                                   on_delete=models.PROTECT)
    symbol = models.CharField(blank=False, null=False)
    quantity = models.DecimalField(max_digits=10, decimal_places=5, blank=False, null=False)
    asset_class = models.CharField(blank=False, null=False)
    cost_basis = models.DecimalField(max_digits=10, decimal_places=5, blank=False, null=False)
    record_last_updated = models.DateTimeField(blank=True, null=True)


class AccountCash(models.Model):
    account_id = models.ForeignKey('Accounts', to_field="account_id", blank=False, null=True,
                                   on_delete=models.CASCADE)
    cash = 'tmp'


class Securities(models.Model):
    symbol = models.CharField(blank=False, null=False)
    asset_class = models.CharField(blank=False, null=False)
    last_price = models.DecimalField(max_digits=10, decimal_places=2, blank=False, null=False)
    call_id = models.ForeignKey('TradeKingCallResponse', to_field="call_id", blank=False, null=True,
                                on_delete=models.PROTECT)
    curr_value = models.BooleanField(blank=False, null=False)
