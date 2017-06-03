# P-Node will store process information
#@author Josue Ruiz CS 431

class pnode:

	def __init__(self, pid):
		self.pid = pid
		self.jobs = {}
		self.counter = 0
		self.time_left = 0
		self.lock = 0
		self.total = 0

	def add(self, job):
		self.jobs.append(job)

	def current(self):
		if self.counter > len(self.jobs)-1:
			return -1
		else:
			return self.jobs[self.counter]

	def next(self):
		self.counter = self.counter + 1

	def isOdd(self):
		if self.jobs[self.counter] % 2 == 0:
			return True
		else:
			return False

	def set(self, result):
		self.jobs[self.counter] = result

	def done(self):
		num = "%02d" % (self.pid)
		string = "\tP"+str(num) + " is done"
		return string

	def sort_list(self):
		self.jobs.sort()

	def add_total(self):
		for x in range(len(self.jobs)):
			self.total = self.total + self.jobs[x]


	def __str__(self):
		string = str(self.pid)+ " "
		for x in range(len(self.jobs)):
			string += str(self.jobs[x]) + " "
		return string
