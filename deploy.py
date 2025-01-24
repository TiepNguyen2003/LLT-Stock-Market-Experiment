import socket
import psutil
from app import create_app
from waitress import serve
import os

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
    port = os.environ.get('PORT', 8080)
    app = create_app()
    url_scheme = os.environ.get('URL_SCHEME', 'http')
    
    print(f"Serving Flask app on http://{wifi_ip if wifi_ip else 'localhost'}:{port}")
    # Bind to 0.0.0.0 to listen on all network interfaces (if needed)
    serve(app,host='0.0.0.0', port=port, url_scheme = url_scheme)