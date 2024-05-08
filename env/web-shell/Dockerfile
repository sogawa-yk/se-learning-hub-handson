FROM ubuntu:latest

# 必要なパッケージのインストール
RUN apt-get update && apt-get install -y \
  ttyd \
  bash \
  curl \
  && rm -rf /var/lib/apt/lists/*

# ttydを使ってbashを公開
CMD ["ttyd", "-p", "8080", "bash"]
