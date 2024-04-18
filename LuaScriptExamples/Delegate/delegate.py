from http.server import BaseHTTPRequestHandler, HTTPServer

import os
import sys
sys.path.append("../")
import ob_helper
from ob import ob
import argparse
from xml.dom import minidom
from svg.path import parse_path
import urllib
import re
import json

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

class S(BaseHTTPRequestHandler):
    def _set_response(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

    def do_GET(self):
        path = self.path
        print(f"{bcolors.WARNING}GET request{bcolors.ENDC},\nPath: {path}\nHeaders:\n{str(self.headers)}\n")
        self._set_response()
        resp = "GET request for {}".format(path)
        if path == "/":
          self.send_header('Content-Type', 'application/json')
          self.end_headers()
          resp = serve()
        self.wfile.write(resp.encode('utf-8'))

    def do_POST(self):
        content_length = int(self.headers['Content-Length']) # <--- Gets the size of data
        post_data = self.rfile.read(content_length) # <--- Gets the data itself
        print("POST request,\nPath: %s\nHeaders:\n%s\n\nBody:\n%s\n",
                str(self.path), str(self.headers), post_data.decode('utf-8'))

        self._set_response()
        self.wfile.write("POST request for {}".format(self.path).encode('utf-8'))

def run(server_class=HTTPServer, handler_class=S, port=8080):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print('Starting httpd...\n')
    try:
        httpd.serve_forever()
        # httpd.handle_request()
    except KeyboardInterrupt:
        pass
    httpd.server_close()
    print('Stopping httpd...\n')


svgDict = {}
def parseSVGs():
  doc = minidom.parse("LUCON.svg")
  for ipath, path in enumerate(doc.getElementsByTagName("glyph")):
    if path.hasAttribute('d') == False: continue
    u = path.getAttribute('unicode')
    d = path.getAttribute('d')
    svgDict[u] = d
    if ipath > 10: return

def server():
  parseSVGs()
  run()

COUNTER = 0
@staticmethod
def serve():
  # ob.new()
  # ob.user.move.to("0,0,20")
  # ob.brush.move.to("0,20,0")

  global COUNTER, svgDict
  COUNTER += 1
  return json.dumps({'svgPath': 'M703 1129l306 139l61 -188l-328 -68v14q0 53 -39 103zM732 983l226 -248l-160 -116l-166 291q63 18 100 73zM601 910l-165 -291l-160 116l226 248q37 -55 99 -73zM492 1012l-328 68l61 188l305 -139q-38 -50 -38 -104v-13zM555 1147l-37 333h198l-37 -333q-35 13 -62 13t-62 -13z'})


def main():
  if "OB_HOST" in os.environ:
    ob.OB_HOST = os.environ['OB_HOST']
  ob.brush.type("Light")
  ob.brush.move.to("0,0,0")
  

  server()

if __name__ == '__main__':
    main()
