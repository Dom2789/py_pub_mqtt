import paho.mqtt.publish as publish
import re
from _lib.logger import setup_logging
import logging
import readline

def main():
    setup_logging("logs/", "", add_date_to_name=True)

    print("Mqtt-Publisher")
    broker_set = False

    while(True):
        if broker_set is False:
            print("Set IP and port for Broker (default 192.168.178.100:1883):")
            while(True):
                broker = input()
                if broker == "":
                    hostname = "192.168.178.100"
                    port = 1883
                    break
                else:
                    if re.match(r"[\d]{1,3}\.[\d]{1,3}\.[\d]{1,3}\.[\d]{1,3}:[\d]{1,4}", broker):
                        hostname, port = broker.split(":")
                        port = int(port)
                        break
                    else:
                        print("Not the right format! See given example.")
                        continue

            print("Set the topic to publish to:")
            while(True):
                topic = input()
                if topic == "":
                    print("Topic must not be empty!")
                    continue
                else:
                    break

            print("Set the quality of service level (default 0):")
            while(True):
                qos = input()
                if qos == "":
                    qos = 0
                    break
                else:
                    if qos in ["0", "1", "2"]:
                        break
                    else:
                        print("Only values 0, 1 and 2 allowed!")
                        continue

            print("Set retain True or False (default False):")
            while(True):
                retain = input()
                retain = retain.lower()
                if retain == "":
                    retain = False
                    break
                else:
                    if retain in ["true", "false", "1", "0"]:
                        if retain == "true" or retain == "1":
                            retain = True
                        else:
                            retain = False
                        break
                    else:
                        print("Only true or false allowed!")
                        continue
            logging.info(f"[broker: {hostname}:{port}][topic: {topic}][qos: {qos}][retain: {retain}]")
            broker_set = True
        try:
            print("Type in the message:")
            payload = input()
            logging.info(f"[message: {payload}]")
            publish.single(topic, payload, int(qos), retain, hostname, port)
        except KeyboardInterrupt:
            break

if __name__ == "__main__":
    main()
