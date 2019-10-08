# Install NGINX w/ Puppet

exec { 'inginx':
     command => 'apt-get install nginx'
     provider => shell,
}