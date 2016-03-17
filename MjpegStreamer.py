import http.server
import socketserver
import os
import shutil
import time

PORT = 8080

class MjpegServerHandler(http.server.BaseHTTPRequestHandler):
	def do_GET(self):
		path = "c:\\dev\\web_dev\\simple_project\\images\\"
		
		try:
			self.send_response(200)
			self.send_header("Content-type", "multipart/x-mixed-replace;boundary=123")
			self.end_headers()
			i = 1
			while True:
				try:
					f = open(path + str(i%3) + ".jpg", 'rb')
					fs = os.fstat(f.fileno())
				except OSError:
					raise
				self.wfile.write(bytes("--123","utf-8"))
				self.send_header("Content-type", "image/jpeg")
				self.send_header("Content-Length", str(fs[6]))
				self.end_headers()
				
				self.wfile.write(f.read())
				time.sleep(1)
				f.close()
				i = i + 1
				print(i)
		except:
			raise

Handler = MjpegServerHandler
httpd = socketserver.TCPServer(("127.0.0.1", PORT), Handler)

print("server at port", PORT)
httpd.serve_forever()