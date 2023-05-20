import webapp2
class MainPage(webapp2.RequestHandler):
	def get(self):
		for i in range(5):
			self.response.out.write("Harshvardhan Patil </br>")
			self.response.out.write("33346 </br>")
			self.response.out.write("Information Technology </br>")
app=webapp2.WSGIApplication([('/',MainPage)],debug=True)
			
