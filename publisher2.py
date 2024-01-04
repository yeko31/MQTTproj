import paho.mqtt.client as mqtt
import time
import RPi.GPIO as GPIO
LED = 5


mqttBroker = "192.168.252.136"
client = mqtt.Client("publisherclient")
client.username_pw_set("kevini","123")
client.connect(mqttBroker)

GPIO.setmode(GPIO.BCM)
GPIO.setup(LED,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)
while True:
    ledvalue = GPIO.input(LED)
    if(ledvalue==1):
        client.publish("topic/led",1)
        print("just published" + str(1))
        time.sleep(2)
    else:
        client.publish("topic/led",0)
        print("Just Published"+str(0))
        time.sleep(2)
    client.publish("topic/test","publish from raspberry pi")

