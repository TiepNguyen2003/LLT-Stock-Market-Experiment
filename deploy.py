import socket
import psutil
from app import app
from wsgiref.simple_server import make_server
from waitress import serve

def get_wifi_ip():
    # Get all network interfaces and their addresses
    interfaces = psutil.net_if_addrs()
    
    # Iterate through the interfaces and find the Wi-Fi interface
    for interface, addresses in interfaces.items():
        if "wlan" in interface or "en" in interface or "Wi-Fi" in interface:  # Check for Wi-Fi interfaces (common names are wlan or en)
            for address in addresses:
                if address.family == socket.AF_INET:  # Filter for IPv4 addresses
                    return address.address
    return None  # If no Wi-Fi interface found

if __name__ == '__main__':
    wifi_ip = get_wifi_ip()
    if wifi_ip:
        print(f"Starting server on Wi-Fi IP: http://{wifi_ip}:8080")
    else:
        print("Wi-Fi interface not found. Please connect to the internet.")

    port = 8080

    # Binds to the Wifi IP
    serve(app, host=wifi_ip, port=8080)

