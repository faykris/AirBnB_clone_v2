# 5. Puppet for setup
# Redo the task #0 but by using Puppet:

exec { 'make_directories':
  command  => 'mkdir -p /data/web_static/releases/; mkdir -p /data/web_static/shared/; mkdir -p /data/web_static/releases/test/;',
  provider => shell,
}
exec { 'move_index_page':
  command  => 'echo "<html><head></head><body><h1>Hello Page!</h1></body></html>" > index.html; mv index.html /data/web_static/releases/test/',
  provider => shell,
}
exec { 'create_symlink':
  command  => 'ln -s /data/web_static/releases/test /data/web_static/current',
  provider => shell,
}
exec { 'append_location':
  command  => 'sed -i "/:80 default_server/a location /hbnb_static/ {\n\talias /data/web_static/current/;\n}\n" /etc/nginx/sites-available/default',
  provider => shell,
}
exec { 'sustitute_path':
  command  => 'sed -i "s:/var/www/html:/data/web_static/current:" /etc/nginx/sites-available/default',
  provider => shell,
}
exec { 'nginx_restart':
  command  => 'service nginx restart',
  provider => shell,
}
