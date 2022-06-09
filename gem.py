import requests


def addgem(userId,shipId,gemId,posId):
    url = 'http://10.101.167.3:5999/SetGemColor?userId='+userId+'&shipId='+shipId+'&gemId='+gemId+'&pos='+posId
    requests.get(url)




if __name__ == "__main__":
    # 用户列表
    user_id_list = [
        
    ]
    for user_id in user_id_list:
        addgem(user_id)