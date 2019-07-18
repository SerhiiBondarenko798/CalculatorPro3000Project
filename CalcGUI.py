from kivy.app import App
from kivy.config import Config
from kivy.uix.button import Button
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.widget import Widget
from kivy.uix.bubble import Bubble
from kivy.uix.carousel import Carousel
from kivy.lang import Builder
from kivy.uix.image import Image
from kivy.graphics import (Color, Ellipse, Rectangle, Line)
from kivy.uix.label import Label
screen_width=400
screen_height=700
screen_text = '0'
Config.set('graphics', 'width', screen_width)
Config.set('graphics', 'height', screen_height)
Config.set('graphics', 'resizable', 1)

class CalcApp(App):
	def build(self):
		Calc_mainscreen = FloatLayout(size_hint=(1, 1))
		kalk_vijet = GridLayout(cols=4, spacing=3, padding = 3, size_hint=(1,.80), pos_hint={'center_x' : 0.5, 'y' :0})
		kalk_vijet.add_widget(Button(text='+', font_size=30))
		kalk_vijet.add_widget(Button(text='1', font_size=30))
		kalk_vijet.add_widget(Button(text='2', font_size=30))
		kalk_vijet.add_widget(Button(text='3', font_size=30))

		kalk_vijet.add_widget(Button(text='-', font_size=30))
		kalk_vijet.add_widget(Button(text='4', font_size=30))
		kalk_vijet.add_widget(Button(text='5', font_size=30))
		kalk_vijet.add_widget(Button(text='6', font_size=30))

		kalk_vijet.add_widget(Button(text='*', font_size=30))
		kalk_vijet.add_widget(Button(text='7', font_size=30))
		kalk_vijet.add_widget(Button(text='8', font_size=30))
		kalk_vijet.add_widget(Button(text='9', font_size=30))

		kalk_vijet.add_widget(Button(text='/', font_size=30))
		kalk_vijet.add_widget(Button(text='.', font_size=30))
		kalk_vijet.add_widget(Button(text='0', font_size=30))
		kalk_vijet.add_widget(Button(text='=', font_size=30))

		output_screen = Label(text=screen_text, font_size = 50,size_hint=(1,.20),  pos_hint={'center_x' : 0.5, 'top' :1}, halign='right', text_size = (screen_width-12, screen_height*.20 -12))
		Calc_mainscreen.add_widget(kalk_vijet)
		Calc_mainscreen.add_widget(output_screen)
		return Calc_mainscreen







if __name__ == '__main__':
	CalcApp().run()