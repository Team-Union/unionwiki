## Installation
```
docker pull endwiki/stable
```

## Start
```
docker run -p 3000:3000 -v data:/app/data --name endwiki endwiki/stable
docker run -p <host-port>:3000 -v <host-data_directory>:/app/data --name <docker-containername> endwiki/stable
```