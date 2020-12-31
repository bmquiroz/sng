FROM centos:centos7

# ENV http_proxy http://builder:K33pSecret@internal-EUIEO-INT-ELB-COMMON-896878853.eu-west-1.elb.amazonaws.com:3228
# ENV https_proxy http://builder:K33pSecret@internal-EUIEO-INT-ELB-COMMON-896878853.eu-west-1.elb.amazonaws.com:3228
# ENV no_proxy=localhost,127.0.0.1,169.254.169.254,.aon.com,.aon.net,.ie.aon.bz

ARG SVC_CREDS

RUN adduser sng
RUN echo "$SVC_CREDS | chpasswd"
RUN usermod -aG wheel sng
RUN mkdir -p /home/sng/sng_api

# Install Python
RUN yum update -y
RUN yum install -y wget
RUN yum install -y make
RUN yum install -y gcc openssl-devel bzip2-devel  libffi-devel
WORKDIR /usr/src
RUN wget https://www.python.org/ftp/python/3.7.0/Python-3.7.0.tgz
RUN tar xzf Python-3.7.0.tgz
WORKDIR /usr/src/Python-3.7.0
RUN ./configure --enable-optimizations
RUN make altinstall
RUN rm -f /usr/src/Python-3.7.0.tgz

# Install PostgreSQL dependencies
RUN yum install -y postgresql-devel 

# Set up env
WORKDIR /home/sng/sng_api
ENV VIRTUAL_ENV=/home/sng/sng_api/venv
RUN python3.7 -m venv $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"
COPY . /home/sng/sng_api
RUN pip install -r requirements.txt

# Install web services
RUN pip install gunicorn 
RUN pip install psycopg2

# Update dirs
WORKDIR /home/sng/sng_api
RUN chown -R sng:sng /home/sng
RUN chmod 710 /home/sng

# Start services
# EXPOSE 5000
RUN ["chmod", "+x", "./gunicorn_starter.sh"]
ENTRYPOINT ["./gunicorn_starter.sh"]
