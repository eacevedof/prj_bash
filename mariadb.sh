#!/bin/sh

cmd='
docker-compose --env-file=/Users/ioedu/projects/prj_docker_imgs/mariadb-univ/.env -f /Users/ioedu/projects/prj_docker_imgs/mariadb-univ/docker-compose.yml up 
'
eval $cmd
