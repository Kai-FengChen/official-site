import tornado.web
import tornado.wsgi
import os

class MainHandler(tornado.web.RequestHandler):
    def get(self):
    	self.render("twcl.html")
        # self.write("Hello, world!!!")

settings = {
    'template_path': os.path.join(os.path.dirname(__file__), 'templates'),
    'debug':False,
}
tornado_app = tornado.web.Application([
    (r"/", MainHandler),
],**settings)
app = tornado.wsgi.WSGIAdapter(tornado_app)