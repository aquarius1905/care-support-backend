from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework import exceptions
from django.contrib.auth import authenticate
from django.utils.translation import gettext_lazy as _

class StaffTokenObtainPairSerializer(TokenObtainPairSerializer):
    # 認証エラーメッセージをカスタマイズするためにvalidateメソッドをオーバーライド
    def validate(self, attrs):
        authenticate_kwargs = {
            self.username_field: attrs[self.username_field],
            'password': attrs['password'],
        }
        
        # 認証を試みる
        user = authenticate(**authenticate_kwargs)

        # 認証失敗の場合
        if user is None:
            raise exceptions.AuthenticationFailed(
                _('ユーザー名またはパスワードが正しくありません。'),
                'invalid_credentials'
            )
        
        # 無効なユーザー（アクティブでない）の場合
        if not user.is_active:
            raise exceptions.AuthenticationFailed(
                _('このアカウントは無効化されています。'),
                'user_inactive'
            )
            
        # スタッフユーザーでない場合
        if user.user_type != 'staff':
            raise exceptions.AuthenticationFailed(
                _('このユーザーは施設スタッフではありません。'),
                'not_staff_user'
            )

        # 親クラスのvalidateに処理を委譲（tokenの生成など）
        data = super(TokenObtainPairSerializer, self).validate(attrs)
        
        return data