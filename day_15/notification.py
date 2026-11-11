from abc import ABC, abstractmethod


class Notification(ABC) :
    @abstractmethod
    def send(self,message):
        print(f"Sending Message : {message}")

class EmailNotification(Notification):

    def send(self, message):
        print(f"Sending EMAIl : {message}")

    def send_cc(self,message, sender):
        print(f"Sending Carbon Copy to {sender} : {message}")

class SMSNotification(Notification):
    def send(self, message):
        print(f"Sending SMS : {message}")

class PushNotification(Notification):
    def send(self, message):
        print(f"Sending Push Notification : {message}")