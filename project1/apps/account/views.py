from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .models import Account
from .serializers import AccountSerializer

@api_view(['GET', 'POST'])
def account_list(request):
    """
    处理 GET 请求返回所有账户数据，POST 请求创建新账户

    目前已实现get请求(获取数据)
    """
    if request.method == 'GET':
        accounts = Account.objects.all()
        serializer = AccountSerializer(accounts, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    elif request.method == 'POST':
        data = request.data
        account = Account(
            account_id=data.get('account_id'),
            account_name=data.get('account_name'),
            a_type=data.get('a_type'),
            a_code=data.get('a_code'),
            a_number=data.get('a_number'),
            a_money0=data.get('a_money0')

        )
        account.save()
        return Response({"message": "Account created successfully"}, status=status.HTTP_201_CREATED)
