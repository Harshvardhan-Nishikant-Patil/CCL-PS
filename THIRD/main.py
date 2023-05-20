import webapp2
class MainPage(webapp2.RequestHandler):
	def get(self):
		i=0
		while i<10:
			self.response.out.write('HNP</br>')
			self.response.out.write('33377</br>')
			self.response.out.write('IT</br>')
			i+= 1
app=webapp2.WSGIApplication([('/',MainPage)],debug=True) 
