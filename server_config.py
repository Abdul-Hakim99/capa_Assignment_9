#! /usr/bin/python3

import os

def configure_network_static(ip_address, netmask, gateway, dns):
    try:
        with open('/etc/network/interfaces', 'w') as interfaces_file:
            interfaces_file.write(f"auto lo\niface lo inet loopback\n\n")
            interfaces_file.write(f"auto eth0\niface eth0 inet static\n")
            interfaces_file.write(f"address {ip_address}\n")
            interfaces_file.write(f"netmask {netmask}\n")
            interfaces_file.write(f"gateway {gateway}\n")
            interfaces_file.write(f"dns-nameservers {dns}\n")
        os.system('service networking restart')
        print("Network configuration set to static.")
    except Exception as e:
        print(f"Error: {e}")

def configure_network_dynamic():
    try:
        with open('/etc/network/interfaces', 'w') as interfaces_file:
            interfaces_file.write(f"auto lo\niface lo inet loopback\n")
            interfaces_file.write(f"auto eth0\niface eth0 inet dhcp\n")
        os.system('service networking restart')
        print("Network configuration set to dynamic (DHCP).")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    try:
        if os.geteuid() != 0:
            print("Please run this script with root privileges.")
        else:
            choice = input("Enter 's' to set static IP or 'd' to set dynamic IP: ")
            if choice.lower() == 's':
                ip_address = input("Enter IP address: ")
                netmask = input("Enter netmask: ")
                gateway = input("Enter gateway: ")
                dns = input("Enter DNS server: ")
                configure_network_static(ip_address, netmask, gateway, dns)
            elif choice.lower() == 'd':
                configure_network_dynamic()
            else:
                print("Invalid choice. Please enter 's' for static or 'd' for dynamic.")
    except KeyboardInterrupt:
        print("\nOperation aborted.")
    except Exception as e:
        print(f"Error: {e}")

