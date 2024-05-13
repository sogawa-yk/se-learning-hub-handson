FROM ubuntu:latest

# 必要なパッケージのインストール
RUN apt-get update && apt-get install -y \
  ttyd \
  bash \
  curl \
  software-properties-common \
  apt-transport-https \
  gnupg \
  git \
  && rm -rf /var/lib/apt/lists/*

# Docker CLIをインストール
RUN curl -fsSL https://download.docker.com/linux/ubuntu/gpg | apt-key add - \
  && add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable" \
  && apt-get update \
  && apt-get install -y docker-ce-cli

# 環境変数の設定、Docker Daemonのアドレスを指定
ENV DOCKER_HOST=tcp://docker-daemon:2375

# ハンズオン資材をDL
RUN git clone https://github.com/sogawa-yk/se-learning-hub-handson.git

# ttydを使ってbashを公開
CMD ["ttyd", "bash"]
