import ipaddress
import argparse
from colorama import init, Fore, Style

# Initialize colorama
init(autoreset=True)

def subnet_calculator(ip_str, subnet_mask_str):
    ip = ipaddress.IPv4Address(ip_str)
    subnet_mask = ipaddress.IPv4Address(subnet_mask_str)
    network = ipaddress.IPv4Network(f"{ip_str}/{subnet_mask_str}", strict=False)

    first_octet = int(ip_str.split('.')[0])
    if 1 <= first_octet <= 126:
        net_class = 'A'
        default_mask_bits = 8
    elif 128 <= first_octet <= 191:
        net_class = 'B'
        default_mask_bits = 16
    elif 192 <= first_octet <= 223:
        net_class = 'C'
        default_mask_bits = 24
    else:
        net_class = 'Unknown'
        default_mask_bits = 0

    hex_ip = ''.join([f"{int(octet):02X}" for octet in ip_str.split('.')])
    wildcard_mask = '.'.join([str(255 - int(octet)) for octet in subnet_mask_str.split('.')])
    mask_bits = bin(int(subnet_mask)).count('1')
    subnet_bits = max(mask_bits - default_mask_bits, 0)
    max_subnets = 2 ** subnet_bits
    hosts_per_subnet = network.num_addresses - 2
    host_range = f"{list(network.hosts())[0]} - {list(network.hosts())[-1]}"
    subnet_id = network.network_address
    broadcast_address = network.broadcast_address
    subnet_bitmap = f"{'0' * default_mask_bits}{'n' * subnet_bits}{'h' * (32 - mask_bits)}"

    results = {
        "Network Class": net_class,
        "IP Address": ip_str,
        "Hex IP Address": hex_ip,
        "Subnet Mask": subnet_mask_str,
        "Wildcard Mask": wildcard_mask,
        "Subnet Bits": subnet_bits,
        "Mask Bits": mask_bits,
        "Maximum Subnets": max_subnets,
        "Hosts per Subnet": hosts_per_subnet,
        "Host Address Range": host_range,
        "Subnet ID": str(subnet_id),
        "Broadcast Address": str(broadcast_address),
        "Subnet Bitmap": subnet_bitmap
    }

    print(Fore.YELLOW + Style.BRIGHT + "Subnet Calculation Results\n" + "-"*40)
    for key, value in results.items():
        print(f"{Fore.CYAN}{key}: {Fore.GREEN}{value}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Subnet Calculator")
    parser.add_argument("ip", help="IP address (e.g., 192.168.1.1)")
    parser.add_argument("subnet_mask", help="Subnet mask (e.g., 255.255.255.192)")
    args = parser.parse_args()

    subnet_calculator(args.ip, args.subnet_mask)
