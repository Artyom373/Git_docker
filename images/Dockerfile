FROM ubuntu
RUN apt-get install wget
RUN wget -O - https://ftp-master.debian.org/keys/archive-key-8-security.asc | apt-key add -
RUN wget -O - https://ftp-master.debian.org/keys/archive-key-8.asc | apt-key add -
RUN apt-key adv --keyserver keyserver.ubuntu.com --recv-keys 8B48AD6246925553
RUN apt-get update && apt-get install -y cowsay && ln -s /usr/games/cowsay /usr/bin/cowsay
ENTRYPOINT ["cowsay"]
