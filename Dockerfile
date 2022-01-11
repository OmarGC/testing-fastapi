# using ubuntu LTS version
FROM ubuntu:20.04

# install python
RUN DEBIAN_FRONTEND=noninteractive apt-get update
RUN DEBIAN_FRONTEND=noninteractive apt-get install python3.9 python3.9-dev python3-pip -y
RUN DEBIAN_FRONTEND=noninteractive apt-get install python3.9-venv -y
RUN DEBIAN_FRONTEND=noninteractive apt-get install build-essential -y
RUN apt-get clean
RUN rm -rf /var/lib/apt/lists/*

# create and activate virtual environment
WORKDIR /fastapi
RUN python3.9 -m venv ./venv
ENV PATH=/fastapi/venv/bin:$PATH

# install requirements
COPY ./requirements.txt .
RUN pip3 install --no-cache-dir --upgrade -r requirements.txt

COPY ./app ./app

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]