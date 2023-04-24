class MessageNotificationManager:
    """Class for managing message notifications"""
    def __init__(self):
        self.message_notifications = []

    def add_new_message(self, new_message):
        """Add a new message"""
        self.message_notifications.append(new_message)

    def display_message_notifications(self):
        """Display all new messages"""
        print("New messages:")

        for message in self.message_notifications:
            print(message.short_message() + "\n")


class KakaoTalkMessage:
    """Class for KakaoTalk messages"""
    notification_message_max_len = 10

    def __init__(self, sent_by, time, content):
        self.sent_by = sent_by
        self.time = time
        self.content = content

    def short_message(self):
        """Return the message information and content"""
        message_str = "{}\n{}\n".format(self.time, self.sent_by)
        message_str += self.content if len(self.content) <= KakaoTalkMessage.notification_message_max_len else self.content[:KakaoTalkMessage.notification_message_max_len] + "..."

        return message_str


class FacebookMessage:
    """Class for Facebook messages"""
    notification_message_max_len = 15

    def __init__(self, sent_by, location, time, content):
        self.sent_by = sent_by
        self.location = location
        self.time = time
        self.content = content

    def notification_display_info(self):
        """Return the message in short form"""
        res_str = "{}\n{}\n{}\n".format(self.time, self.sent_by, self.location)
        res_str += self.content if len(self.content) <= FacebookMessage.notification_message_max_len else self.content[:FacebookMessage.notification_message_max_len] + "..."

        return res_str   

class TextMessage:
    """Class for text messages"""
    notification_message_max_len = 12

    def __init__(self, sent_by, time, content):
        self.sent_by = sent_by
        self.time = time
        self.content = content

    def notification_string(self):
        """Return the message information and content"""
        noti_string = "{}, {}\n".format(self.sent_by, self.time)
        noti_string += self.content if len(self.content) <= TextMessage.notification_message_max_len else self.content[:TextMessage.notification_message_max_len] + "..."
        return noti_string 

# Create an instance of the message notification manager
message_notification_manager = MessageNotificationManager()

# Create 3 messages of different types
kakao_talk_message = KakaoTalkMessage("Godaewi", "July 1, 2019 11:30 PM", "I think I can't go out to play today, sorry!")
facebook_message = FacebookMessage("Godaewi", "Seongbuk-gu, Seoul", "July 1, 2019 11:35 PM", "No, I'm going! Where are you guys hanging out?")
text_message = TextMessage("Lee Young-hoon", "July 2, 2019 12:30 AM", "I'm also going out to play, I'm leaving now.")

# Add the 3 messages to the message notification manager instance
message_notification_manager.add_new_message(kakao_talk_message)
message_notification_manager.add_new_message(facebook_message)
message_notification_manager.add_new_message(text_message)

# Display all the messages in the message notification manager instance
message_notification_manager.display_message_notifications()
