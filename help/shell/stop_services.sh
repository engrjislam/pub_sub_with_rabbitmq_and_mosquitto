#!/bin/sh


# NOTE:
# -----
# docker-compose.yml will use influxdb, grafana & 
# mosquitto servers with their default ports. So, 
# stop all the services to avoid port conflictions
# with either service or systemctl command.


# with service command
# --------------------
# service status
#service influxdb status
#service grafana-server status
#service mosquitto status

# service stop
ehco "Stopping influxdb, grafana-server; and mosquitto services ..."
service influxdb stop
service grafana-server stop
service mosquitto stop

# service start
#service influxdb start
#service grafana-server start
#service mosquitto start

# service restart
#service influxdb restart
#service grafana-server restart
#service mosquitto restart


# with systemctl command
# --------------------
# service status
#systemctl status influxdb
#systemctl status grafana-server
#systemctl status mosquitto

# service stop
#systemctl stop influxdb
#systemctl stop grafana-server
#systemctl stop mosquitto

# service start
#systemctl start influxdb
#systemctl start grafana-server
#systemctl start mosquitto

# service restart
#systemctl restart influxdb
#systemctl restart grafana-server
#systemctl restart mosquitto
