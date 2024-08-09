# Working with containers
```sh
$ docker --version
Docker version 27.1.0, build 6312585
$ docker image list
REPOSITORY                                                            TAG       IMAGE ID       CREATED        SIZE
gitlab-pro.demcon.local:4567/ligalli/medring-oab/firmware/compilers   1.36      33a27ce6c12b   20 hours ago   2.21GB
$ docker container list
CONTAINER ID   IMAGE                                                                      COMMAND                  CREATED         STATUS         PORTS     NAMES
b65b5213690d   gitlab-pro.xxx.xxx:4567/projectX/productX/firmware/compilers:1.36   "/bin/sh -c 'echo Co…"   2 minutes ago   Up 2 minutes             projecX_devcontainer
```

remove the build folder
```sh 
rm -rf build/
```
