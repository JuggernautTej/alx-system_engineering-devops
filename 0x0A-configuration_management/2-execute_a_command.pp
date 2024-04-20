# This is a manifest that kills a process called killmenow
exec { 'kill_killmenow_process':
command     => 'pkill killmenow',
path        => '/bin:/usr/bin',
refreshonly => true,
subscribe   => File['/path/to/notify'],
}