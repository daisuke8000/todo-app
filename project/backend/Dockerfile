#official base-image python
FROM python:3.9.6-slim-buster

#working directroy
WORKDIR /usr/src/app/

#environment variables
ENV PYTHONDONTWRITERBYTECODE 1
ENV PYTHONUNBUFFERED 1

#install system depedencies
RUN apt-get update \
  && apt-get -y install netcat gcc postgresql \
  && apt-get clean

#install python depedencies
RUN pip install --upgrade pip
COPY ./requirements.txt .
COPY ./requirements-dev.txt .
RUN pip install -r requirements-dev.txt

#add app
COPY . .

##add entrypoint.sh
#COPY ./entrypoint.sh .
#RUN chmod +x /usr/src/app/entrypoint.sh
#
##entrypoint.sh
#ENTRYPOINT ["/usr/src/app/entrypoint.sh"]
