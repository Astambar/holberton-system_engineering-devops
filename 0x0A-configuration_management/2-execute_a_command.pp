# créer un manifeste qui tue un processus nommé killmenow
exec { 'pkill':
  path    => '/usr/bin:/usr/sbin:/bin',
  command => 'pkill killmenow',
}
