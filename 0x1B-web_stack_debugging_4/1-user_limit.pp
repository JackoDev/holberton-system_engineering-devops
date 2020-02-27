# Puppet script to fix file limitations
exec { 'soft_file':
  command => '/bin/sed -i "holberton soft nofile 4/holberton hard nofile 1500/" /etc/security/limits.conf'
}
exec { 'hard_file':
  command => '/bin/sed -i "holberton hard nofile 5/holberton hard nofile 1500/" /etc/security/limits.conf'
}
-> exec {'restart_sysctl':
  command => '/usr/sbin/sysctl -p'
}

