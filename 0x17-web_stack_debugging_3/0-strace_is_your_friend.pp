# Fix the error located by strace using puppet manifest
exec { 'The fixer':
  command => "sed -i 's/phpp/php/' /var/www/html/wp-settings.php",
  path    => ['/bin']
}