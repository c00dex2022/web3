class HTTPRequestHandler(http.server.BaseHTTPRequestHandler):
    def do_POST(self):
        # Read the request data
        content_length = int(self.headers['Content-Length'])
        request_data = self.rfile.read(content_length).decode('utf-8')

        # Extract the data between the "i" parameter and the end of the request
        i_param_index = request_data.find("i=")
        if i_param_index != -1:
            http_index = request_data.find("HTTP/1.1", i_param_index)
            if http_index != -1:
                data = request_data[i_param_index+2:http_index].strip()

                # Decode the Base64-encoded data
                decoded_data = base64.b64decode(data).decode('utf-8')

                # Write the decoded data to a CSV file
                with open('output.csv', 'a', newline='') as csvfile:
                    csv_writer = csv.writer(csvfile)
                    csv_writer.writerow([decoded_data])

        # Send a response
        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()
        self.wfile.write(b'Success')
