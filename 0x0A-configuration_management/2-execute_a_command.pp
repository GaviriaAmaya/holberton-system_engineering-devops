#Execute pkill on a process
exec { 'killmenow':
  command => '/usr/bin/pkill killmenow'
}