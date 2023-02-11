#!/bin/sh

# install grafana-server
#- ref: https://grafana.com/docs/grafana/latest/installation/debian/
#+ ref: https://grafana.com/docs/grafana/latest/setup-grafana/installation/debian/

sudo apt-get install -y apt-transport-https
sudo apt-get install -y software-properties-common wget
#- wget -q -O - https://packages.grafana.com/gpg.key | sudo apt-key add -
#+
sudo wget -q -O /usr/share/keyrings/grafana.key https://apt.grafana.com/gpg.key

#- echo "deb https://packages.grafana.com/oss/deb stable main" | sudo tee -a /etc/apt/sources.list.d/grafana.list
#+
echo "deb [signed-by=/usr/share/keyrings/grafana.key] https://apt.grafana.com stable main" | sudo tee -a /etc/apt/sources.list.d/grafana.list

sudo apt-get update
sudo apt-get install grafana

sudo systemctl daemon-reload
sudo systemctl enable grafana-server
sudo systemctl start grafana-server
#service grafana-server status
