# set up your client SSH configuration file so that you can connect
# to a server without typing a password using Puppet
exec { '/etc/ssh/ssh_config':
  command => '/bin/echo -e "IdentityFile ~/.ssh/holberton\nPasswordAuthentication no" >> /etc/ssh/ssh_config',
  path    => '/etc/ssh/ssh_config',
}
