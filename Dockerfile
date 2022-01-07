FROM tiangolo/uvicorn-gunicorn-fastapi:python3.8-slim

EXPOSE 80

EXPOSE 443

COPY ./requirements.txt /app/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt

COPY ./app /app/app/
# COPY ./.env.dev /app/.env