class Message:
    def __init__(self, message_body):
        self.__message_body = message_body

    def get_message(self):
      return self.__message_body

    def set_message(self, message_body):
      self.__message_body = message_body


class Messanger:
  def send(self, message: Message):
    print('Message sent:', message.get_message())
    #do something

  def receive(self):
    print('Message received')
    # do something
    return Message('message body')

messanger = Messanger()
message = Message('message body')
messanger.send(message)