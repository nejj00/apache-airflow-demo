FROM apache/airflow:2.10.4
COPY requirements.txt /requirements.txt

RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r /requirements.txt

# We tell docker to build an image using the docker file
# docker build . --tag extending_airflow:latest