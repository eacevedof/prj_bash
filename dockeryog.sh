#!/bin/sh

# fuente: https://github.com/eacevedof/prj_docker_imgs/tree/master/sqlyog
open -a XQuartz
IP=$(ifconfig en0 | grep inet | awk '$1=="inet" {print $2}')
/opt/X11/bin/xhost + $IP

docker run \
      -it \
      --rm \
      -d \
      -h hyog \
      -e DISPLAY=$IP:0 \
      -v /tmp/.X11-unix:/tmp/.X11-unix:ro \
      -v $HOME/dockercfg/sqlyog:/shared \
      -v $HOME/dockercfg/db_dumps:/db_dumps \
      --network mariadb-univ_net \
      --name cyog yantis/sqlyog >/dev/null