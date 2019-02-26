# Create self signed SSL certificate for test purposes
openssl req -new -x509 -nodes -out certificates/test_server.crt -keyout certificates/test_server.key -sha256