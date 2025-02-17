from django.contrib.auth.models import AnonymousUser
from rest_framework.decorators import api_view
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken

from user.models import User

#登录验证
@api_view(['POST'])
def login(request):
    """
    用户登录接口，用户账号与密码匹配则返回成功信息。
    """
    userid = request.data.get('userid')
    userpassword = request.data.get('userpassword')

    if not userid or not userpassword:
        return Response({"error": "用户名和密码不能为空"}, status=status.HTTP_400_BAD_REQUEST)

    try:
        user = User.objects.get(userid=userid)

        if user.userpassword == userpassword:
            # 生成JWT token
            refresh = RefreshToken.for_user(user)
            access_token = str(refresh.access_token)

            return Response({
                "message": "登录成功",
                "data": {
                    "token": access_token,
                    "refresh_token": str(refresh)  # 返回 refresh token
                }
            }, status=status.HTTP_200_OK)
        else:
            return Response({"error": "密码错误"}, status=status.HTTP_401_UNAUTHORIZED)

    except User.DoesNotExist:
        return Response({"error": "用户不存在"}, status=status.HTTP_404_NOT_FOUND)




