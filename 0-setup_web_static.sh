#!/usr/bin/env bash
# My Bash script that sets up your web servers for the deployment of web_static
apt-get update
if ! command -v nginx &> /dev/null; then
  sudo apt-get install -y nginx;
fi
sudo ufw allow 'Nginx HTTP'
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
sudo tee /data/web_static/releases/test/index.html > /dev/null << EOF
<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>
EOF
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current
sudo chown -R ubuntu:ubuntu /data/
sed -i '/location \/ {/i \    location \/hbnb_static {\n        alias /data/web_static/current/;\n    }' /etc/nginx/sites-enabled/default
sudo service nginx restart
