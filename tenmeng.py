# 十盟决赛奖励缓存清除

import redis

redisCon = redis.Redis(host='10.101.166.100', port=19000, db=0)



def ten(allanceId):
    redis_key_single = "champion:award:%d:0:activity:set"%(int(allanceId))
    redisCon.delete(redis_key_single)
    


def main():
    for line in open("十盟.txt"):
        line = line.strip()  #去掉每行头尾空白
        if not len(line) or line.startswith('#'):  #判断是否是空行或注释行
            continue
        tableArgs = line.split(",")
        allanceId = int(tableArgs[0])
        ten(allanceId)



if __name__ == "__main__":
    main()