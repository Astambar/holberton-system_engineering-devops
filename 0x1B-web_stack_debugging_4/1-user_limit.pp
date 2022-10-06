# augmenter la correction des limites matérielles et logicielles Trop d'erreurs de fichiers ouverts

exec { 'limit-soft':
  command => 'echo "nginx       soft    holberton   1000" > /etc/security/limits.conf',
  path    => '/usr/local/bin/:/bin/'
}

exec { 'limit-hard':
  command => 'echo "nginx       hard    holberton  2000" > /etc/security/limits.conf',
  path    => '/usr/local/bin/:/bin/'
}
