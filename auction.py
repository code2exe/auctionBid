import pyautogui as auto
from time import sleep
import configparser
OK_position = (811, 335)
potpisi = (685, 256)
pass_io = (455, 295)
after_pass = (928, 345)
pwd = configparser.ConfigParser()
pwd.read('config.ini')
key = pwd['PKI']['password']
def main():
	sleep(2)
	auto.moveTo(1133, 565, duration=0)
	sleep(0.5)
	auto.click(1133, 565, duration=0.5, clicks=1, interval=0.0, button='left')
	sleep(10)
	auto.moveTo(OK_position, duration=0.25)
	auto.click(OK_position, duration=0.5, clicks=1, interval=0.0, button='left')
	auto.moveTo(potpisi, duration=0.25)
	auto.click(potpisi, duration=0.5, clicks=1, interval=0.0, button='left')
	sleep(0.5)
	# key input
	auto.moveTo(pass_io, duration=0.25)
	sleep(0.5)
	auto.click(pass_io, duration=0.5, clicks=1, interval=0.0, button='left')
	sleep(0.5)
	auto.typewrite(key)
	# end key input
	sleep(0.5)
	auto.moveTo(after_pass, duration=0.25)
	sleep(0.5)
	auto.click(after_pass, duration=0.5, clicks=1, interval=0.0, button='left')
	sleep(1)

if __name__ == '__main__':
	main()