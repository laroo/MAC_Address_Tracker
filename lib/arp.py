import re
from subprocess import Popen, PIPE


def parse_arp_line(arp_line):
    mac_address_match = re.search(r'([0-9A-F]{1,2}[:-]){5}([0-9A-F]{1,2})', arp_line, re.IGNORECASE)
    mac_address = mac_address_match.group() if mac_address_match else None

    ip_address_match = re.search(r'((2[0-5]|1[0-9]|[0-9])?[0-9]\.){3}((2[0-5]|1[0-9]|[0-9])?[0-9])', arp_line, re.IGNORECASE)
    ip_address = ip_address_match.group() if ip_address_match else None

    interface_match = re.search(r' on (.*)$', arp_line)
    interface = interface_match.group(1) if interface_match else None

    return {
        'mac_address': format_mac_address(mac_address),
        'ip_address': ip_address,
        'interface': interface,
    }

def get_arp_table():
    pid = Popen(["arp", "-a"], stdout=PIPE)
    output = pid.communicate()[0]

    arp_table = []
    for line in output.splitlines():
        arp = parse_arp_line(line)
        if not arp.get('mac_address'):
            continue
        arp_table.append(arp)

    return arp_table

def format_mac_address(input_mac):
    parts = input_mac.lower().split(':')

    for idx, part in enumerate(parts):
        if len(part) == 1:
            parts[idx] = '0{}'.format(part)

    return ":".join(parts)
