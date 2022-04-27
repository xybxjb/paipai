import requests


#一键清船
def clear(user_id,ship_id):
    url = "https://ranch.ifreetalk.com/testToolsController/clearShipSail/user_id/"+str(user_id)+"/ship_id/"+str(ship_id)
    print(url)
    rest = requests.get(url, stream=True)
    print(rest.text)
    # s = rest.raw.read()
    # print(s.decode('utf-8'))


def use(user_id_list):
    for ship_id in range(1,6):
        clear(user_id_list,ship_id)



if __name__ == "__main__":
    # 用户列表
    user_id_list = [
        1000002810
    ]
    for user_id in user_id_list:
        use(user_id)

