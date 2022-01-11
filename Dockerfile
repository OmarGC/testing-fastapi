# using ubuntu LTS version
FROM ubuntu:20.04

# install python
RUN apt-get update
RUN apt-get install python3 -y
RUN apt-get install python3-pip -y

WORKDIR /fastapi

# install requirements
COPY ./requirements.txt /fastapi/requirements.txt
RUN pip3 install --no-cache-dir --upgrade -r requirements.txt

COPY ./app /fastapi/app

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]