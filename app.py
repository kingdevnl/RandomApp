#!/usr/bin/python

from http.server import BaseHTTPRequestHandler, HTTPServer

PORT_NUMBER = 8080

class MyHandler(BaseHTTPRequestHandler):

  def do_GET(self):
    """Handler for GET requests"""
    self.send_response(200)
    self.send_header('Content-type','text/html')
    self.end_headers()
    self.wfile.write("<h1>Hello to this app</h1>")

try:
  server = HTTPServer(('', PORT_NUMBER), MyHandler)
  print('Started app httpserver on port', PORT_NUMBER)
  server.serve_forever()

except KeyboardInterrupt:
  server.server_close()
  print('Stopping server')
