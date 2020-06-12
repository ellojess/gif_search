# Gif Search

Tenor gif search web application built using flask as a collaboration project with @Beck-Haywood

### To get up and running:
- If you don't have pipenv, install it with brew install pipenv
- Clone this repository, cd into it, and then run pipenv shell to active the virtual env.
- Run pipenv install to install all the packages that the program requires to run.
- Run the command flask run or python3 app.py to get the server up and running!

### DOCKER!

### Build the image

```bash
docker build -t flask-image .
```

### Build the container

```bash
docker run -p 5000:5000 --rm --name flask-container flask-image
```

### Remove all images with names that contain `flask`

```bash
docker images -a | grep "flask" | awk '{print $3}' | xargs docker rmi
```

### Remove all containers with names that contain `flask`

```bash
docker ps -a | grep "flask" | awk '{print $3}' | xargs docker rmi
```

### See what's running

```bash
docker ps --format '{{.Names}}'
```