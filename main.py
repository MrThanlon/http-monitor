import requests
import subprocess
import config
import signal
import sys
import time


process = []


def exit_handler(sig, frame):
    for p in process:
        p.terminate()
    sys.exit(1)


def check_alive(url):
    response = requests.get(url, headers={
        "User-Agent":
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36 Edg/114.0.1823.82"
    }, timeout=5)
    return response.status_code == 200


if __name__ == '__main__':
    signal.signal(signal.SIGINT, exit_handler)
    signal.signal(signal.SIGTERM, exit_handler)
    # start process
    for c in config.process:
        process.append(subprocess.Popen(c['command'], cwd=c['cwd']))

    while True:
        time.sleep(60 * 5)
        for idx, c in enumerate(config.process):
            if not check_alive(c['url']):
                print(f"{c['command'][0]} down, restarting")
                process[idx].terminate()
                process[idx].wait()
                process[idx] = subprocess.Popen(c['command'], cwd=c['cwd'])
                print(f"{c['command'][0]} restarted")
            else:
                print(f"{c['command']} is alive")
