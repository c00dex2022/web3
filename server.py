import csv
import base64
from http.server import BaseHTTPRequestHandler, HTTPServer

class RequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        # Get the value of the i parameter from the query string
        query = self.path.split('?')[-1]
        i_param = query.split('=')[1] if 'i=' in query else ''

        # Decode the i parameter value from Base64 to regular text
        i_param_decoded = base64.b64decode(i_param).decode('utf-8')

        # Save the decoded value to a CSV file
        with open('output.csv', mode='a') as csv_file:
            writer = csv.writer(csv_file)
            writer.writerow([i_param_decoded])

        # Send an empty response to the client
        self.send_response(200)
        self.end_headers()

def run(server_class=HTTPServer, handler_class=RequestHandler, port=8000):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print(f'Starting server on port {port}...')
    httpd.serve_forever()

if __name__ == '__main__':
    run()
