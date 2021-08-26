#!/usr/bin/env bash
# 0. Prepare your web servers 

# nginx install
apt-get -y update
apt-get -y install nginx
ufw allow 'Nginx HTTP'

# make directories
mkdir -p /data/
mkdir -p /data/web_static/
mkdir -p /data/web_static/releases/
mkdir -p /data/web_static/shared/
mkdir -p /data/web_static/releases/test/

# create fake HTML file
echo '<html><head></head><body><h1>Hello Fake Page</h1></body></html>' > index.html 
mv index.html /data/web_static/releases/test/

# create symbolic link
if [ -d /data/web_static/current ]
then
	rm /data/web_static/current
fi
ln -s /data/web_static/releases/test /data/web_static/current

# give ownership user and group with recursive option
chown -R ubuntu:ubuntu /data/

# add nginx configuration
sed -i '/:80 default_server/a location /hbnb_static/ {\n\talias /data/web_static/current/;\n}\n' /etc/nginx/sites-available/default
sed -i 's:/var/www/html:/data/web_static/current:' /etc/nginx/sites-available/default

# restart nginx configuration
service nginx restart
