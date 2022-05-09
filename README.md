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
<h1>p2 producer 1 topic 2 partisi</h1>
<ul>kita buat producer  dg 1 topic 2 partisi dan 1 broker</ul>
<ul>data/message akan di publish/dikirim ke 2 buah partisi</ul>
<ul>data/message nya dipublish scra random(bisa ke partisi 1 / partisi 2)</ul>

<h1>docker kafka manager</h1>
<ul>docker-compose -f docker-compose.yml up</ul>

<h1>p3 producer mengirim pesan ke 1 buah partisi suatu topic yg ditentukan </h1>
<h3>ERROR</h3>
<ul>producer dpt memilih satu partisi dari suatu topic untuk dirimkan/publish pesannya</ul>
<ul>semua pesan akan dipublish jd single partition (P0)</ul>
<ul>parameter dalam partisi adlh key_bytes (publish psn ke 1 partisi dg key yg ditentukan), all_partition (publish msg ke semua partisi), available_partition (publish psn ke semua partisi yg ada)</ul>

<h1>consumer</h1>
<ul>setiap consumer akan di assign(dibungkus) kedlm 1 grup consumer(consumer dibungkus kedlm 1 grup consumer yg mengonsumsi consumer yg sama)</ul>
<ul>jika tdk ada group_id maka akan menggunakan group id yg di assign scra random (group id berupa key)</ul>
<ul>config untuk consumer umumnya hanya 3 yaitu topic (topic yg ingin diconsume), bootstrap_servers, group_id (grup untuk consumer yg ingin mengonsumsi data)</ul>

<h1>p4 Apa itu consumer group ?</h1>
<ul>adlh logical grouping dari 1/lbh consumer. logical group disini adlh logik untuk setiap consumer yg perlu data yg sama</ul>
<ul>bersifat mandatory, untuk setiap consumer hrs ter-registrasi kedalam consumer group</ul>
<ul>consumer hidup didalam consumer group (consumer group ibaratnya wadah untuk sekumpulan consumer)</ul>

<h1>sumber</h1>
<ul>setting kafka dengan docker https://www.youtube.com/watch?v=FlAlz8guJeM</ul>
<ul>producer consumer code https://www.youtube.com/watch?v=LHNtL4zDBuk</ul>
<ul>p1 producer https://www.youtube.com/watch?v=Q4XA5nUpLeo&list=PLxoOrmZMsAWxXBF8h_TPqYJNsh3x4GyO4&index=7</ul>
<ul>docker kafka manager https://www.youtube.com/watch?v=enqqp2ZIEyE</ul>
<ul>p2 producer 1 topic 2 partisi https://www.youtube.com/watch?v=AvXjRswx9n8&list=PLxoOrmZMsAWxXBF8h_TPqYJNsh3x4GyO4&index=8</ul>
<ul>p3 producer mengirim pesan ke 1 buah partisi suatu topic yg ditentukan https://www.youtube.com/watch?v=kuvTB5SVSJc&list=PLxoOrmZMsAWxXBF8h_TPqYJNsh3x4GyO4&index=9</ul>
<ul>p4 Apa itu consumer group ? https://www.youtube.com/watch?v=gn2zLFRQ8rI&list=PLxoOrmZMsAWxXBF8h_TPqYJNsh3x4GyO4&index=11 </ul>