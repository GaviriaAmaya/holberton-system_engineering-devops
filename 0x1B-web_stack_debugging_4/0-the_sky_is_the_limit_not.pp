# Increase the limit of requests on Nginx Web Server
exec {'Config file':
path     => '/etc/default/nginx',
command  => "echo 'ULIMIT=\"-n 4096\"' > /etc/default/nginx",
provider => shell
}
-> exec {'Restart':
command  =>  'service nginx restart',
provider => shell
}