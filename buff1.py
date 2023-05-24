import paho.mqtt.client as mqtt
import sqlite3
 
MQTT_HOST = '192.168.1.5'
MQTT_PORT = 1883
MQTT_CLIENT_ID = 'pkd'
TOPIC = 'komdat/fungames/6.1/data'
 
DATABASE_FILE = 'pkd.db'
 
 
def on_connect(mqtt_client, user_data, flags, conn_result):
    mqtt_client.subscribe(TOPIC)
 
 
def on_message(mqtt_client, user_data, message):
    payload = message.payload.decode('utf-8')
 
    db_conn = user_data['db_conn']
    sql = 'INSERT INTO pkd (topik, data) VALUES (?, ?)'
    cursor = db_conn.cursor()
    cursor.execute(sql, (message.topic, payload))
    db_conn.commit()
    cursor.close()
 
 
def main():
    db_conn = sqlite3.connect(DATABASE_FILE)
    sql = """
    CREATE TABLE IF NOT EXISTS pkd (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        topik TEXT NOT NULL,
        data TEXT NOT NULL
    )
    """
    cursor = db_conn.cursor()
    cursor.execute(sql)
    cursor.close()
 
    mqtt_client = mqtt.Client(MQTT_CLIENT_ID)
    mqtt_client.user_data_set({'db_conn': db_conn})
 
    mqtt_client.on_connect = on_connect
    mqtt_client.on_message = on_message
 
    mqtt_client.connect(MQTT_HOST)
    mqtt_client.loop_forever()

main()
