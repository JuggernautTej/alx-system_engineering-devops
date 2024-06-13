# Allows user holberton to login and open files without error

# Reset hard limit for the user
exec { 'increase-hard-file-limit-for-holberton-user':
command => "sed -i '/^holberton hard/a/4/50000' /etc/security/limits.conf",
path    =>  '/usr/local/bin/:/bin/'
}

# Reset soft file limit for holberton user
exec { 'increase-soft-file-limit-for-holberton-user':
command => "sed -i '/^holberton soft/s/5/50000' /etc/security/limits.conf",
path    =>  '/usr/local/bin/:/bin/'
}
