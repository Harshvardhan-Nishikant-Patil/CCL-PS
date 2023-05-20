import os
import urllib
import json
import webapp2
from google.appengine.ext.webapp import template
class MainPage(webapp2.RequestHandler):
    def get(self):
        temp={}
        path=os.path.join(os.path.dirname(__file__),'template/index.html')
        self.response.out.write(template.render(path,temp))
    def post(self):
        name=self.request.get('name')
        country=self.request.get('country')
        url="http://universities.hipolabs.com/search?name="+name+"&country="+country
        data=urllib.urlopen(url).read()
        data=json.loads(data)

        if len(data) == 0:
            temp=[]
            path=os.path.join(os.path.dirname(__file__),'template/error.html')
            self.response.out.write(template.render(path,temp))
        else:
            domains=data[1]['domains'][0]
            name=data[1]['name']
            temp={"domains":domains,"name":name}
            path=os.path.join(os.path.dirname(__file__),'template/result.html')
            self.response.out.write(template.render(path,temp))
app=webapp2.WSGIApplication([('/',MainPage)],debug=True)