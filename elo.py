# -*- coding: utf-8 -*-
def elo(elo_A, elo_B, win_type, win_num):
    '''
    :param elo_A: A家族赛前elo分
    :param elo_B: B家族赛前elo分
    :param win_type: A家族胜利还是失败（1：胜利/平局，0：失败）
    :param win_num: 连胜场次（正数连胜，负数连败）
    :return: A家族结束后的elo分
    '''
    
    elo_X = elo_A - elo_B
    print("分差" + str(elo_X))
    
   
    win = 1 / (1 + 10 ** (-elo_X / 400))
    print("比赛前elo分——>" + str(win))


    
    # 家族赛前分数
    r0 = elo_A
    # 常量
    k = 32
    w = 0
    if win_type == 1:
        print("胜利方")
        w = 1
    elif win_type == 0:
        print("失败方")
        w = 0
    # 连胜大于2场小于6场
    elo_extra = 0
    if 3 <= win_num < 6:
        # elo_extra额外elo分
        elo_extra = (1 - win) * 2 * (win_num + 1)
        print("用户连胜大于2场小于6场额外增加分数——>" + str(elo_extra))
    # 连胜大于6场
    elif win_num >= 6:
        if win_num > 10:
            print("用户连胜大于10场，win_num取10")
            win_num = 10
        elo_extra = (1 - win) * 2 * (2 * (win_num - 2))
        print("用户连胜大于等于6场额外增加分数——>" + str(elo_extra))
    # 连败
    elif win_num < -2:
        # 连败次数
        if abs(win_num) > 17:
            print("用户连败超过17场，win_num取17")
            win_num = 17
        elo_extra = ((0 - win) * 2 * (abs(win_num) - 1))
        print("用户连败超过2场额外增加分数——>" + str(abs(elo_extra)))
    elo_new = r0 + k * (w - win) + elo_extra
    print("A家族赛后elo分——>" + str(round(elo_new)))


if __name__ == '__main__':
    elo(1200, 1200, 1, 0)
    # print("《——连胜方———》")
    # elo(1283, 1111, 0, -3)