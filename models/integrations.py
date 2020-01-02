from django.db import models


class TradeKingCallResponse(models.Model):
    call_id = models.CharField(primary_key=True, blank=False, null=False)
    rest_operation = models.ForeignKey('TradeKingRestOperation', to_field="operation_id", blank=False, null=True,
                                       on_delete=models.PROTECT)
    call_datetime = models.DateTimeField(blank=True, null=True)
    error = models.CharField(blank=True, null=True)
    elapsed_time = models.IntegerField(blank=True, null=True)


class TradeKingRestOperation(models.Model):
    BASE = 'https://api.tradeking.com/v1/'
    HTTP_METHOD = ['get', 'post']
    OPERATION_TYPE = ['accounts', 'member']

    operation_id = models.AutoField(primary_key=True, blank=False, null=False)
    operation = models.CharField(blank=False, null=False)
    operation_type = models.CharField(blank=True, null=True, choices=OPERATION_TYPE)
    http_method = models.CharField(blank=True, null=True, choices=HTTP_METHOD)
    account_level = models.BooleanField(blank=False, null=False)