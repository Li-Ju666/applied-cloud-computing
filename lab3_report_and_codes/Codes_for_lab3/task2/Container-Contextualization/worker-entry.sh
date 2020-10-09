sudo docker build --tag worker:latest .
sudo docker run -d --network host -e RMQIP="192.168.2.134" worker sh -c "celery -A project worker & python3 -m project.run & sleep infinity"
