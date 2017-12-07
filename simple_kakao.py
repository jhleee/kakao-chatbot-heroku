
TEXT = 'text'
BUTTONS = 'buttons'

# Response Objects

# Keyboard
class Buttons(list):
    def add(self, btn):
        self.append(btn)
        return self

class Keyboard(dict):
    def __init__(self, t, buttons=[]):
        assert(t is 'text' or t is 'buttons')
        self['type'] = t
        if buttons :
            self['buttons'] = buttons

# Message
class Message(dict):
    def __init__(self, text=None, photo=None, msg_btn=None):
        assert(text or photo or msg_btn)
        if text :
            self["text"] = text
        if photo :
            self["photo"] = photo
        if msg_btn :
            self["message_button"] = msg_btn

class MessageButton(dict):
    def __init__(self, label, url):
        assert(label and url)
        self['label'] = label
        self['url'] = url


class Photo(dict):
    def __init__(self, url, width, height):
        self['url'] = url
        self['width'] = width
        self['height'] = height

# Response
class Response(dict):
    def __init__(self, msg, keyboard=None):
        self['message'] = msg
        if keyboard :
            self['keyboard'] = keyboard

