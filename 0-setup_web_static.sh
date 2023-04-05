#!/usr/bin/env bash
# Bash script that sets up your web servers for the deployment of web_static
if [ command nginx] | grep 'not found'; then
  sudo apt-get install -y nginx;
fi
if [ ! -d '/data/' ]; then
  sudo mkdir /data/;
fi
if [ ! -d '/data/web_static/' ]; then
  sudo mkdir -p /data/web_static/;
fi
if [ ! -d '/data/web_static/releases/' ]; then
  sudo mkdir -p /data/web_static/releases/;
fi
if [ ! -d '/data/web_static/shared/' ]; then
  sudo mkdir -p /data/web_static/shared/;
fi
if [ ! -d '/data/web_static/releases/test/' ]; then
  sudo mkdir -p /data/web_static/releases/test/;
fi
echo 'Are you a sphinx or a white lion, make up your mind Kimba' | sudo tee /data/web_static/releases/test/index.html
sudo ln -sf /data/web_static/current /data/web_static/releases/test/
sudo chown -R ubuntu:ubuntu /data/
sed -i.bak '/listen 80 default_server/a \tlocation \/hbnb_static {\n\talias /data/web_static/current/;\n\t}' menginx
