import csv

# specify the log file path
log_file = "/var/log/apache2/access.log"

# create an empty list to store URLs
urls = []

# open the log file and read each line
with open(log_file, "r") as file:
    for line in file:
        # split the line by whitespace
        parts = line.split()

        # get the requested URL from the "GET" request
        if len(parts) > 6 and parts[5] == "GET":
            url = parts[6].split("?")[0]
            urls.append(url)

# write the URLs to a CSV file
with open("output1.csv", "w", newline="") as file:
    writer = csv.writer(file)
    for url in urls:
        writer.writerow([url])
