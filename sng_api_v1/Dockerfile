FROM centos:centos7

RUN adduser sng
RUN echo "" | chpasswd
RUN usermod -aG wheel sng
RUN mkdir -p /home/sng/sng_api_v1

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

# Set up env
WORKDIR /home/sng/sng_api_v1
ENV VIRTUAL_ENV=/home/sng/sng_api_v1/venv
RUN python3.7 -m venv $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"
COPY . /home/sng/sng_api_v1
RUN pip install -r requirements_dev.txt

# Install web services
RUN pip install gunicorn  
RUN yum install -y epel-release
RUN yum install -y nginx
COPY nginx.conf /etc/nginx/
RUN gunicorn --bind 0.0.0.0:5000 name_string_api:app

# Install Python and Pip 2.7 (for Supervisor)
RUN yum install -y gcc
WORKDIR /usr/src
RUN wget https://www.python.org/ftp/python/2.7.10/Python-2.7.10.tgz
RUN tar xzf Python-2.7.10.tgz
WORKDIR /usr/src/Python-2.7.10
RUN ./configure
RUN make altinstall
WORKDIR /tmp
RUN curl "https://bootstrap.pypa.io/get-pip.py" -o "get-pip.py"
RUN python2.7 get-pip.py

# Install Supervisor
RUN pip2.7 install supervisor
RUN echo_supervisord_conf
RUN echo_supervisord_conf > /etc/supervisord.conf
RUN supervisord -c /etc/supervisord.conf
RUN mkdir -p /var/log/sng

# Configure Supervisor
COPY supervisord.conf /etc
RUN supervisorctl update
RUN supervisorctl status all

# Update dirs
RUN chown -R sng:sng /home/sng
RUN usermod -a -G sng nginx
RUN chmod 710 /home/sng

# Start services
RUN systemctl enable nginx
RUN service nginx start

# ENTRYPOINT [ "python", "project" ]
