import os
import urllib
import webapp2
import json
from google.appengine.ext.webapp import template
class MainPage(webapp2.RequestHandler):
    def get(self):
        temp={}
        path=os.path.join(os.path.dirname(__file__),'template/index.html')
        self.response.out.write(template.render(path,temp))
    
    def post(self):
        latitude=self.request.get('latitude')
        longitude=self.request.get('longitude')
        url="https://api.open-meteo.com/v1/forecast?latitude="+latitude+"&longitude="+longitude+"&current_weather=true"
        data=urllib.urlopen(url).read()
        data=json.loads(data)

        if data.get('error') is not None:
            temp={"data":data}
            path=os.path.join(os.path.dirname(__file__),'template/error.html')
            self.response.out.write(template.render(path,temp))
        else :
            temperature=data['current_weather']['temperature']
            windspeed=data['current_weather']['windspeed']
            time=data['current_weather']['time']
            winddirection=data['current_weather']['winddirection']
            temp={"temperature":temperature,"windspeed":windspeed,"time":time,"winddirection":winddirection}
            path=os.path.join(os.path.dirname(__file__),'template/result.html')
            self.response.out.write(template.render(path,temp))
app=webapp2.WSGIApplication([('/',MainPage)],debug=True)
