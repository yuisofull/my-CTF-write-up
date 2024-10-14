FROM ubuntu:focal

RUN apt-get update && apt-get install -y python3.8 python3-pip
RUN apt-get install xinetd -qy
RUN useradd -m md5Encryption
RUN chown -R root:root /home/md5Encryption
RUN chmod -R 755 /home/md5Encryption
RUN python3 -m pip install pycryptodome

CMD ["/usr/sbin/xinetd","-dontfork"]
