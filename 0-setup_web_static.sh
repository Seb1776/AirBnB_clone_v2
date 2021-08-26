#!/usr/bin/env bash
# this script install Ngingx Service and verify if exist some dir and create

# Update dependencies and Nginx
sudo apt-get -y update
sudo apt-get -y upgrade
sudo apt-get install -y nginx

# Verify for dir existance
sudo mkdir -p /data/web_static/shared/
sudo mkdir -p /data/web_static/releases/test/

# Create a fake HTML file
echo '<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>' > /data/web_static/releases/test/index.html

# Create a symbolic link, in case that it already existed, delet it and recreate it
rm /data/web_static/current

ln -sf  /data/web_static/releases/test/ /data/web_static/current

# Assign ubuntu owner
sudo chown -R ubuntu:ubuntu /data

# Update Nginx config
echo "server {
    listen 80 default_server;
    listen [::]:80 default_server;
    add_header X-Served-By $HOSTNAME;
    root   /var/www/html;
    index  index.html index.htm;
    location /hbnb_static {
        alias /data/web_static/current;
        index index.html index.htm;
    }
    location /redirect_me {
        return 301 https://github.com/mauriciosierrac/;
    }
    error_page 404 /404.html;
    location /404 {
      root /var/www/html;
      internal;
    }
}" > /etc/nginx/sites-available/default

# Restart Nginx services
sudo service nginx restart
