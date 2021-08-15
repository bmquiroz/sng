FROM centos:centos7

ARG SVC_CREDS

RUN adduser sng
RUN echo "$SVC_CREDS | chpasswd"
RUN usermod -aG wheel sng
RUN mkdir -p /home/sng/sng_api

# Install Python
RUN yum update -y
RUN yum install -y wget
RUN yum install -y make
RUN yum install -y gcc openssl-devel bzip2-devel libffi-devel
RUN yum group install -y "Development Tools"
RUN yum install -y openldap-devel python3-devel
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
