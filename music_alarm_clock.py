'''
Music alarm clock
'''
from time import sleep
import datetime
from datetime import date
import pyglet

music_for_alarm_clock = pyglet.resource.media('music.mp3')

def check_validity(year, month ,day, hour, minutes):
	try:
		tmp = datetime.datetime(year, month ,day, hour, minutes)
		return True
	except:
		return False

def compare_dates(year, month, day, hour, minutes):
	user_set = datetime.datetime(year, month ,day, hour, minutes)
	if datetime.datetime.now() > user_set:
		print('This date is in the past!')
		return False
	elif (user_set - datetime.datetime.now()).days > 0:
	 	print('It is boring to wait so long!')
	 	return False
	else:
		return True

def wait_for_music(year, month, day, hour, minutes):
	while True:
		current_time = datetime.datetime.now()
		sleep(1)

		if day == current_time.day and hour == current_time.hour and minutes == current_time.minute:
			break
	music_for_alarm_clock.play()
	pyglet.app.run()			 	

def main():
	year = date.today().year
	month = date.today().month
	while True:
		try:
			day = int (input("Day: "))
			hour = int (input("Hour: "))
			minutes = int (input("Minutes: "))
		except:
			print('Invalid date!')
			continue	
		if check_validity(year, month, day, hour, minutes) == True:
			if compare_dates(year, month, day, hour, minutes)  == True:
				wait_for_music(year, month, day, hour, minutes)
		else:
			print('Invalid date!')

main()
