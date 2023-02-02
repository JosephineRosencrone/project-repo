FROM python:3.7-alpine
COPY . /app
WORKDIR /app
RUN pip install .
CMD ["master_thesis_python_repo"]
