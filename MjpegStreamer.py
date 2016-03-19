from BaseHTTPServer import BaseHTTPRequestHandler
import SocketServer
import os
import shutil
import time
import numpy as np
import cv2
import httplib

PORT = 8080

class MjpegServerHandler(BaseHTTPRequestHandler):

	def capture_image(self):
		cap = cv2.VideoCapture(0)

	def do_GET(self):
		cap = cv2.VideoCapture(0)
		path = "c:\\dev\\web_dev\\simple_project\\images\\"
		
		try:
			self.send_response(httplib.OK)
			self.send_header("Content-type", "multipart/x-mixed-replace;boundary=123")
			self.end_headers()
			i = 1
			while True:
				try:
					f = open(path + str(i%3) + ".jpg", 'rb')
					fs = os.fstat(f.fileno())
				except OSError:
					raise
				self.wfile.write("--123")
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
httpd = SocketServer.TCPServer(("127.0.0.1", PORT), Handler)

print "server at port", PORT
httpd.serve_forever()