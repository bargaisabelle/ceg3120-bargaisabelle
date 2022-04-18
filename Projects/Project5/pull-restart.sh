#!/bin/bash

# Pull docker image
# Docker pull bargaisabelle/mysite:latest
# Kill old running container (to clear host port)
echo "stopping contianer"
docker stop cheese

# Prunes latest
docker system prune -f -a

# Pull docker image post prune
echo "pulling image"
docker pull bargaisabelle/mysite:latest

# Run new image
echo "run image cheese"
docker run -d --name cheese -p 80:80 bargaisabelle/mysite:latest
