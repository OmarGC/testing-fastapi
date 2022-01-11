FROM amazonlinux:2
RUN yum install -y python3.9 python3-pip

WORKDIR /code

# install requirements
COPY ./requirements.txt /code/requirements.txt
RUN pip3 install --no-cache-dir --upgrade -r requirements.txt

COPY ./app /code/app

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]