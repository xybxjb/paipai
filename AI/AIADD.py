import redis

redisCon = redis.Redis(host='10.101.166.100', port=19000, db=0)


def allance1(allanceId, a, user_id):
    redis_key_single = "eal:ai:lib:league:%d:zset " % (int(allanceId))
    mapping = {a: user_id}
    redisCon.zadd(redis_key_single,mapping)


def main():
    for line in open("/Users/xiaoyu/Code/paipai/AI/ai.txt"):
        line = line.strip()  # 去掉每行头尾空白
        if not len(line) or line.startswith('#'):  # 判断是否是空行或注释行
            continue
        tableArgs = line.split(",")
        allanceId = int(tableArgs[0])
        a = int(tableArgs[1])
        user_id = int(tableArgs[2])
        allance1(allanceId, a, user_id)


if __name__ == "__main__":
    main()
