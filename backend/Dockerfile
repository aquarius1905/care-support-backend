FROM python:3.13-slim

# 環境変数の設定
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# 必要なシステムパッケージをインストール
RUN apt-get update && apt-get install -y --no-install-recommends \
    libpq-dev \
    gcc \
    && rm -rf /var/lib/apt/lists/*

# 作業ディレクトリの作成
WORKDIR /app

# 必要なパッケージをインストール
COPY requirements.txt /app/
RUN pip install --upgrade pip && \
    pip install -r requirements.txt

# アプリケーションのコピー
COPY . /app/

# ポート公開
EXPOSE 8000

# Djangoの起動コマンド
CMD ["sh", "-c", "python manage.py migrate && python manage.py runserver 0.0.0.0:8000"]