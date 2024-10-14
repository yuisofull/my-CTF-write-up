FROM ubuntu:focal

RUN apt-get update && apt-get install -y python3.8 python3-pip
RUN apt-get install xinetd -qy
RUN useradd -m easyRSA
RUN chown -R root:root /home/easyRSA
RUN chmod -R 755 /home/easyRSA
RUN python3 -m pip install pycryptodome

CMD ["/usr/sbin/xinetd","-dontfork"]
