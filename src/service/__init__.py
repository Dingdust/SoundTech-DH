import os
from loguru import logger
from threading import Thread

def frpc_server():
    logger.info("启动 FRP 内网穿透服务")
    os.popen(r"ssl_certs\frpc.exe -c ssl_certs\frpc.toml")
    
thread = Thread(target=frpc_server, daemon=True)
thread.start()
