import socket

def get_port_number(service_name, protocol='tcp'):
    try:
        port = socket.getservbyname(service_name, protocol)
        print(f"The port number for {service_name} ({protocol}) is: {port}")
    except OSError:
        print(f"Service '{service_name}' not found.")

if __name__ == "__main__":
    service = input("Enter the service name (e.g., http, ftp, ssh): ").strip()
    protocol = input("Enter the protocol (tcp/udp, default is tcp): ").strip().lower() or 'tcp'
    get_port_number(service, protocol)

