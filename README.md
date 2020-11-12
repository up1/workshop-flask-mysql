## Start services

```
$docker-compose up -d database
$docker-compose up -d backend
$docker-compose up -d frontend

$docker-compose ps
$docker-compose logs --follow
```

## Access to database

```
$docker container exec -it database bash
/#mysql -udemo_user -p
>use demo
>show tables;
>describe user;
>select * from user;
```

## Clear all

```
$docker-compose down
$docker volume prune
```
