#!/usr/bin/env python3
"""Static file server with no-cache headers for the preview (avoids stale builds)."""
import http.server
import socketserver
import os

os.chdir('/home/user/mobile_shop1/dist')

class Handler(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header('Cache-Control', 'no-store, no-cache, must-revalidate, max-age=0')
        self.send_header('Pragma', 'no-cache')
        self.send_header('Expires', '0')
        super().end_headers()
    def log_message(self, *args):
        pass

class Server(socketserver.TCPServer):
    allow_reuse_address = True

with Server(('0.0.0.0', 4173), Handler) as httpd:
    httpd.serve_forever()
