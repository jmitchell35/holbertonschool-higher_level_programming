#!/usr/bin/python3
from http.server import BaseHTTPRequestHandler, HTTPServer
import json

PORT = 8000

class SimpleServer(BaseHTTPRequestHandler):
    def do_GET(self):    
        if self.path == "/data":
            data = {
                "name": "John",
                "age": 30,
                "city": "New York"
            }
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            message = json.dumps(data)
        elif self.path == "/status":
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            message = "OK"
        elif self.path == "/info":
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            data = {
                "version": "1.0",
                "description": "A simple API built with HTTP server"
            }
            message = json.dumps(data)
        elif self.path == "/":
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            message = "Hello, this is a simple API!"
        else:
            self.send_response(404)
            self.send_header('Content-type', 'text/html')
            message = "404 Not Found : The requested endpoint does not exist"
        self.end_headers()
        self.wfile.write(message.encode('utf-8'))
        
httpd = HTTPServer(("localhost", PORT), SimpleServer)
try:
    print("Server starting on localhost:8000...")
    httpd.serve_forever()
except KeyboardInterrupt:
    print("\nShutting down the server...")
    httpd.server_close()