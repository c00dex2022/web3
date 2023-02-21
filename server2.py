mport Base64
import csv
import http.server

# Create a server on port 80
server = http.server.HTTPServer(('localhost', 80), http.server.BaseHTTPRequestHandler)

# Handler for GET requests
def handle_get(self):
    self.send_response(200)
    self.end_headers()

    # Get the 'i' parameter from the query string
    query_components = self.path.split('?')
    if len(query_components) > 1:
        params = query_components[1].split('&')
        for param in params:
            if param.startswith('i='):
                i_value = param[2:]

                # Decode the i parameter from Base64
                decoded = Base64.b64decode(i_value)

                # Store the decoded value in a CSV file
                with open('output.csv', 'a') as csvfile:
                    writer = csv.writer(csvfile)
                    writer.writerow([decoded])

# Set the handler for GET requests
server.handle_get = handle_get

# Start the server
server.serve_forever()
