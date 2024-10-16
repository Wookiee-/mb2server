#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time
import socket
import random
import json
from datetime import datetime, timedelta

class AutoMessagePlugin:
    def __init__(self, config_file):
        with open(config_file, 'rb') as f:
            config_content = f.read().decode('utf-8-sig').strip()
        print("Config file content:")
        print(repr(config_content))
        try:
            config_content = config_content.replace('\r\n', '\n').replace('\r', '\n')
            self.config = json.loads(config_content)
        except ValueError as e:
            print("Error parsing JSON:")
            print(str(e))
            raise
        self.rcon_socket = None
        self.last_message_time = datetime.now()

    def connect_to_server(self):
        self.rcon_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    def send_rcon_command(self, command):
        cmd = b"\xff\xff\xff\xffrcon " + self.config['rcon_password'].encode('utf-8') + b" " + command.encode('utf-8')
        print("Sending RCON command: %r" % cmd)
        self.rcon_socket.sendto(cmd, (self.config['address'], self.config['port']))
        try:
            data, addr = self.rcon_socket.recvfrom(4096)
            print("RCON response: %r" % data)
        except socket.error as e:
            print("Error receiving RCON response: %s" % str(e))

    def send_auto_message(self):
        message = random.choice(self.config['messages'])
        self.send_rcon_command(u"svsay ^7%s" % message)

    def run(self):
        self.connect_to_server()
        print("Auto Message Plugin started at %s" % datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

        while True:
            current_time = datetime.now()
            if current_time - self.last_message_time >= timedelta(minutes=self.config['interval']):
                self.send_auto_message()
                self.last_message_time = current_time
            time.sleep(10)  # Checks every 10 seconds if it's time for a new message

if __name__ == "__main__":
    plugin = AutoMessagePlugin('automessage.cfg')
    try:
        plugin.run()
    except KeyboardInterrupt:
        print("Plugin stopped at %s" % datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
        exit(0)
