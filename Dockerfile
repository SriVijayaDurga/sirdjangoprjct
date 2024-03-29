FROM hub.livnsense.com/python3.6.7 
ADD . /usr/src/app
#set directoty where CMD will execute
WORKDIR /usr/src/app
# set environment varibles
ENV PYTHONDONTWRITEBYTECODE 1 
ENV PYTHONUNBUFFERED 1 
COPY requirements.txt ./
# Get pip to download and install requirements:
RUN pip install --no-cache-dir -r requirements.txt
# Expose ports
EXPOSE 8000
# default command to execute
CMD python3 manage.py runserver 0:8000
