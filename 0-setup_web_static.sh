#!/usr/bin/env bash
# 0. Prepare your web servers 

# nginx install
sudo apt-get -y update
sudo apt-get -y install nginx
sudo ufw allow 'Nginx HTTP'

# make directories
mkdir -p /data/
mkdir -p /data/web_static/
mkdir -p /data/web_static/releases/
mkdir -p /data/web_static/shared/
mkdir -p /data/web_static/releases/test/

# create fake HTML file
echo '<html><head></head><body><h1>Hello Fake Page</h1></body></html>' > index.html 
sudo mv index.html /data/web_static/releases/test/

# create symbolic link
if [ -d /data/web_static/current ]
then
	sudo rm /data/web_static/current
fi
sudo ln -s /data/web_static/releases/test/ /data/web_static/current

# give ownership user and group with recursive option
chown -R ubuntu:ubuntu /data/

# add nginx configuration
# def_route="root /var/www/html;"
# new_route="root /data/web_static/current;"
sed -i '/:80 default_server/a location /hbnb_static/ {\n\talias /data/web_static/current/;\n}' /etc/nginx/sites-available/default
# sed -i 's/root /\$def_route/ \$new_route' /etc/nginx/sites-available/default

# restart nginx configuration
sudo service nginx restart
