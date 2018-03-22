#!bash
DB_ROOT_PW=root
DB_USER=dev
DB_PW=dev
DB_DATA_PATH=/var/docker_data/mongo/data/
DB_PROT=27017

apt update
apt install docker mongodb-clients
docker pull mongo
docker run -p ${DB_PROT}:27017 --name mongo_test -v ${DB_DATA_PATH}:/data/db -d mongo --auth
echo "input this: db.createUser({ user: 'dev', pwd: 'dev', roles: [ { role: 'userAdminAnyDatabase', db: 'admin' } ] });"
echo "and exit"
docker exec -it some-mongo mongo admin