from rest_framework.authentication import BaseAuthentication
from rest_framework.exceptions import AuthenticationFailed
from my_site import models


class Auth(BaseAuthentication):
    def authenticate(self, request):
        token = request.query_params.get("token")
        # print(token)
        obj = models.UserToken.objects.filter(token=token).first()
        # print(obj)
        if not obj:
            raise AuthenticationFailed({"code":1001,"error":"认证失败111"})
        return(obj.user.username, obj)