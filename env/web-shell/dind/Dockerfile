# Docker in Docker の公式イメージを使用
FROM docker:dind

# /etc/docker ディレクトリの作成
RUN mkdir -p /etc/docker

# Dockerデーモンの設定
# TLSを無効にしてHTTPで通信する設定ファイルを作成
RUN echo '{ "hosts": ["tcp://0.0.0.0:2375", "unix:///var/run/docker.sock"] }' > /etc/docker/daemon.json

# ポート2375を開放（Docker API用）
EXPOSE 2375

# Dockerデーモンをカスタム設定ファイルで直接起動
CMD ["dockerd", "--config-file=/etc/docker/daemon.json"]
