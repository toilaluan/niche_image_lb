sudo docker network create --driver=bridge nichenet 
sudo docker rm haproxy
sudo docker run \
   --name haproxy \
   --net nichenet \
   -v ./haproxy.cfg:/usr/local/etc/haproxy/haproxy.cfg \
   -p 15000:15000 \
   -p 15001:15001 \
   -p 15010:15010 \
   -p 15011:15011 \
   -p 15012:15012 \
   haproxy
