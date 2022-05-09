#内网批量重置任务
import requests


# https://task-nurture17.ifreetalk.com/taskWeb/taskTest/branch/world/step/clearDailyTask/u/9003200100011800
def clearDaily(user_id):
    url = "https://task-nurture17.ifreetalk.com/taskWeb/taskTest/branch/world/step/clearDailyTask/u/"+str(user_id)
    rest = requests.get(url, stream=True)
    print(rest.text)



if __name__ == "__main__":
    # 用户列表
    user_id_list = [
        9003200100011800
    ]
    for user_id in user_id_list:
        clearDaily(user_id)
