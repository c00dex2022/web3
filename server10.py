import base64
from http.server import HTTPServer, BaseHTTPRequestHandler
import csv

class RequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        # extract the requested URL
        url = self.path.split("?")[0]
        if "i=" in self.path:
            i_param = self.path.split("i=")[1].split("&")[0]
            url += "?i=" + i_param
        
        # log the URL to the console
        print("Requested URL:", url)

        # extract the base64-encoded value from the URL
        b64_value = ""
        if "b64=" in self.path:
            b64_value = self.path.split("b64=")[1].split("&")[0]
        
        # decode the base64 value
        decoded_value = base64.b64decode(b64_value).decode("utf-8")

        # remove "/?i=" from the URL and write it to a CSV file
        with open("output1.csv", "a", newline="") as file:
            writer = csv.writer(file)
            writer.writerow([url.replace("/?i=", ""), decoded_value])

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
