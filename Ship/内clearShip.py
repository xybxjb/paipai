# 内网清船
import requests


#一键清船
def clear(user_id):
    url = "http://10.101.70.8:8080/user/ship/clear_user_ship.html?user="+str(user_id)
    print(url)
    rest = requests.get(url, stream=True)
    print(rest.text)
    # s = rest.raw.read()
    # print(s.decode('utf-8'))


if __name__ == "__main__":
    # 用户列表
    user_id_list = [
9003200100015217
    ]
    for user_id in user_id_list:
        clear(user_id)