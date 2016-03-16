import http.server
import socketserver
import os
import shutil

PORT = 8080

class MjpegServerHandler(http.server.BaseHTTPRequestHandler):
	def do_GET(self):
		print ("override")

		'''
		f = self.send_head()
		if f:
			try:
				print (f)
				self.copyfile(f, self.wfile)
			finally:
				f.close() '''
	
		path = "c:\\dev\\web_dev\\simple_project\\images\\20150516_123212.jpg"
		try:
			f = open(path, 'rb')
		except OSError:
			self.send_error(404, "File not found")
			return None
		try:
			self.send_response(200)
			self.send_header("Content-type", "multipart/x-mixed-replace")
			fs = os.fstat(f.fileno())
			self.send_header("Content-Length", str(fs[6]))
			self.send_header("Last-Modified", self.date_time_string(fs.st_mtime))
			self.end_headers()
			shutil.copyfileobj(f, self.wfile)
		except:
			f.close()
			raise

Handler = MjpegServerHandler
httpd = socketserver.TCPServer(("127.0.0.1", PORT), Handler)

print("server at port", PORT)
httpd.serve_forever()