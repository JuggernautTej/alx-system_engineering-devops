# This is a manifest that kills a process called killmenow
exec { 'kill_killmenow_process':
command     => 'pkill -f killmenow',
path        => '/usr/bin:/usr/sbin:/bin',
}