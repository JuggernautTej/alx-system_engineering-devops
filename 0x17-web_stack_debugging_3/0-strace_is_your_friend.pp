# A puppet manuscript that fixes a 500 code error from an Apache

$the_file = '/var/www/html/wp-settings.php'

exec {'replace_line':
command => "sed -i 's/phpp/php/g' ${the_file}",
path    => '/usr/local/bin/:/bin/'
}