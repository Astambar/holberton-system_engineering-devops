# Modifie la configuration du système d'exploitation afin qu'il soit possible de se connecter avec l'utilisateur holberton et ouvre un fichier sans aucun message d'erreur

exec { 'soft-limit':
  command => 'echo "nginx       soft    holberton   1000" > /etc/security/limits.conf',
  path    => '/usr/local/bin/:/bin/'
}

exec { 'hard-limit':
  command => 'echo "nginx       hard    holberton  2000" > /etc/security/limits.conf',
  path    => '/usr/local/bin/:/bin/'
}
