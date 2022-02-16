# FROM python:3.7-slim
FROM registry.access.redhat.com/ubi8/python-38
COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

COPY . .


# Define environment variable
ENV MODEL_NAME Iris
ENV SERVICE_TYPE MODEL
ENV ENV_MODEL_NAME Iris


CMD exec seldon-core-microservice $MODEL_NAME --service-type $SERVICE_TYPE 
#--http-port 8080
