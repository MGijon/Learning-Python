import time

class Date(object):

	# Mean constructor
	def __init__(self, year, month, day):
		''' save year, month and day '''
		self.year = year
		self.month = month
		self.day = day

	# Alternative constructor
	@classmethod
	def today(cls):
		''' Uses 'time' class to save the current data '''
		t = time.localtime()
		return cls(t.tm_year, t.tm_mon, t.tm_mday)


a = Date(2012, 12, 21)
b = Date.today()

print('It\'s: ' + str(b.day))
print('month: ' + str(b.month))
print('year: ' + str(b.year))

print('Time function of the data class: ' + Date.today.__doc__)
print('Data class constructor: ' + Date.__init__.__doc__)