from mycroft import MycroftSkill, intent_handler
from adapt.intent import IntentBuilder
import RPi.GPIO as GPIO
import requests

GPIO.setmode(GPIO.BCM)
GPIO.setup(27, GPIO.OUT)
GPIO.setup(22, GPIO.OUT)
GPIO.setup(17, GPIO.OUT)
GPIO.setup(10, GPIO.OUT)
GPIO.setup(9, GPIO.OUT)

class Ledtester(MycroftSkill):
	def __init__(self):
		super().__init__()

	@intent_handler(IntentBuilder('DoorUnlock').require('lock').require('door'))
	def handle_Door_Unlock(self, message):
		if message.data['lock'].upper() == 'UNLOCK':
			GPIO.output(27, GPIO.HIGH)
			self.speak('Door is unlocked')
		elif message.data['lock'].upper() == 'LOCK':
			GPIO.output(27, GPIO.LOW)
			self.speak('Door is locked')

	@intent_handler(IntentBuilder('BlindOpen').require('open').require('blind'))
	def handle_Blind_Open(self, message):
		if message.data['open'].upper() == 'OPEN':
			GPIO.output(22, GPIO.HIGH)
			self.speak('Blind is open')
		elif message.data['open'].upper() == 'CLOSE':
			GPIO.output(22, GPIO.LOW)
			self.speak('Blind is closed')
			
	@intent_handler(IntentBuilder('LightSwitch').require('command').require('onoff').require('object'))
	def handle_Light_Switch(self, message):
		if message.data['object'].upper() == 'FAN':
			if message.data['onoff'].upper() == 'ON':
				GPIO.output(17, GPIO.HIGH)
				self.speak_dialog('fanon')
			elif message.data['onoff'].upper() == 'OFF':
				GPIO.output(17, GPIO.LOW)
				self.speak_dialog('fanoff')
		elif message.data['object'].upper() == 'LIVING LIGHT':
			if message.data['onoff'].upper() == 'ON':
				GPIO.output(10, GPIO.HIGH)
				self.speak_dialog('livingon')
			elif message.data['onoff'].upper() == 'OFF':
				GPIO.output(10, GPIO.LOW)
				self.speak_dialog('livingoff')
		elif message.data['object'].upper() == 'ROOM LIGHT':
			if message.data['onoff'].upper() == 'ON':
				GPIO.output(9, GPIO.HIGH)
				self.speak_dialog('roomon')
			elif message.data['onoff'].upper() == 'OFF':
				GPIO.output(9, GPIO.LOW)
				self.speak_dialog('roomoff')
		elif message.data['object'].upper() == 'WIFI LIGHT':
			if message.data['onoff'].upper() == 'ON':
				r = requests.get('http://192.168.42.140/LED=ON')
				self.speak_dialog('wifion')
			elif message.data['onoff'].upper() == 'OFF':
				r = requests.get('http://192.168.42.140/LED=OFF')
				self.speak_dialog('wifioff')
				

def create_skill():
	return Ledtester()
