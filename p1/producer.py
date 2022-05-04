import json
from time import time
from kafka import KafkaProducer

from p1.data import create_data
# ubah data jd format json
def json_serializer(data):
    return json.dump(data).encode("utf-8")
# data (value_serialize) akan dibuat dlm data.py (dummy data)
producer = KafkaProducer(bootstrap_servers=['localhost:9092'],
                        value_serializer=json_serializer)
                        
if __name__=="__main__":
    while 1==1:
        data_send = create_data()
        print(data_send)
        # publis/kirim data dg send(), param 1 = nama topic, param 2 = data yg dikirim
        producer.send("data", data_send)
        # data akan dipublish/kirim setiap 4 detik sekali
        time.sleep(4)