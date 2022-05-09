from kafka.admin import KafkaAdminClient, NewTopic

# INI UNTUK MEMBUAT TOPIC BARU DENGNAM MENGGUNAKAN KAFKA-PYTHON
admin_client = KafkaAdminClient(
    bootstrap_servers="localhost:9092", 
    client_id='test'
)

topic_list = []
topic_list.append(NewTopic(name="p7", num_partitions=2, replication_factor=1))
admin_client.create_topics(new_topics=topic_list, validate_only=False)