FROM tiangolo/uwsgi-nginx-flask:python3.7

ENV SERVICE video-service

WORKDIR /opt/$SERVICE
ENV PYTHONPATH=/opt/$SERVICE

RUN groupadd -r etl \
    && useradd -r -g etl etl

RUN apt-get update && apt-get install -y \
      cron \
      build-essential \
      software-properties-common \
      python3-software-properties \
      git \
      openssl \
      libssl-dev

# copy everything to working directory
COPY . /opt/$SERVICE/.

RUN python -m pip install --upgrade pip

RUN pip install -r requirements.txt

RUN rm -rf /var/lib/apt/lists/* \
    && apt-get remove -y \
      build-essential \
      git \
    && apt-get autoremove -y \
    && apt-get clean

