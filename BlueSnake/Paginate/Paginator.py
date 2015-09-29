
# Pagination class

class Paginator:

	def __init__(self):
		pass

	def tweak(self, totalAmount, page, perPageCount):
		self.totalAmount = totalAmount
		self.page = page
		self.perPageCount = perPageCount

	def setUrl(self, url):
		self.url = url
		return self

	def getUrl(self):
		return self.url

	def getFirstPage(self):
		return 1

	def getLastPage(self):
		pass

	def countOffset(self):
		return (self.page - 1) * self.perPageCount