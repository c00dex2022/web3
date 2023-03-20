from http.server import HTTPServer, BaseHTTPRequestHandler
import csv
import base64

class RequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        # check if token variable exists and has the correct value
        if "token" not in self.path or self.path.split("token=")[1].split("&")[0] != "VmFsdWVfc2V0dGluZ19nZW9fc2NfNTo0NlBNLTIwLU1hcmNoLTIwMjM=":
            # if token variable doesn't exist or has incorrect value, drop the request and block the IP address
            self.send_response(403)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            self.wfile.write(b"Access forbidden. Your IP address has been blocked.")
        else:
            # extract the requested URL
            url = self.path.split("?")[0]
            if "i=" in self.path:
                i_param = self.path.split("i=")[1].split("&")[0]
                url += "?i=" + i_param

            # log the URL to the console
            print("Requested URL:", url)

            # remove "/?i=" from the URL and write it to a CSV file
            url_without_i = url.replace("/?i=", "")
            with open("output1.csv", "a", newline="") as file:
                writer = csv.writer(file)
                writer.writerow([url_without_i])

            # decode base64 and save to output2.csv
            decoded_url = base64.b64decode(url_without_i).decode("utf-8")
            with open("output2.csv", "a", newline="") as file:
                writer = csv.writer(file)
                writer.writerow([decoded_url])

            # send an empty response with a 200 status code
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            self.wfile.write(b"")

if __name__ == "__main__":
    # specify the server address and port
    server_address = ("", 8080)

    # create the HTTP server
    httpd = HTTPServer(server_address, RequestHandler)
    print("Server running at http://localhost:8080")

    try:
        # serve requests indefinitely
        httpd.serve_forever()
    except KeyboardInterrupt:
        # gracefully shut down the server on Ctrl-C
        httpd.server_close()
        print("Server stopped")
