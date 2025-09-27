import os
import requests

# URLs to download the txt files
url1 = "https://a.dove.isdumb.one/127.txt"
url2 = "https://a.dove.isdumb.one/list.txt"

# Download the content from the URLs
response1 = requests.get(url1)
response2 = requests.get(url2)

# Check if the requests were successful
if response1.status_code == 200 and response2.status_code == 200:
    content1 = response1.text
    content2 = response2.text

    # Combine the content from both files
    combined_content = content1 + "\n" + content2

    # Define the path to the hosts file to be created
    hosts_file_path = "hosts"

    # Write the combined content to the hosts file
    with open(hosts_file_path, "w") as file:
        file.write(combined_content)

    # Destination directory for the hosts file
    dest_dir = r"C:\Windows\System32\drivers\etc"

    # Destination path for the hosts file
    dest_path = os.path.join(dest_dir, "hosts")

    # Move the hosts file to the destination directory
    os.replace(hosts_file_path, dest_path)
else:
    print("Failed to download one or both of the files.")
    os.system('pause')
    
