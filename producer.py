from kafka import KafkaProducer
import json


#爵位加声望
producer = KafkaProducer(
    value_serializer=lambda v: json.dumps(v).encode('utf-8'),
    bootstrap_servers="10.101.166.80:9092,10.101.166.81:9092,10.101.166.85:9092".split(","), )

msg = {"desc": "测试加加声望", "rep_leader": "7000000", "rep_no_addition": "66899", "reputation_new": 66899,
       "reputation_old": 65999, "sub_type": 0, "sw64_new": "66899", "sw64_old": "65999", "time": 1641960036, "type": 10,
       "user_id": "9003200100010861"}

producer.send("user-prestige-change-msg-r2p3-v1", msg)
producer.close()