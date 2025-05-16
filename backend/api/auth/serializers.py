from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework import exceptions, serializers
from django.contrib.auth import authenticate
from django.utils.translation import gettext_lazy as _

class StaffTokenObtainPairSerializer(TokenObtainPairSerializer):
    username_field = 'email'  # ユーザー名フィールドをemailに設定
    
    # emailとpasswordフィールドを明示的に定義
    email = serializers.EmailField(label=_("メールアドレス"))
    password = serializers.CharField(
        label=_("パスワード"),
        style={'input_type': 'password'},
        trim_whitespace=False,
        write_only=True
    )
    
    def validate(self, attrs):
        authenticate_kwargs = {
            'email': attrs['email'],
            'password': attrs['password'],
        }
        
        # 認証を試みる
        user = authenticate(**authenticate_kwargs)

        # 認証失敗の場合
        if user is None:
            raise exceptions.AuthenticationFailed(
                _('メールアドレスまたはパスワードが正しくありません。'),
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
        data = super().validate(attrs)
        
        return data