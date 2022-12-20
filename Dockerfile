FROM python:3.10
WORKDIR /app
COPY ./requirements.txt requirements.txt
RUN pip install --no-cache-dir --upgrade -r requirements.txt
COPY . .
ENTRYPOINT ["gunicorn", "--bind", "0.0.0.0:80", "app:app"]

