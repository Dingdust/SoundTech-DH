import os
from threading import Thread

def frpc_server():
    os.popen(r"ssl_certs\frpc.exe -c ssl_certs\frpc.toml")
    
thread = Thread(target=frpc_server)
thread.start()
