/*
Modifie la configuration du système d'exploitation afin qu'il soit possible de se connecter
avec l'utilisateur holberton et ouvre un fichier sans aucun message d'erreur
*/
exec { '/usr/bin/env sed -i "s/holberton/foo/" /etc/security/limits.conf': }
