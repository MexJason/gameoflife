from kivy.uix.relativelayout import RelativeLayout


def keyboard_closed(self):
    self._keyboard.unbind(on_key_down=self.on_keyboard_down)
    self._keyboard.unbind(on_key_up=self.on_keyboard_up)
    self._keyboard = None

def on_keyboard_down(self, keyboard, keycode, text, modifiers):
    if keycode[1] == 'left':
        self.current_speed_x = self.SPEED_X
    elif keycode[1] == 'right':
        self.current_speed_x = - self.SPEED_X
    return True  # return True to say I have managed this key press for these functions


def on_keyboard_up(self, keyboard, keycode):
    self.current_speed_x = 0
    return True  # return True to say I have managed this key press for these functions


def on_touch_down(self, touch):
    if not self.state_game_over and self.state_game_start:
        if touch.x < self.width / 2:
            # print("left")
            self.current_speed_x = self.SPEED_X
        else:
            # print("right")
            self.current_speed_x = - self.SPEED_X
    #return super(MainWidget, self).on_touch_down(touch)
    return super(RelativeLayout, self).on_touch_down(touch) #this solves the problem of having to import MainWidget. It would cause issues so RelativeLayout Used instead



def on_touch_up(self, touch):
    # print("Up")
    self.current_speed_x = 0  # stop movement when you release button