# 基本イメージ
FROM python:3.8-slim

# 作業ディレクトリの設定
WORKDIR /app

# 依存関係のインストール
COPY requirements.txt .
RUN pip install -r requirements.txt

# アプリケーションファイルをコピー
COPY app .

COPY manifests/ /config/
# アプリケーションの起動
CMD ["python", "run.py"]
