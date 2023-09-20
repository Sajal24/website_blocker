import time
from datetime import datetime as dt

# Set the path to the hosts file depending on your operating system
hosts_path = "/etc/hosts"
# Local IP address
redirect = "127.0.0.1"

# List of websites to block
website_list = ["www.facebook.com", "facebook.com",
                "dub119.mail.live.com", "www.dub119.mail.live.com",
                "www.gmail.com", "gmail.com"]

while True:

    # Define your working hours
    if dt(dt.now().year, dt.now().month, dt.now().day, 8) < dt.now() < dt(dt.now().year, dt.now().month, dt.now().day, 16):
        print("During working hours...")
        with open(hosts_path, 'r+') as file:
            content = file.read()
            for website in website_list:
                if website in content:
                    pass
                else:
                    # Redirect website hostnames to your local IP address
                    file.write(redirect + " " + website + "\n")
    else:
        with open(hosts_path, 'r+') as file:
            content = file.readlines()
            file.seek(0)
            for line in content:
                if not any(website in line for website in website_list):
                    file.write(line)

            # Remove blocked hostnames from the hosts file
            file.truncate()

        print("During non-working hours...")
    time.sleep(5)
