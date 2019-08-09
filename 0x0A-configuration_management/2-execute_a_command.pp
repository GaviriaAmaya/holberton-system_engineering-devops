#Execute pkill on a process
exec { 'killmenow':
  command  => 'pkill killmenow'
  provider => shell,
}
