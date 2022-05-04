# kafka
<h1>topic</h1>
<ul>docker-compose -f docker-compose.yml up -d</ul>
<ul>docker exec -it kafka /bin/sh</ul>
<!-- cari direktori yg ada kafka-topics.sh untuk membuat topic, di wurstmeister/kafka ada di /opt/kafka_2.13-2.8.1/bin -->
<!-- buat topic dengan partisi & replication(agar tdk ada data yg duplikat jd diset 1)-nya adlh 1 -->
<ul>kafka-topics.sh --create --zookeeper zookeeper:2181 --replication-factor 1 --partitions 1 --topic namatopic</ul>
  <!--lihat all topic dr zookeeper  -->
<ul>kafka-topics.sh --list --zookeeper zookeeper:2181</ul>
<!-- lihat semua informasi dari 1 topic -->
<ul>kafka-topics.sh --describe --zookeeper zookeeper:2181 --topic namatopic</ul>
<!-- hapus 1 topic -->
<ul>kafka-topics.sh --delete --zookeeper zookeeper:2181 --topic namatopic</ul>
<h1>producer consumer di console cli</h1>
<ul>buat dulu topic <b>kafka-topics.sh --create --zookeeper zookeeper:2181 --replication-factor 1 --partitions 1 --topic namatopic</b></ul>
<ul>jlnkan topic yg akan mengirim data dr producer lewat cli <b>kafka-console-producer.sh --broker-list kafka:9092 --topic namatopic</b></ul>
<ul>masukkan data json di cli.  data 1 <br>{'user_id':1, 'recipient_id':2, 'message':'halo'}<br>data 2<br>{'user_id':2, 'recipient_id':1, 'message':'halo juga'}</ul>
<ul>untuk melihat hslnya coba buka 2 terminal dimana 1 mengikuti langkah diatas (as producer)<br><b>kafka-console-producer.sh --broker-list kafka:9092 --topic namatopic</b><br>{'user_id':1, 'recipient_id':2, 'message':'halo'}<br> dan 1 terminal untuk menerima pesan (consumer) dg jlnkan <b>kafka-console-consumer.sh --bootstrap-server kafka:9092 --topic namatopic</ul>
<ul>melihat semua pesan yg telah diterima oleh consumer <br>
<b>kafka-console-consumer.sh --bootstrap-server kafka:9092 --topic namatopic --from-beginning</b></ul>
<h1>dengan code </h1>
<ul>python -m venv venv <br> pip install kafka-python</ul>
<h1>p1 producer</h1>
<ul>kafka-python dan Faker(untuk membuat data dummy)</ul>
<ul>config yg perlu dlm producer yaitu bootstrap_server(alamat server kafka yg dituju, ini berupa ip dan port), topic (as tabel di sql), value_serializer(data yg akan dikirim)</ul>
<ul>skenarionya adlh semua data akan di publish ke 1 partisi</ul>
<ul></ul>
<h1>sumber</h1>
<ul>setting kafka dengan docker https://www.youtube.com/watch?v=FlAlz8guJeM</ul>
<ul>producer consumer code https://www.youtube.com/watch?v=LHNtL4zDBuk</ul>
<ul>p1 producer https://www.youtube.com/watch?v=Q4XA5nUpLeo&list=PLxoOrmZMsAWxXBF8h_TPqYJNsh3x4GyO4&index=7</ul>