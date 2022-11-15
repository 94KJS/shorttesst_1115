from rest_framework.permissions import BasePermission
from datetime import timedelta, datetime
from django.utils import timezone
from rest_framework.exceptions import APIException
from rest_framework import status


class GenericAPIException(APIException):
    def __init__(self, status_code, detail=None, code=None):
        self.status_code = status_code
        super().__init__(detail=detail, code=code)


class RegisteredMoreThanThreeDaysUser(BasePermission):
    """
    가입일 기준 3일 이상 지난 사용자만 접근 가능
    """

    SAFE_METHODS = ("GET",)
    message = "가입 후 3일 이상 지난 사용자만 사용하실 수 있습니다."

    def has_permission(self, request, view):
        user = request.user

        if not user.is_authenticated:
            response = {
                "detail": "서비스를 이용하기 위해 로그인 해주세요.",
            }
            raise GenericAPIException(
                status_code=status.HTTP_401_UNAUTHORIZED, detail=response
            )

        # 로그인 사용자가 get 요청 시 True
        if user.is_authenticated and request.method in self.SAFE_METHODS:
            return True

        return bool(
            user.is_authenticated
            and request.user.join_date < (timezone.now() - timedelta(days=3))
        )
