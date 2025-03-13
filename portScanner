import socket
import argparse

def scan_port(target, port):
    """Scans a specific port on the target machine."""
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(1)
        result = s.connect_ex((target, port))

        if result == 0:
            print(f"[+] Port {port} is OPEN")
        s.close()
    except socket.error:
        print("[!] Unable to connect to the target.")

def scan_ports(target, start_port, end_port):
    """Scans a range of ports on the target machine."""
    print(f"\n[Scanning {target} from port {start_port} to {end_port}]\n")
    for port in range(start_port, end_port + 1):
        scan_port(target, port)

def main():
    parser = argparse.ArgumentParser(description="Python Port Scanner")
    parser.add_argument("target", help="Target IP or domain")
    parser.add_argument("start_port", type=int, help="Start port")
    parser.add_argument("end_port", type=int, help="End port")
    args = parser.parse_args()

    scan_ports(args.target, args.start_port, args.end_port)

if __name__ == "__main__":
    main()
