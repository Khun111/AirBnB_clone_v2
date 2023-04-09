# Task 0 with puppet

package { 'nginx':
ensure   => 'installed',
provider => 'apt'
}
file { '/data/':
ensure  => directory,
}
file { '/data/web_static/':
ensure => directory,
}
file { '/data/web_static/releases/':
ensure => directory,
}
file { '/data/web_static/shared/':
ensure => directory,
}
file { '/data/web_static/releases/test/':
ensure => directory,
}
file { '/data/web_static/releases/test/index.html':
ensure => file,
}
file { '/data/web_static/current':
ensure => 'link',
target => '/data/web_static/releases/test/',
force  => true,
}

exec { 'chown -R ubuntu:ubuntu /data/':
path => '/usr/bin/:/usr/local/bin/:/bin/'
}

file { '/var/www/':
ensure => directory,
}
file { '/var/www/html/':
ensure => directory,
}

file { '/var/www/html/index.html':
ensure  => 'file',
content => 'Are you a white lion or a sphynx? Make up your mind\n',
}

file { '/var/www/html/404.html':
ensure  => 'file',
content => "Ceci n'est pas une page - Error page\n",
}

file { '/etc/nginx/sites-enabled/default':
ensure  => 'file',
content => "server {\n    listen 80 default_server;\n    listen [::]:80 default_server;\n    root   /var/www/html;\n    index  index.html index.htm;\n    add_header X-Served-By ${hostname};\n    location /hbnb_static {\n        alias /data/web_static/current;\n    }\n    location /redirect_me {\n        return 301 https://oluwatobialure.hashnode.dev/;\n    }\n    error_page 404 /404.html;\n    location /404 {\n        root /var/www/html;\n        internal;\n    }\n}"
}

exec { 'nginx restart':
path => '/etc/init.d/',
}
