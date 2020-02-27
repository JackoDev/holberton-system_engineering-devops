# Puppet script to fix server processes.
exec { 'limits':
  command => '/bin/sed -i "s/15/1500/g" /etc/default/nginx'
}
-> exec {'restart':
  command => '/usr/sbin/service nginx restart'
}

