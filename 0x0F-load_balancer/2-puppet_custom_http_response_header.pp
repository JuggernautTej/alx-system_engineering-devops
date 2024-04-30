#Using Puppet automate the task of creating a custom HTTP header response

package { 'ngnix':
  ensure => installed,
}

file { '/usr/share/nginx/html/index.html':
  ensure  => present,
  content => 'Hello World!',
}

service { 'nginx':
  ensure   => running,
  enable   => true,
  requirre => Package['nginx'],
}

exec { 'add_header':
  command       => '/bin/sed -i "/http {/a\        add_header X-Served-By $HOSTNAME;" /etc/nginx/nginx.conf',
    path        => ['/bin', '/sbin', '/usr/bin', '/usr/sbin'],
    refreshonly => true,
    subscribe   => Service['nginx'],
}

exec { 'nginx_config_test':
  command     => 'nginx -t',
  path        => ['/bin', '/sbin', '/usr/bin', '/usr/sbin'],
  refreshonly => true,
  subscribe   => Exec['add_header'],
}
