import paho.mqtt.publish as publish
import re
from _lib.logger import setup_logging
import logging
import readline
from _lib.paramters import Parameters, parsing_for_parameters
import argparse

def main():
    setup_logging("logs/", "", add_date_to_name=True)

    print("Mqtt-Publisher")

    # default values
    parameters = Parameters(False, "", "logs/logfile.txt", "192.168.178.100", 1884, "climate/office/+", 0, False)

    # parsing command-line arguments
    parser = argparse.ArgumentParser()
    parser.add_argument("-x", action="store_true", help="activate fileoutput")
    parser.add_argument("-o", help= "name or full path of logfile")
    parser.add_argument("-i", help= "IP of MQTT-broker")
    parser.add_argument("-p", help= "port of MQTT-broker")
    parser.add_argument("-t", help= "topic to subscribe to")
    parser.add_argument("-q", help= "quality of service")
    parser.add_argument("-r", action="store_true", help= "activate retain message")
    args = parser.parse_args()

    parsing_for_parameters(args, parameters)

    print(parameters.__repr__())


    while(True):
        
        try:
            print("Type in the message:")
            payload = input()
            logging.info(f"[message: {payload}]")
            publish.single(parameters.topic, payload, parameters.qos, parameters.retain, parameters.broker_IP, parameters.broker_port)
        except KeyboardInterrupt:
            break

if __name__ == "__main__":
    main()
