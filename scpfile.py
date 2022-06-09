import os
import paramiko
import unicodedata
from scp import SCPClient
 
client = paramiko.SSHClient()
client.load_system_host_keys()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
client.connect('服务器IP地址', 服务器SSH端口, '服务器登录账号', '服务器登录密码')
scp = SCPClient(client.get_transport())
 
# 拿到服务器上所有文件夹
stdin, stdout, stderr = client.exec_command(
    'find 服务器上的文件路径 -type l'
)
 
# 遍历远端服务器上的所有文件夹，若在本地服务器不存在，则scp过来
for line in stdout:
    dir = line.strip("\n")
    
    # 文件名截取出来
    file_name = dir.split('/')[第几位]
    if os.path.exists('待拷贝进入的本机路径' + file_name):
        print('sub dir %s  already exists. skip it' % file_name)
    else:
        print('start to copy %s...' % file_name)
        scp.get(os.path.join(dir), '待拷贝进入的本机路径', recursive=True)
 
scp.close()
client.close()

