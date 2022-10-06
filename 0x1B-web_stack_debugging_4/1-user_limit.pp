#increase hard and soft limit fixToo Many Open Files Error

exec { 'soft-limit':
  command => 'echo "nginx       soft    holberton   10000" > /etc/security/limits.conf',
  path    => '/usr/local/bin/:/bin/'
}

exec { 'hard-limit':
  command => 'echo "nginx       hard    holberton  30000" > /etc/security/limits.conf',
  path    => '/usr/local/bin/:/bin/'
}
