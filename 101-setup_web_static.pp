# 5. Puppet for setup
# Redo the task #0 but by using Puppet:

exec { 'prepare_servers':
  command  => 'apt-get -y update; apt-get -y install nginx; mkdir -p /data/web_static/releases/; mkdir -p /data/web_static/shared/; mkdir -p /data/web_static/releases/test/; echo "<html><head></head><body><h1>Hello Page!</h1></body></html>" > index.html; mv index.html /data/web_static/releases/test/; ln -sf /data/web_static/releases/test /data/web_static/current; chown -R ubuntu:ubuntu /data/; sed -i "/:80 default_server/a location /hbnb_static/ {\n\talias /data/web_static/current/;\n}\n" /etc/nginx/sites-available/default; sed -i "s:/var/www/html:/data/web_static/current:" /etc/nginx/sites-available/default; service nginx restart',
  provider => shell,
}
