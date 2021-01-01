sudo /etc/init.d/mysql start
mysql -uroot -e "CREATE DATABASE mubase;"
mysql -uroot -e "CREATE USER 'django@localhost' IDENTIFIED BY 'pass123';"
mysql -uroot -e "GRANT ALL ON mubase.* TO 'django@localhost';"
mysql -uroot -e "FLUSH PRIVILEGES;"