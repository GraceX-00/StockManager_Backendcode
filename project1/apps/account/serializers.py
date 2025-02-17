#创建 Serializer 以便转换数据格式：
from rest_framework import serializers
from .models import Account

class AccountSerializer(serializers.Serializer):
    account_id = serializers.CharField()
    account_name = serializers.CharField()
    a_type = serializers.CharField()
    a_code = serializers.CharField()
    a_number = serializers.CharField()
    a_money0=serializers.IntegerField()
