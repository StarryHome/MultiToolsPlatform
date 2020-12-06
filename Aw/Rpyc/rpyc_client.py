"""
1.Client一定要 close()连接哦！
2.Server中exposed_打头的函数才能被 客户端调用。
所以如果写服务端代码的时候想要让客户端调用 就要加这一个前缀哦
c=rpyc.connect('localhost',12233) #首先要连接服务器
3.client要访问服 务器端代码通过c.root才能访问哦！
c.root.get_time()  调用服务器端方法了！
4.RPYC没有认证机制，任何客 户端都可以直接访问服务器端的暴露的方法了！
"""

import rpyc
conn = rpyc.classic.connect('localhost', 9999)

# 客户端调用模块可以有两种方法，一种是点运算符，一种是中括号；
# 在某些情形下（如selenium的__init__文件中没有子模块webdriver的路径），
# 无法通过点运算符调用，但可以使用[' selenium.webdriver']的形式
path = conn.modules.sys.path
# driver = conn.modules['selenium.webdriver'].Firefox()
time_1 = conn.modules['test_aw'].TestAw()
print(time_1.show())