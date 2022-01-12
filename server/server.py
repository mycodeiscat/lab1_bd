import sys
import os
import functools

import http.server
import socketserver

import string
import random

def checksum256(st):
    return functools.reduce(lambda x,y:x+y, map(ord, st)) % 256

N=1024
text = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(N))

path_of_file = '/serverdata/text.txt'


#os.remove(path_of_file)
open(path_of_file, 'w').write(text)

PORT = 8000
DIRECTORY = "/serverdata"

if len(sys.argv) > 1:
    PORT = int(sys.argv[1])

class Handler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIRECTORY, **kwargs)

    def end_headers(self):
        self.send_my_headers()
        http.server.SimpleHTTPRequestHandler.end_headers(self)

    def send_my_headers(self):
        self.send_header("checksum", checksum256(text))

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print("serving at port", PORT)
    httpd.serve_forever()
