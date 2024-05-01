# 基本イメージを指定
FROM ubuntu:20.04

# Nginxをインストール
RUN apt-get update && apt-get install -y nginx

# このコンテナが外部に公開したいポート番号（ドキュメントのような役割）
EXPOSE 9000

# ホストのindex.htmlをコンテナにコピー
COPY ./index.html /var/www/html/index.html

# Nginxを実行
CMD ["nginx", "-g", "daemon off;"]