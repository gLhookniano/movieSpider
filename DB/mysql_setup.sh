#!bash
DB_ROOT_PW=root
DB_USER=dev
DB_PW=dev
DB_DATA_PATH=/var/docker_data/mysql/data/
DB_PROT=3306

apt update
apt install docker mysql-client python3 python3-pip
python3 -m pip install mysql-connector-python
docker pull mariadb
docker run -p ${DB_PROT}:3306 --name mariadb_test -v ${DB_DATA_PATH}:/var/lib/mysql -e MYSQL_ROOT_PASSWORD=${DB_ROOT_PW} -e MYSQL_USER=${DB_USER} -e MYSQL_PASSWORD=${DB_PW} -d mariadb
mysql -h 0.0.0.0 -u root -p < ./mysql_db_create.sql