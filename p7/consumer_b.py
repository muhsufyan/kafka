import json
from kafka import KafkaConsumer


if __name__=="__main__":
    consumer = KafkaConsumer(
        # nama topic
        "p7",
        bootstrap_servers="localhost:9092",
        # offset yg diconsumer adlh offset yg terbaru
        auto_offset_reset="earliest",
        # group id nya adlh consumer-group-A
        group_id="consumer-group-B"
    )
    print("mulai consuming")
    for msg in consumer:
        print("data dari topic data : {} ".format(json.loads(msg.value)))