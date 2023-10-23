from datetime import date
import time


class Timer:
	data = {}
	
	def __init__(self, app_title):
		self.app_title = app_title

	def time_entry(self):
		if self.app_title is None:
			return
		time.sleep(1)
		self.add_data()

	def add_data(self):
		today = str(date.today())
		if self.app_title in Timer.data:
			Timer.data[self.app_title][today] += 1
		else:
			Timer.data[self.app_title] = {today: 1}
