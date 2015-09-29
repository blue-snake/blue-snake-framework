
# Provides abstraction for HTTP request

import cgi

class Request:

	def __init__(self):
		# Shared query container
		self.form = cgi.FieldStorage()

	def hasQuery(self, key):
		return self.form.has_key(key);

	def getQuery(self, key, default = None):
		if self.form.has_key(key):
			return self.form.getvalue(key)
		else:
			return default