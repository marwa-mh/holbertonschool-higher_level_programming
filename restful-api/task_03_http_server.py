from http.server import HTTPServer, BaseHTTPRequestHandler
import json
"""Develop a simple API using Python with the `http.server` module"""

PORT = 8000


class SimpleAPI(BaseHTTPRequestHandler):
    """class SimpleAPI"""
    def do_GET(self):
        if self.path.startswith("/"):
            self.send_response(200)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write(b"Hello, this is a simple API!")
        elif self.path.startswith("/data"):
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            data = {"name": "John", "age": 30, "city": "New York"}
            self.wfile.write(json.dumps(data).encode())
        elif self.path.startswith("/status"):
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            self.wfile.write(json.dumps({"status": "OK"}).encode())
        elif self.path == "/info":
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            info = {"version": "1.0",
                    "description": "A simple API built with http.server"}
            self.wfile.write(json.dumps(info).encode())
        else:
            self.send_error(404, "Endpoint not found")


if __name__ == "__main__":
    httpd = HTTPServer(("", PORT), SimpleAPI)
    print(f"Serving on port {PORT}...")
    httpd.serve_forever
