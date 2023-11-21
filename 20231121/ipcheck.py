import socket

def get_ip_address(hostname):
    try:
        ip_address = socket.gethostbyname(hostname)
        return ip_address
    except socket.error as e:
        print(f"Error: {e}")
        return None

hostname = 'www.it-college.ac.jp'

ip_address = get_ip_address(hostname)

if ip_address:
    print(f"The IP address of {hostname} is: {ip_address}")
else:
    print(f"Failed to retrieve the IP address for {hostname}")
