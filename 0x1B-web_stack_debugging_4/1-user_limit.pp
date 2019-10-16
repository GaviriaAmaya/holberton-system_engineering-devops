# Allows holberton user change limits with no error messages
exec {'Change hard lims':
command  => "sed -i 's/holberton hard nofile 5/holberton hard no file 10000/g' \
/etc/security/limits.conf",
provider => shell
}
-> exec {'Change Soft Lims':
command  => "sed -i 's/holberton soft nofile 4/holberton soft no file 10000/g' \
/etc/security/limits.conf",
provider => shell
}
-> exec {'Rstart':
command  => 'sysctl -p',
provider => shell
}