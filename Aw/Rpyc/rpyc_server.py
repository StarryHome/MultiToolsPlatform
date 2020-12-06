# coding:utf-8
import time
from rpyc.core.service import SlaveService
from rpyc.utils.server import ThreadedServer

# SlaveService是一种允许客户端任意的调用服务器端的模块和代码的服务
server = ThreadedServer(SlaveService, auto_register=False, hostname='localhost', port=9999)
server.start()

