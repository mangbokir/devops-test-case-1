FROM python:3.8-slim
WORKDIR /app
RUN apt-get update && \
    apt-get install -y git

RUN git clone https://github.com/mangbokir/devops-test-case-1.git
RUN cd /app/devops-test-case-1 && \
    pip install pipenv && \
    pipenv install && \
    pip install pre-commit && \
    pre-commit && \
    pip install --upgrade boto3 && \
    python -m pip install boto3-stubs['essential']
CMD ["python", "/app/devops-test-case-1/create_s3_bucket.py"]
