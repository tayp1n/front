## Installation

Clone this repository, after that run this command to build containers.
```bash
docker build -t service . 
```

## Run
Run this command in project folder to start containers.
```bash
docker run -p 9090:9090 -e SETTINGS_MODULE=ci service

docker-compose up --build
```

```url
http://0.0.0.0:9090/
```