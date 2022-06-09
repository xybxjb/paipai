import redis

redisCon = redis.Redis(host='10.101.166.100', port=19000, db=0)



def allance(allanceId,allanceName):
    redis_key_single = "ppisland:allians:%d:hash"%(int(allanceId))
    redisCon.hset(redis_key_single, 'merge_name',allanceName)



def hgall(allanceId):
    res = redisCon.hgetall('ppisland:allians:%d:hash'%(int(allanceId)))
    print(res.get,end='/t')

def main():
    for line in open("allanceName/test_txt/allanceN.txt"):
        line = line.strip()  #去掉每行头尾空白
        if not len(line) or line.startswith('#'):  #判断是否是空行或注释行
            continue
        tableArgs = line.split(",")
        allanceId = int(tableArgs[0])
        # allanceName = str(tableArgs[1])
        # allance(allanceId,allanceName)
        hgall(allanceId)

if __name__ == "__main__":
    main()
