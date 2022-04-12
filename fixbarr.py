import sys
import importlib
import time
import redis
import struct
import json
import os
import logging
from kafka import KafkaProducer
producer = KafkaProducer(bootstrap_servers=['10.101.166.80:9092','10.101.166.81:9092','10.101.166.85:9092'])   #1000370
chg_producer = KafkaProducer(bootstrap_servers=['10.101.166.80:9092','10.101.166.81:9092','10.101.166.85:9092'])  #1000485
channel_producer =  KafkaProducer(bootstrap_servers=['10.101.166.80:9092','10.101.166.81:9092','10.101.166.85:9092']) #1000373
task_producer =  KafkaProducer(bootstrap_servers=['10.101.166.23:9091','10.101.166.23:9092','10.101.166.23:9093']) #1000044
from logging.handlers import TimedRotatingFileHandler
sys.path.append("..")
logging.basicConfig(
   filename='fixbarrier.log',
   level=logging.WARNING,
   format='[%(asctime)s]%(levelname)s:%(message)s')
#10.101.171.239 65005
redisCon = redis.Redis(host='10.101.166.100', port=19000, db=0)
DEF_LOG_PATH = os.path.dirname(os.path.abspath(__file__)) + '/log'
DEF_LOG_FILENAME_PREFIX = __file__.split('.')[0].split('/')[-1]



#远征关卡通过
def main():
    for line in open("barrier.txt"):# barrier.txt  格式是用户id,第几章,第几关
        line = line.strip()  #去掉每行头尾空白
        if not len(line) or line.startswith('#'):  #判断是否是空行或注释行
            continue
        tableArgs = line.split(",")
        userId = int(tableArgs[0])
        big_bar_id = int(tableArgs[1])
        small_bar_id = int(tableArgs[2])
        logging.warning(' userId =%d  big_bar_id=%d small_bar_id=%d' % (userId, big_bar_id, small_bar_id) )
        #continue
        redis_set_value = "11:2271:1331"
        max_small_index = 21
        for bar_index in range(1,big_bar_id+1):
            logging.warning('bar_index=%d' % (bar_index) )
            if bar_index > 1:
                redis_set_value = "11:2271:3991"
            if bar_index == big_bar_id:
                max_small_index = min(small_bar_id + 1,21)
            for smal_index in range(1,max_small_index):
                logging.warning('smal_index=%d' % (smal_index) )
                redis_key_single = "u:%d:1:%d:small:bar:condition"%(int(userId), int(bar_index))
                filed = bar_index*100000 + smal_index*100 + 1
                redis_value = redisCon.hget(redis_key_single, str(filed))
                chg_value = False
                if redis_value == None:
                    chg_value = True
                else:
                    value_list = str(redis_value.decode("utf-8")).split(":")
                    logging.warning('con1=%d con2=%d  con3=%d' % (int(value_list[0]),int(value_list[1]),int(value_list[2])) )
                    con1 = int(value_list[0]) % 10
                    con2 = int(value_list[1]) % 10
                    con3 = int(value_list[2]) % 10
                    logging.warning('con1=%d con2=%d  con3=%d' % (con1,con2,con3) )
                    if (con1 == 0) and (con2 == 0)  and (con3 == 0):
                        chg_value = True
                if chg_value == True:
                    redisCon.hset(redis_key_single, str(filed), redis_set_value)
                    logging.warning('hset key =%s  filed=%s value=%s' % (redis_key_single, str(filed), redis_set_value) )
                    kafka_data = {}
                    kafka_data["user_id"] = userId
                    kafka_data["big_bar_id"] = bar_index
                    kafka_data["barrier_type"] = 1
                    kafka_data["small_bar_id"] = filed
                    kafka_data["condition"] = redis_set_value
                    kafka_data["opt_type"] = 3
                    kafka_data["data_name"] = "pirate_barrier_condition_status"
                    kafka_data["data_type"] = 38
                    kafka_data["update_time"] = int(time.time())
                    data2 = json.dumps(kafka_data)
                    logging.warning('data2=%s' % (data2) )
                    producer.send('pirate-barrier-condition-status', bytes(data2.encode('utf-8')))
                    kafka_chg_data = {}
                    kafka_chg_data["user_id"] = userId
                    kafka_chg_data["big_bar_id"] = bar_index
                    kafka_chg_data["barrier_type"] = 1
                    kafka_chg_data["small_bar_id"] = filed
                    kafka_chg_data["condition"] = redis_set_value
                    kafka_chg_data["op_type"] = 0
                    kafka_chg_data["update_time"] = int(time.time())
                    data3 = json.dumps(kafka_chg_data)
                    logging.warning('data3=%s' % (data3) )
                    chg_producer.send('topic-barrier-condition-chg', bytes(data3.encode('utf-8')))
                    channel_record = {}
                    channel_record["user_id"] = userId
                    channel_record["small_bar_id"] = filed
                    channel_record["barrier_type"] = 1
                    channel_record["a_ward"] = "脚本封印,无奖励"
                    channel_record["battle_info"] = "无战斗"
                    channel_record["star"] = 1
                    channel_record["create_time"] = int(time.time())
                    data4 = json.dumps(channel_record)
                    logging.warning('data4=%s' % (data4) )
                    channel_producer.send('pirate-barrier-battle-record', bytes(data4.encode('utf-8')))
                    task_record = {}
                    task_record["user_id"] = userId
                    task_record["condition_id"] = 3001
                    task_record["item_id"] = bar_index
                    task_record["item_value"] = smal_index
                    task_record["time"] =  int(time.time())
                    task_record["result"] = 1
                    data5 = json.dumps(task_record)
                    logging.warning('data5=%s' % (data5) )
                    task_producer.send('ppworld-task-points-r3p16-v1', bytes(data5.encode('utf-8')))

    producer.close()
    chg_producer.close()
    channel_producer.close()
    task_producer.close()
    return



if __name__ == '__main__':
    main()
