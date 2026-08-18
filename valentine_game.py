import os
import sys
import kivy
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.image import Image
from kivy.clock import Clock
from kivy.core.window import Window
from kivy.core.audio import SoundLoader
from kivy.core.text import LabelBase
from kivy.graphics import Rectangle, Color, Ellipse, RoundedRectangle
from kivy.properties import BooleanProperty
import random
import math
from tkinter import filedialog
import tkinter as tk
import shutil

def resource_path(relative_path):
    """Get absolute path to resource, works for dev and for PyInstaller"""
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

# Register Gothess font
LabelBase.register(name='Gothess', fn_regular=resource_path('fonts/Gothess.ttf'))

Window.size = (1000, 700)

class ValentineQuestion(FloatLayout):
    def __init__(self, app_instance, **kwargs):
        super().__init__(**kwargs)
        self.app_instance = app_instance

        # Load music
        self.music = SoundLoader.load(resource_path('music/1st screen whimsical.mp3'))
        if self.music:
            self.music.loop = True
            self.music.volume = 1.0
            self.music.play()

        # Background image
        with self.canvas.before:
            self.bg = Rectangle(source=resource_path("assets/valentine_bg.png"),
                                size=Window.size,
                                pos=(0, 0))
        self.bind(size=self._update_rect, pos=self._update_rect)

        # Dark backdrop behind title
        with self.canvas.before:
            Color(0, 0, 0, 0.5)
            self.title_bg = RoundedRectangle(
                pos=(50, Window.height * 0.55),
                size=(900, 140),
                radius=[20]
            )

        # Question label
        self.question = Label(
            text="Will you be my valentine?",
            font_name='Gothess',
            font_size='56sp',
            color=(1, 1, 1, 1),
            size_hint=(None, None),
            size=(900, 120),
            halign='center',
            valign='middle'
        )
        self.question.bind(size=self.question.setter('text_size'))
        self.question.pos = (50, Window.height * 0.58)
        self.add_widget(self.question)

        # YES button background - 80% TRANSPARENT GREY/BLACK
        with self.canvas:
            Color(0, 0, 0, 0.8)
            self.yes_bg_rect = RoundedRectangle(pos=(230, 240), size=(300, 90), radius=[20])

        # YES button
        yes_btn = Button(
            text="Yes, Fly",
            font_name='Gothess',
            size_hint=(None, None),
            size=(300, 90),
            pos=(230, 240),
            background_normal='',
            background_color=(0, 0, 0, 0),
            color=(1, 1, 1, 1),
            font_size='40sp'
        )
        yes_btn.bind(on_press=self.on_yes)
        self.add_widget(yes_btn)

        # NO button background - 80% TRANSPARENT GREY/BLACK
        with self.canvas:
            Color(0, 0, 0, 0.8)
            self.no_bg_rect = RoundedRectangle(pos=(550, 240), size=(280, 90), radius=[20])

        # NO button
        self.no_btn = Button(
            text="Alas, no",
            font_name='Gothess',
            size_hint=(None, None),
            size=(280, 90),
            pos=(550, 240),
            background_normal='',
            background_color=(0, 0, 0, 0),
            color=(1, 1, 1, 1),
            font_size='40sp'
        )
        self.no_btn.bind(on_press=self.on_no)
        self.no_btn.bind(pos=self.update_no_bg)
        self.add_widget(self.no_btn)

        Clock.schedule_interval(self.check_mouse, 0.05)

    def _update_rect(self, instance, value):
        self.bg.pos = instance.pos
        self.bg.size = instance.size

    def update_no_bg(self, instance, value):
        """Update the background rectangle when the NO button moves"""
        self.no_bg_rect.pos = self.no_btn.pos

    def check_mouse(self, dt):
        mouse_pos = Window.mouse_pos
        btn_x = self.no_btn.x
        btn_y = self.no_btn.y
        btn_center_x = btn_x + self.no_btn.width / 2
        btn_center_y = btn_y + self.no_btn.height / 2
        distance = ((mouse_pos[0] - btn_center_x)**2 + (mouse_pos[1] - btn_center_y)**2)**0.5
        if distance < 140:
            self.move_no_button()

    def move_no_button(self):
        new_x = random.randint(100, Window.width - 380)
        new_y = random.randint(100, Window.height - 190)
        self.no_btn.pos = (new_x, new_y)

    def on_no(self, instance):
        self.move_no_button()

    def on_yes(self, instance):
        Clock.unschedule(self.check_mouse)
        self.fade_out_music()
        Clock.schedule_once(lambda dt: self.app_instance.show_game(), 0.3)

    def fade_out_music(self):
        if self.music and self.music.state == 'play':
            def fade_step(dt):
                if self.music.volume > 0.05:
                    self.music.volume -= 0.1
                    Clock.schedule_once(fade_step, 0.05)
                else:
                    self.music.stop()
            fade_step(0)


class Critter(Image):
    is_caught = BooleanProperty(False)

    def __init__(self, critter_type, is_bad=False, **kwargs):
        if is_bad:
            bad_items = ["badteddy", "thornyrose", "wiltedflower"]
            source_name = bad_items[critter_type]
            super().__init__(
                source=resource_path(f"assets/{source_name}.png"),
                size_hint=(None, None),
                size=(80, 80),
                allow_stretch=True,
                keep_ratio=True,
                **kwargs
            )
        else:
            super().__init__(
                source=resource_path(f"assets/critter{critter_type + 1}.png"),
                size_hint=(None, None),
                size=(80, 80),
                allow_stretch=True,
                keep_ratio=True,
                **kwargs
            )

        self.velocity = random.randint(160, 230)
        self.critter_type = critter_type
        self.is_bad = is_bad
        self.floaty = random.random() < 0.5
        self.bob_offset = 0
        self.bob_speed = random.uniform(3, 5)
        self.side_amp = random.randint(8, 18)
        self.base_x = random.randint(40, Window.width - 100)
        self.x = self.base_x
        self.y = Window.height + 50

        with self.canvas.before:
            Color(0, 0, 0, 0.3)
            self.shadow = Ellipse(
                pos=(self.x + 10, self.y - 5),
                size=(60, 15)
            )

    def move(self, dt):
        if self.is_caught:
            return

        self.y -= self.velocity * dt

        if self.floaty:
            self.bob_offset += self.bob_speed * dt
            bob_y = math.sin(self.bob_offset) * 3
            side_x = math.sin(self.bob_offset * 0.7) * self.side_amp
            self.x = self.base_x + side_x
        else:
            bob_y = 0

        self.shadow.pos = (self.x + 10, self.y - 5 + bob_y)
        self.pos = (self.x, self.y + bob_y)


class Player(Image):
    def __init__(self, **kwargs):
        super().__init__(
            source=resource_path("assets/girl.png"),
            size_hint=(None, None),
            size=(120, 140),
            allow_stretch=True,
            keep_ratio=True,
            **kwargs
        )

        self.x = Window.width / 2 - 60
        self.y = 60

        with self.canvas.before:
            Color(0, 0, 0, 0.25)
            self.shadow = Ellipse(
                pos=(self.x + 15, self.y - 8),
                size=(90, 20)
            )

        self.bind(pos=self.update_shadow)

    def update_shadow(self, *args):
        self.shadow.pos = (self.x + 15, self.y - 8)


class GameScreen(FloatLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.score = 0
        self.lives = 3
        self.game_active = True
        self.current_good_critter = 0

        self.good_catch_sound = SoundLoader.load(resource_path('sounds/good_catch.mp3'))
        self.bad_catch_sound = SoundLoader.load(resource_path('sounds/bad_catch.mp3'))
        self.missed_sound = SoundLoader.load(resource_path('sounds/sad_squeak.mp3'))
        self.game_over_sound = SoundLoader.load(resource_path('sounds/game_over.mp3'))

        self.music = SoundLoader.load(resource_path('music/1st level strange.mp3'))
        if self.music:
            self.music.loop = True
            self.music.volume = 0.0
            self.music.play()
            self.fade_in_music()

        with self.canvas.before:
            self.bg = Rectangle(
                source=resource_path("assets/level_bg.png"),
                size=Window.size,
                pos=(0, 0)
            )

        self.bind(size=self._update_rect, pos=self._update_rect)

        # Score - NO background
        self.score_label = Label(
            text=f"Score: {self.score}/10",
            font_size='48sp',
            color=(1, 1, 1, 1),
            outline_width=2,
            outline_color=(0, 0, 0, 1),
            size_hint=(None, None),
            size=(300, 70),
            pos=(15, Window.height - 80)
        )
        self.add_widget(self.score_label)

        # Lives - NO background
        self.lives_label = Label(
            text=f"Lives: {self.lives}",
            font_size='48sp',
            color=(1, 1, 1, 1),
            outline_width=2,
            outline_color=(0, 0, 0, 1),
            size_hint=(None, None),
            size=(200, 70),
            pos=(Window.width - 210, Window.height - 80)
        )
        self.add_widget(self.lives_label)

        self.player = Player()
        self.add_widget(self.player)

        self.critters = []

        Clock.schedule_interval(self.spawn_critter, 1.4)
        Clock.schedule_interval(self.update_game, 1 / 60.0)

        Window.bind(mouse_pos=self.on_mouse_move)
        self._keyboard = Window.request_keyboard(self._keyboard_closed, self)
        self._keyboard.bind(on_key_down=self.on_key_down)

    def fade_in_music(self):
        if self.music:
            def fade_step(dt):
                if self.music.volume < 0.95:
                    self.music.volume += 0.1
                    Clock.schedule_once(fade_step, 0.05)
                else:
                    self.music.volume = 1.0
            fade_step(0)

    def _update_rect(self, instance, value):
        self.bg.pos = instance.pos
        self.bg.size = instance.size

    def _keyboard_closed(self):
        if self._keyboard:
            self._keyboard.unbind(on_key_down=self.on_key_down)
            self._keyboard = None

    def spawn_critter(self, dt):
        if self.score < 10 and self.game_active:
            if random.random() < 0.38:
                bad_type = random.randint(0, 2)
                critter = Critter(bad_type, is_bad=True)
            else:
                critter = Critter(self.current_good_critter, is_bad=False)
                self.current_good_critter = (self.current_good_critter + 1) % 5
            
            self.critters.append(critter)
            self.add_widget(critter)

    def update_game(self, dt):
        if not self.game_active:
            return

        for critter in self.critters[:]:
            if critter.is_caught:
                continue

            critter.move(dt)

            if self.check_collision(self.player, critter):
                if critter.is_bad:
                    self.lose_life(critter, caught_bad=True)
                else:
                    self.catch_critter(critter)
            elif critter.y < -100:
                if not critter.is_bad:
                    self.lose_life(critter, caught_bad=False, missed=True)
                else:
                    self.critters.remove(critter)
                    self.remove_widget(critter)

    def catch_critter(self, critter):
        critter.is_caught = True
        self.critters.remove(critter)
        self.remove_widget(critter)

        if self.good_catch_sound:
            self.good_catch_sound.play()

        self.score += 1
        self.score_label.text = f"Score: {self.score}/10"

        if self.score >= 10:
            self.win_game()

    def lose_life(self, critter, caught_bad=False, missed=False):
        critter.is_caught = True
        self.critters.remove(critter)
        self.remove_widget(critter)

        if missed:
            if self.missed_sound:
                self.missed_sound.play()
        elif caught_bad:
            if self.bad_catch_sound:
                self.bad_catch_sound.play()

        self.lives -= 1
        self.lives_label.text = f"Lives: {self.lives}"

        if self.lives <= 0:
            self.game_over()

    def check_collision(self, player, critter):
        return (
            critter.x < player.x + player.width - 20 and
            critter.x + critter.width > player.x + 20 and
            critter.y < player.y + player.height - 20 and
            critter.y + critter.height > player.y + 20
        )

    def on_key_down(self, keyboard, keycode, text, modifiers):
        if keycode[1] == "left":
            self.player.x = max(0, self.player.x - 25)
        elif keycode[1] == "right":
            self.player.x = min(Window.width - self.player.width, self.player.x + 25)

    def on_mouse_move(self, window, pos):
        if self.game_active:
            self.player.x = pos[0] - self.player.width / 2
            self.player.x = max(0, min(Window.width - self.player.width, self.player.x))

    def game_over(self):
        self.game_active = False
        Clock.unschedule(self.spawn_critter)
        Clock.unschedule(self.update_game)

        if self.music:
            self.music.stop()
        if self.game_over_sound:
            self.game_over_sound.play()

        for critter in self.critters[:]:
            self.remove_widget(critter)
        self.critters.clear()

        lose_msg = Label(
            text="Game Over!\nYou Lost All Lives",
            font_name='Gothess',
            font_size='72sp',
            color=(1, 1, 1, 1),
            halign='center',
            valign='middle',
            size_hint=(None, None),
            size=(Window.width, 220)
        )
        lose_msg.bind(size=lose_msg.setter('text_size'))
        
        with lose_msg.canvas.before:
            Color(0, 0, 0, 0.7)
            Rectangle(pos=(0, Window.height / 2 + 30), size=(Window.width, 220))
        
        lose_msg.pos = (0, Window.height / 2 + 30)
        self.add_widget(lose_msg)

        # Retry button background - TRANSPARENT GREY/BLACK
        with self.canvas:
            Color(0, 0, 0, 0.8)
            RoundedRectangle(pos=(370, Window.height / 2 - 90), size=(260, 95), radius=[20])
        
        retry_btn = Button(
            text="Retry",
            font_name='Gothess',
            size_hint=(None, None),
            size=(260, 95),
            pos=(370, Window.height / 2 - 90),
            background_normal='',
            background_color=(0, 0, 0, 0),
            color=(1, 1, 1, 1),
            font_size='54sp'
        )
        retry_btn.bind(on_press=self.retry_game)
        self.add_widget(retry_btn)

    def retry_game(self, instance):
        app = App.get_running_app()
        app.show_game()

    def win_game(self):
        self.game_active = False
        Clock.unschedule(self.spawn_critter)
        Clock.unschedule(self.update_game)

        if self.music:
            self.music.stop()

        for critter in self.critters[:]:
            self.remove_widget(critter)
        self.critters.clear()

        win_msg = Label(
            text="You Win!",
            font_name='Gothess',
            font_size='130sp',
            color=(1, 1, 1, 1),
            halign='center',
            valign='middle',
            size_hint=(None, None),
            size=(Window.width, 200)
        )
        win_msg.bind(size=win_msg.setter('text_size'))
        
        with win_msg.canvas.before:
            Color(0, 0, 0, 0.7)
            Rectangle(pos=(0, Window.height / 2 + 200), size=(Window.width, 200))
        
        win_msg.pos = (0, Window.height / 2 + 200)
        self.add_widget(win_msg)

        # Collect Reward button background - TRANSPARENT GREY/BLACK
        with self.canvas:
            Color(0, 0, 0, 0.8)
            RoundedRectangle(pos=(300, 280), size=(400, 100), radius=[20])
        
        self.collect_btn = Button(
            text="Collect Reward",
            font_name='Gothess',
            size_hint=(None, None),
            size=(400, 100),
            pos=(300, 280),
            background_normal='',
            background_color=(0, 0, 0, 0),
            color=(1, 1, 1, 1),
            font_size='52sp'
        )
        self.collect_btn.bind(on_press=self.show_tickets)
        self.add_widget(self.collect_btn)

        # Play Again button background - TRANSPARENT GREY/BLACK
        with self.canvas:
            Color(0, 0, 0, 0.8)
            RoundedRectangle(pos=(360, 160), size=(280, 80), radius=[20])
        
        playagain_btn = Button(
            text="Play Again",
            font_name='Gothess',
            size_hint=(None, None),
            size=(280, 80),
            pos=(360, 160),
            background_normal='',
            background_color=(0, 0, 0, 0),
            color=(1, 1, 1, 1),
            font_size='42sp'
        )
        playagain_btn.bind(on_press=self.retry_game)
        self.add_widget(playagain_btn)

    def show_tickets(self, instance):
        reward_sound = SoundLoader.load(resource_path('sounds/reward_sound.mp3'))
        if reward_sound:
            reward_sound.play()

        self.remove_widget(self.collect_btn)

        tickets = Image(
            source=resource_path("assets/reward_ticket.png"),
            size_hint=(None, None),
            size=(800, 400),
            allow_stretch=True,
            keep_ratio=True,
            pos=(100, 150)
        )
        self.add_widget(tickets)

        # Save button background - TRANSPARENT GREY/BLACK
        with self.canvas:
            Color(0, 0, 0, 0.8)
            RoundedRectangle(pos=(625, 90), size=(310, 90), radius=[20])
        
        save_btn = Button(
            text="Save Tickets",
            font_name='Gothess',
            size_hint=(None, None),
            size=(300, 90),
            pos=(625, 90),
            background_normal='',
            background_color=(0, 0, 0, 0),
            color=(1, 1, 1, 1),
            font_size='50sp'
        )
        save_btn.bind(on_press=self.save_tickets)
        self.add_widget(save_btn)

    def save_tickets(self, instance):
        root = tk.Tk()
        root.withdraw()
        
        file_path = filedialog.asksaveasfilename(
            defaultextension=".png",
            filetypes=[("PNG files", "*.png"), ("All files", "*.*")],
            title="Save Your Reward Tickets",
            initialfile="Valentine_Tickets.png"
        )
        
        if file_path:
            shutil.copy(resource_path("assets/reward_ticket.png"), file_path)
            print(f"Tickets saved to: {file_path}")


class ValentineApp(App):
    def build(self):
        self.title = "Valentine"
        root = FloatLayout()
        self.question_screen = ValentineQuestion(self)
        root.add_widget(self.question_screen)
        return root

    def show_game(self):
        root = self.root
        root.clear_widgets()
        self.game_screen = GameScreen()
        root.add_widget(self.game_screen)


if __name__ == "__main__":
    ValentineApp().run()
