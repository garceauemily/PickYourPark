import json
from random import randint
from time import sleep

from channels.generic.websocket import WebsocketConsumer

class DashboardConsumer(WebsocketConsumer):
    def connect(self):
        self.accept()

        for i in range(1000):
            self.send(json.dumps({'value': randint(-20,20)}))

