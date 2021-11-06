# Script that sets up web servers for deployment of web_static

# nginx config file
$nginx_conf = "server {
    listen 80 default_server;
    listen [::]:80 default_server;
    root   /var/www/html;
    index  index.html index.htm;
    location /hbnb_static {
        alias  /data/web_static/current;
        index  index.html index.htm;
    }
}"

# Test file
$test_file = "\
<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>
"

# Install nginx if not present
package { 'nginx':
  ensure   => 'present',
  provider => 'apt'
}

# Create directory tree
file { ['/data/', '/data/web_static/', '/data/web_static/releases/',
        '/data/web_static/releases/test/', '/data/web_static/shared']:
  ensure => 'directory',
  owner  => 'ubuntu',
  group  => 'ubuntu'
}

# Create test file
file {'/data/web_static/releases/test/index.html':
  ensure  => 'present',
  content => $test_file,
  owner   => 'ubuntu',
  group   => 'ubuntu'
}

# Create symlink
file { '/data/web_static/current':
  ensure => 'link',
  target => '/data/web_static/releases/test/',
  force  => yes,
  owner  => 'ubuntu',
  group  => 'ubuntu',
}

# Change nginx config
file { '/etc/nginx/sites-available/default':
  ensure  => 'present',
  content => $nginx_conf,
  require => Package['nginx']
}

# Run service nginx
service { 'nginx':
  ensure  => 'running',
  require => Package['nginx']
}
