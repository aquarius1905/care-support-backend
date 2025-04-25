from exponent_server_sdk import (
    DeviceNotRegisteredError,
    PushClient,
    PushMessage,
    PushTicketError,
    PushServerError,
)
from requests.exceptions import ConnectionError, HTTPError

class NotificationService:
    @staticmethod
    def send_push_notification(token, title, message, extra=None):
        """
        Expo Push通知を送信する
        
        Args:
            token (str): ExpoのプッシュトークンC
            title (str): 通知のタイトル
            message (str): 通知のメッセージ
            extra (dict, optional): 追加データ
        
        Returns:
            bool: 送信が成功したかどうか
        """
        try:
            response = PushClient().publish(
                PushMessage(
                    to=token,
                    title=title,
                    body=message,
                    data=extra or {}
                )
            )
            
            # エラーチェック
            if response and response.validated_response:
                # 成功
                return True
            else:
                return False
                
        except (ConnectionError, HTTPError, PushServerError) as exc:
            # サーバー側のエラー
            return False
        except DeviceNotRegisteredError:
            # デバイスが登録されていない場合はトークンを削除すべき
            return False
        except PushTicketError:
            # プッシュチケットエラー
            return False