import http.server
import socketserver
import base64
import csv

class HTTPRequestHandler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write(b'Hello, world!')

    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        request_data = self.rfile.read(content_length).decode('utf-8')

        i_param_index = request_data.find("i=")
        if i_param_index != -1:
            http_index = request_data.find("HTTP/1.1", i_param_index)
            if http_index != -1:
                data = request_data[i_param_index+2:http_index].strip()

                decoded_data = base64.b64decode(data).decode('utf-8')

                with open('output.csv', 'a', newline='') as csvfile:
                    csv_writer = csv.writer(csvfile)
                    csv_writer.writerow([decoded_data])

        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()
        self.wfile.write(b'Success')

PORT = 80
Handler = HTTPRequestHandler
httpd = socketserver.TCPServer(("", PORT), Handler)

print(f'Starting server on port {PORT}...')
httpd.serve_forever()
