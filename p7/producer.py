import json
import time
from kafka import KafkaProducer

from data import create_data



# from data import create_data
# ubah data jd format json
def json_serializer(data):
    return json.dumps(data).encode("utf-8")

# data (value_serialize) akan dibuat dlm data.py (dummy data). bootstrap_server disini adlh server kafka
producer = KafkaProducer(bootstrap_servers=['localhost:9092'],
                        value_serializer=json_serializer)
                        
if __name__=="__main__":
    while 1==1:
        data_send = create_data()
        print(data_send)
        # publis/kirim data dg send(), param 1 = nama topic, param 2 = data yg dikirim
        producer.send("p7", data_send)
        # data akan dipublish/kirim setiap 4 detik sekali
        time.sleep(4)