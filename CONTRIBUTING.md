# CONTRIBUTING

## Initial Dockerfile: When to be run with Flask and we did not have gunicorn installed
```
<!-- FROM python:3.10
EXPOSE 5000
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir --upgrade -r requirements.txt
COPY . .
CMD ["flask", "run", "--host", "0.0.0.0"] -->
```

## How to build the Docker Image
```
docker built -t flask-smorest-api .
__:where image name is: flask-smorest-api__
```
where image name is: flask-smorest-api
## How to run the docker file locally
```
docker run -dp 5000:5000 -w /app -v "$(pwd):/app" flask-smorest-api sh -c "flask run --host 0.0.0.0"
__:where image name is: flask-smorest-api__
```
