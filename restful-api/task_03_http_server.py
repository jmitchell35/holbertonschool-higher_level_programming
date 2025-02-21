#!/usr/bin/python3
import http.server
import socketserver
import json

PORT = 8000

class SimpleServer(http.server.BaseHTTPRequestHandler):
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
            self.send_header('Content-type', 'text/plain')
            message = "OK"
        elif self.path == "/info":
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            data = {
                "version": "1.0",
                "description": "A simple API built with HTTP server"
            }
            self.send_header('Content-type', 'application/json')
            message = json.dumps(data)
        elif self.path == "/":
            self.send_response(200)
            self.send_header('Content-type', 'text/plain')
            message = "Hello, this is a simple API!"
        else:
            self.send_response(404)
            self.send_header('Content-type', 'text/plain')
            message = "404 Not Found : The requested endpoint does not exist"
        self.end_headers()
        self.wfile.write(message.encode('utf-8'))
        
httpd = http.server.HTTPServer(("", PORT), SimpleServer)
print(f"Server started - listening on localhost:{PORT}")
try:
    httpd.serve_forever()
except KeyboardInterrupt:
    print("\nShutting down server...")
    httpd.server_close()