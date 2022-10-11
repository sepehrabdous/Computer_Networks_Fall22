import SimpleHTTPServer
import SocketServer

class CS414Handler(SimpleHTTPServer.SimpleHTTPRequestHandler):

    # Disable logging DNS lookups
    def address_string(self):
        return str(self.client_address[0])


PORT = 80

Handler = CS414Handler
httpd = SocketServer.TCPServer(("", PORT), Handler)
print "Server1: httpd serving at port", PORT
httpd.serve_forever()
