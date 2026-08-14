from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.clock import Clock
import cv2

class SmartTrackerApp(App):
    def build(self):
        self.counter = 0
        layout = BoxLayout(orientation='vertical', padding=20, spacing=10)
        
        # App ki Screen par text aur buttons
        self.label = Label(text="🚀 Smart Tracker Active!\nPress Start to Run", font_size='20sp', halign='center')
        layout.add_widget(self.label)
        
        start_btn = Button(text="Start Background Loop", size_hint=(1, 0.2), background_color=(0.1, 0.8, 0.4, 1))
        start_btn.bind(on_press=self.start_loop)
        layout.add_widget(start_btn)
        
        return layout

    def start_loop(self, instance):
        self.label.text = "🔄 Background Loops Running...\nPress Control + C (or back) to quit."
        # Har 1 second baad background logic chalane ke liye clock trigger
        Clock.schedule_interval(self.background_logic, 1.0)

    def background_logic(self, dt):
        self.counter += 1
        # Piche camera aur counter ka kaam chalta rahega
        cap = cv2.VideoCapture(0)
        if cap.isOpened():
            ret, frame = cap.read()
            cap.release()
        print(f"Loop count: {self.counter}")

if __name__ == '__main__':
    SmartTrackerApp().run()
