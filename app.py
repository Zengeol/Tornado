import tornado.ioloop
import tornado.web
class MainHandler(tornado.web.RequestHandler):
    def get(self): #'get' will handle the request
        # if it's post(self), it is a post request
        self.set_header("Content-Type", 'text/plain')
        self.write("Hello, world. <html><head><title>narf</title></head></html>")

def make_app():# this URL matches with this handle
    return tornado.web.Application([
        (r"/", MainHandler), #if it doesn't find the page, it will give us 404 message.
    ], autoreload=True)
if __name__ == "__main__":
    app = make_app()
    app.listen(8888) # post it on port 8888
    tornado.ioloop.IOLoop.current().start()