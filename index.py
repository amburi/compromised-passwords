import json
from http.server import BaseHTTPRequestHandler, HTTPServer

# Updated list of compromised passwords
COMPROMISED_PASSWORDS = {'password123', '123456', 'qwerty', 'letmein'}

class RequestHandler(BaseHTTPRequestHandler):
    def _set_headers(self, status_code=200, content_type="application/json"):
        self.send_response(status_code)
        self.send_header('Content-Type', content_type)
        self.end_headers()

    def _respond_with_message(self, status_code, message):
        self._set_headers(status_code)
        response = json.dumps({"message": message}).encode()
        self.wfile.write(response)

    def do_POST(self):
        if self.path == '/compromised':
            content_length = int(self.headers['Content-Length'])
            body = self.rfile.read(content_length)

            if not body:
                self._respond_with_message(400, "Password not provided!")
                return

            try:
                data = json.loads(body)
            except json.JSONDecodeError:
                self._respond_with_message(400, "Invalid JSON!")
                return

            password = data.get('password')
            if password is None:
                self._respond_with_message(400, "Password not provided!")
                return

            print(f"Checking password {password}")

            if password not in COMPROMISED_PASSWORDS:
                self._set_headers(204)
            else:
                self._respond_with_message(200, "Password is compromised!")
        else:
            self._respond_with_message(404, "Not found!")

    def do_GET(self):
        self._respond_with_message(405, "Method Not Allowed")

def run(server_class=HTTPServer, handler_class=RequestHandler, port=8080):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print(f'Starting server on port {port}')
    httpd.serve_forever()

if __name__ == "__main__":
    run()
