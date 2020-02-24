FROM ubuntu
RUN apt-get update -y && apt-get install -y cowsay && ln -s /usr/games/cowsay /usr/bin/cowsay
ENTRYPOINT ["cowsay"]
