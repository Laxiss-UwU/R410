docker run --rm -d -p 3306:3306 --env MYSQL_ROOT_PASSWORD=foo -v vol-sql:/var/lib/mysql --name bdd mysql
docker run -d -p 8000:8000 --name final tp2c
