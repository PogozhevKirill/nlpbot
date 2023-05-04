from typing import List, Optional


class KeyboardButton:
    def __init__(self,
                 text: str):
        self.text: str = text

    def __repr__(self):
        rep = 'KeyboardButton(text="{}")'.format(self.text)
        return rep

    def to_json(self):
        js = {'text': self.text}
        return js


class InlineKeyboardButton:
    def __init__(self,
                 text: str,
                 callback_data: str):
        self.text: str = text
        self.callback_data: str = callback_data

    def __repr__(self):
        rep = 'KeyboardButton(text="{}",callback_data="{}")'.format(self.text, self.callback_data)
        return rep

    def to_json(self) -> dict:
        js = {'text': self.text,
              'callback_data': self.callback_data}
        return js


class ReplyKeyboardMarkup:
    def __init__(self,
                 keyboard: Optional[List[KeyboardButton]] = None,
                 n_cols: Optional[int] = None,
                 is_persistent: bool = False,
                 resize_keyboard: bool = True,
                 one_time_keyboard: bool = False,
                 input_field_placeholder: str = ''):
        if keyboard is None:
            self.keyboard = []
        else:
            self.keyboard: List[KeyboardButton] = keyboard
        if n_cols is not None and n_cols > 0:
            self.n_cols = n_cols
        else:
            self.n_cols = 2
        self.is_persistent = is_persistent
        self.resize_keyboard = resize_keyboard
        self.one_time_keyboard = one_time_keyboard
        self.input_field_placeholder = input_field_placeholder

    def __repr__(self):
        rep = "ReplyKeyboardMarkup(n_buttons={},n_cols={},is_persistent={},input_field_placeholder='{}')".format(
            len(self.keyboard),
            self.n_cols,
            self.is_persistent,
            self.input_field_placeholder
        )
        return rep

    def to_json(self) -> dict:
        js = {'is_persistent': self.is_persistent,
              'resize_keyboard': self.resize_keyboard,
              'one_time_keyboard': self.one_time_keyboard,
              'input_field_placeholder': self.input_field_placeholder}
        js_list = [x.to_json() for x in self.keyboard]
        js['keyboard'] = [js_list[i:i + self.n_cols] for i in range(0, len(js_list), self.n_cols)]
        return js


class InlineKeyboardMarkup:
    def __init__(self,
                 inline_keyboard: Optional[List[InlineKeyboardButton]] = None,
                 n_cols: Optional[int] = None):
        if inline_keyboard is None:
            self.inline_keyboard = []
        else:
            self.inline_keyboard: List[InlineKeyboardButton] = inline_keyboard
        if n_cols is not None and n_cols > 0:
            self.n_cols = n_cols
        else:
            self.n_cols = 2

    def __repr__(self):
        rep = "InlineKeyboardMarkup(n_buttons={},n_cols={})".format(len(self.inline_keyboard), self.n_cols)
        return rep

    def to_json(self) -> list:
        js_list = [x.to_json() for x in self.inline_keyboard]
        js = [js_list[i:i + self.n_cols] for i in range(0, len(js_list), self.n_cols)]
        return js
