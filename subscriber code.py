import paho.mqtt.client as mqtt
import RPi.GPIO as GPIO
import time
LEDin=29
GPIO.setmode(GPIO.BOARD)
GPIO.setup(LEDin,GPIO.OUT)


def on_message(client,userdata,message):
    if(str(message.payload.decode("utf-8"))=='1'):
        GPIO.output(LEDin,GPIO.HIGH)
        print("Received message:",str(message.payload.decode("utf-8")))
        #print("Received message 1")
        time.sleep(2)
    elif(str(message.payload.decode("utf-8"))=='0'):
        GPIO.output(LEDin,GPIO.LOW)
        print("Received message:",str(message.payload.decode("utf-8")))
        time.sleep(2)
mqttBroker="192.168.252.136"
client=mqtt.Client("subscriberclient")
client.username_pw_set("malsha","456")
client.connect(mqttBroker)
client.subscribe("topic/led")

client.on_message=on_message
client.loop_forever()

