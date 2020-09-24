import os
import subprocess
import time

def write_curl_format():
    if os.path.isfile('/tmp/curl_format.txt'):
        return

    with open('/tmp/curl_format.txt', 'w') as f:
        f.write(
            "%{time_namelookup}," + 
            "%{time_connect}," + 
            "%{time_appconnect}," + 
            "%{time_pretransfer}," + 
            "%{time_redirect}," + 
            "%{time_starttransfer}," + 
            "%{time_total}\n"
        )


def curl():
    write_curl_format()
    cmd = "curl -w @/tmp/curl_format.txt -o /dev/null -s http://www.google.com/"
    proc = subprocess.Popen(cmd.split(), stdout = subprocess.PIPE)
    output, error = proc.communicate()

    return [float(s) for s in output.decode().split(",")]


while True:
    try:
        ts = curl()
        if ts[-1] > 1:
            print("%d,%3dms" % (time.time(), 1000*ts[-1]))
    except Exception:
        print("%d,ERROR" % time.time())
        pass
    time.sleep(1)
