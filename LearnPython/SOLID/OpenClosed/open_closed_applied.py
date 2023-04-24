from abc import ABC, abstractmethod

class NotifiableMessage(ABC):
    """Abstract class representing a notifiable message"""
    @abstractmethod
    def get_notification_message(self) -> str:
        """Returns a string containing the notification message"""
        pass

class KakaoTalkMessage(NotifiableMessage):
    """Class representing a KakaoTalk message"""
    notification_message_max_len = 10

    def __init__(self, sent_by, time, content):
        self.sent_by = sent_by
        self.time = time
        self.content = content

    def get_notification_message(self):
        """Returns a string containing the message information and content"""
        message_str = "{}\n{}\n".format(self.time, self.sent_by)
        message_str += self.content if len(self.content) <= KakaoTalkMessage.notification_message_max_len else self.content[:KakaoTalkMessage.notification_message_max_len] + "..."

        return message_str

class FacebookMessage(NotifiableMessage):
    """Class representing a Facebook message"""
    notification_message_max_len = 15

    def __init__(self, sent_by, location, time, content):
        self.sent_by = sent_by
        self.location = location
        self.time = time
        self.content = content

    def get_notification_message(self):
        """Returns a string containing the message information and content"""
        res_str = "{}\n{}\n{}\n".format(self.time, self.sent_by, self.location)
        res_str += self.content if len(self.content) <= FacebookMessage.notification_message_max_len else self.content[:FacebookMessage.notification_message_max_len] + "..."

        return res_str

class TextMessage(NotifiableMessage):
    """Class representing a text message"""
    notification_message_max_len = 12

    def __init__(self, sent_by, time, content):
        self.sent_by = sent_by
        self.time = time
        self.content = content

    def get_notification_message(self):
        """Returns a string containing the message information and content"""
        noti_string = "{}, {}\n".format(self.sent_by, self.time)
        noti_string += self.content if len(self.content) <= TextMessage.notification_message_max_len else self.content[:TextMessage.notification_message_max_len] + "..."

        return noti_string

class MessageNotificationManager:
    """Class representing a message notification manager"""
    def __init__(self):
        self.message_notifications = []

    def add_new_message(self, new_message: NotifiableMessage):
        """Adds a new message"""
        self.message_notifications.append(new_message)

    def display_message_notifications(self):
        """Displays all new messages"""
        print("New messages:")

        for message in self.message_notifications:
            print(message.get_notification_message() + "\n")

# Create a message notification manager instance
message_notification_manager = MessageNotificationManager()

# Create three different messages
kakao_talk_message = KakaoTalkMessage("Godaewi", "July 1, 2019 11:30 PM", "Sorry, I can't go out with you today!")
facebook_message = FacebookMessage("Godaewi", "Seongbuk-gu, Seoul", "July 1, 2019 11:35 PM", "No, I'm coming. Where are you guys hanging out?")
text_message = TextMessage("Lee Young-hoon", "July 2, 2019 12:30 AM", "I'm going out too. I'm leaving now.")

# Add the three messages to the message notification manager instance
message_notification_manager.add_new_message(kakao_talk_message)
message_notification_manager.add
