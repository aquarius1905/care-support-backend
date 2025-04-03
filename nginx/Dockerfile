FROM nginx:1.25-alpine

# デフォルト設定ファイルの削除
RUN rm /etc/nginx/conf.d/default.conf

# カスタム設定ファイルのコピー
COPY default.conf /etc/nginx/conf.d/