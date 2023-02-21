import http.server
import socketserver
import base64
import csv

# Define the HTTP request handler
class HTTPRequestHandler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write(b'Hello, world!')

    def do_POST(self):
        # Read the request data
        content_length = int(self.headers['Content-Length'])
        request_data = self.rfile.read(content_length)

        # Decode the Base64-encoded data
        decoded_data = base64.b64decode(request_data).decode('utf-8')

        # Write the decoded data to a CSV file
        with open('output.csv', 'a', newline='') as csvfile:
            csv_writer = csv.writer(csvfile)
            csv_writer.writerow([decoded_data])

        # Send a response
        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()
        self.wfile.write(b'Success')

# Set up the server
PORT = 80
Handler = HTTPRequestHandler
httpd = socketserver.TCPServer(("", PORT), Handler)

# Start the server
print(f'Starting server on port {PORT}...')
httpd.serve_forever()
