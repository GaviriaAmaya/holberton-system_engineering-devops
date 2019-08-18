#Execute pkill on a process
exec { 'killmenow':
<<<<<<< HEAD
  command => '/usr/bin/pkill killmenow'
}
=======
  command  => 'pkill killmenow',
  provider => shell,
}
>>>>>>> 1ffb65e190406f7a79f4e5de6b8756e688be1bdc
