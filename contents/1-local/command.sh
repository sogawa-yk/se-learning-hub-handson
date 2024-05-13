docker build -t 1-local . # 1-localという名前でビルド
docker run -d -p 8080:80 1-local:latest # ビルドしたコンテナをバックグラウンドで起動
curl localhost:8080 # webサーバにアクセス