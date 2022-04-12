# -*- coding: utf-8 -*-

"""
    @Author hujiahong
    @Date 2020/12/2 10:11 下午
    @proto
    @FileName : Ship3dCase.py
    功能描述：船相关的测测试用例
"""
import requests


def AddCommonItems(userID, goods_id, goods_count):
    # gm_ip =get_gm_ip(userID)
    gm_ip ="http://10.102.21.42:5999"
    goods_id = goods_id
    url = gm_ip + "/addItem?userId=" + str(userID) + "&id=" + str(
        goods_id) + "&count=" + str(
        goods_count)
    print(url)
    r = requests.get(url, stream=True)
    s = r.raw.read()
    print(s.decode('utf-8'))

# 设置神器等级
def weaponsLv(userId, lv=0, weaponsId=None, is_add_weapons=True):
    gm_ship_ip = "http://10.101.167.3:5999"
    if weaponsId == None:
        weapons_id_list = [
            36150101, 36150102, 36150103, 36150104, 36150105, 36150106, 36150107, 36150108,
            36150201, 36150202, 36150203, 36150204, 36150205, 36150206, 36150207, 36150208,
            36150301, 36150302, 36150303, 36150304, 36150305, 36150306, 36150307, 36150308,
            36150601, 36150602, 36150603, 36150604, 36150605, 36150606, 36150607, 36150608,
            36150901, 36150902, 36150903, 36150904, 36150905, 36150906, 36150907, 36150908
        ]
    else:
        # weapons_id_list = [weaponsId]
        weapons_id_list = weaponsId

    for weaponsId in weapons_id_list:
        if is_add_weapons:
            AddCommonItems(userId, weaponsId, 1)
        if lv == 0:
            continue
        url = gm_ship_ip + "/weaponsLv?userId=" + str(userId) + "&weaponsId=" + str(
            weaponsId) + "&lv=" + str(lv)
        print(url)
        r = requests.get(url, stream=True)
        s = r.raw.read()
        result = s.decode('utf-8')
        # print(result)


def make_big_ship(user_id_list):
    for user_id  in user_id_list:
        # ## 设置神器等级
        weaponsLv(user_id,11)



if __name__ == '__main__':
    user_id_list = [
        9003200100007420
    ]
    for user_id in user_id_list:
        make_big_ship(user_id_list)
