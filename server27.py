class RequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        # extract the requested URL
        url = self.path.split("?")[0]
        
        # check if the URL contains "?i="
        if not "?i=" in self.path:
            # send a 404 Not Found response
            self.send_response(404)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            self.wfile.write(b"404 Not Found")
            return
        
        # extract the value of "i" parameter from the URL
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
