docker build -t service . 

docker run -p 9090:9090 -e SETTINGS_MODULE=ci service
