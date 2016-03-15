import http.server
import socketserver

PORT = 8080

class MjpegServerHandler(http.server.SimpleHTTPRequestHandler):
	def do_GET(self):
		print ("override")
		f = self.send_head()
		'''
		if f:
			try:
				print (f)
				self.copyfile(f, self.wfile)
			finally:
				f.close() '''

#Handler = http.server.SimpleHTTPRequestHandler
Handler = MjpegServerHandler
httpd = socketserver.TCPServer(("127.0.0.1", PORT), Handler)

print("server at port", PORT)
httpd.serve_forever()