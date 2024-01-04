import paho.mqtt.client as mqtt
import time

mqttBroker = "192.168.1.10"
client = mqtt.Client()
client.connect(mqttBroker)
while True:
    client.publish("topic/test","publish from raspberry pi")
