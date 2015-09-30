
 #
 # This file is part of the BlueSnake Framework
 # 
 # Copyright (c) No Global State Lab
 # 
 # For the full copyright and license information, please view
 # the license file that was distributed with this source code.
 #

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