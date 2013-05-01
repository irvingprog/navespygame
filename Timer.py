import time

class Timer():
	"""docstring for Timer"""
	def __init__(self):
		self.corriendo = False
		self.offset = 0

	def time(self):
		self.tiempo = (time.clock() - self.start())
		return self.tiempo

	def start(self):
		if not self.corriendo:
			self.corriendo=True
			self.offset = time.clock();

		return self.offset

	def stop(self):
		self.corriendo = False