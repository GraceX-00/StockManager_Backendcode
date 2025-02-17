#创建 Serializer 以便转换数据格式：
from rest_framework import serializers
from .models import User

class AccountSerializer(serializers.Serializer):
    userid = serializers.CharField()
    username = serializers.CharField()
    userpassword = serializers.CharField()
    userphone = serializers.CharField()
    useremail = serializers.CharField()

