# Import plugins from ABC
from abc import ABC, abstractmethod

# Create Class For notification
class Notification(ABC):
    @abstractmethod
    def send(self):
        pass

# Create Subclasses that depends to Nofication
class EmailNotification(Notification):
    def send(self):
        return "Sending Email Notification"

class SMSNotification(Notification):
    def send(self):
        return "Sending SMS Notification"

class PushNotification(Notification):
    def send(self):
        return "Sending Push Notification"

class NotificationFactory:
    @staticmethod
    def create_notification(type_): # Create method for user inputs
        if type_.lower() == "email":
            return EmailNotification()
        elif type_.lower() == "sms":
            return SMSNotification()
        elif type_.lower() == "push":
            return PushNotification()
        else:
            raise ValueError("Unsupported notification type")

# Demo
notif_type = input("Enter notification type (Email, SMS, or Push): ")
notification = NotificationFactory.create_notification(notif_type)
print(notification.send()) # Display send notification
