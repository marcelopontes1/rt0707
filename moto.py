import paho.mqtt.client as mqtt
import random, json
from random import randrange, uniform
import time


def connect_broker(ip, client_name):
    mqttBroker = ip
    client = mqtt.Client(client_name)
    client.connect(mqttBroker)
    return client


def message(stationID, stationType, vitesse, Heading, position_x, position_y, cause_code):
    msg = {"CAM" :
          {"stationId": stationID,
           "stationType": stationType,
           "vitesse": vitesse,
           "Heading": Heading,
           "positionGPS": [{
                            "x" : position_x,
                            "y" : position_y
                        }]
        },
           "DENM" :
           {"stationId": stationID,
            "stationType": stationType,
            "cause_code": cause_code,
            "positionGPS": [{
                             "x" : position_x,
                             "y" : position_y
                         }]
        }
}

    return json.dumps(msg)

while True:
    #print("Entrou no while")
    client = connect_broker('10.22.135.24', "MOTO")
    cam = message(2, random.choice([5, 10, 15]), random.randint(0,130), random.randint(-360,360), 45, 25, random.choice([3, 4, 5, 6, 7]))
    client.publish("MESSAGES", cam)
    print("Just published " + str(cam) + " to Topic MESSAGES")
    time.sleep(1)
    