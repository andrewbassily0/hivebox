FROM debian:jessie 

WORKDIR /home/vito/hivebox/hivebox/

COPY  version.py ./

CMD [ "python", "./version.py"]
