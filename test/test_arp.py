
from lib.arp import parse_arp_line

def test_arp_parse():

    # Linux (Ubuntu 14.04)
    # ? (172.17.2.129) at c4:b3:01:b1:95:ee [ether] on eth1
    # ? (172.17.2.107) at 00:25:64:8a:00:d1 [ether] on eth1
    # ? (172.17.2.166) at 18:65:90:54:56:d9 [ether] on eth1
    # ? (172.17.2.109) at 00:1d:aa:9f:0b:ac [ether] on eth1
    # ? (172.17.2.184) at 48:5a:b6:74:6f:af [ether] on eth1
    # ? (172.17.2.2) at <incomplete> on eth1
    # ? (172.17.2.118) at 7c:04:d0:d5:45:86 [ether] on eth1

    # macOS (Sierra)
    # ? (192.168.192.1) at 20:d5:bf:1f:e1:57 on en0 ifscope [ethernet]
    # ? (192.168.192.20) at 0:11:32:5d:ab:6b on en0 ifscope [ethernet]
    # ? (192.168.192.100) at 20:d5:bf:1f:e1:5a on en0 ifscope [ethernet]
    # ? (224.0.0.251) at 1:0:5e:0:0:fb on en0 ifscope permanent [ethernet]
    # ? (239.255.255.250) at 1:0:5e:7f:ff:fa on en0 ifscope permanent [ethernet]


    test_arp_lines = [
        '? (172.17.2.129) at c4:b3:01:b1:95:ee [ether] on eth1',
        '? (172.17.2.107) at 00:25:64:8a:00:d1 [ether] on eth1',
        '? (172.17.2.166) at 18:65:90:54:56:d9 [ether] on eth1',
        '? (172.17.2.109) at 00:1d:aa:9f:0b:ac [ether] on eth1',
        '? (172.17.2.184) at 48:5a:b6:74:6f:af [ether] on eth1',
        '? (172.17.2.2) at <incomplete> on eth1',
        '? (172.17.2.118) at 7c:04:d0:d5:45:86 [ether] on eth1',
        '? (192.168.192.1) at 20:d5:bf:1f:e1:57 on en0 ifscope [ethernet]',
        '? (192.168.192.20) at 0:11:32:5d:ab:6b on en0 ifscope [ethernet]',
        '? (192.168.192.100) at 20:d5:bf:1f:e1:5a on en0 ifscope [ethernet]',
        '? (224.0.0.251) at 1:0:5e:0:0:fb on en0 ifscope permanent [ethernet]',
        '? (239.255.255.250) at 1:0:5e:7f:ff:fa on en0 ifscope permanent [ethernet]',
    ]

    for line in test_arp_lines:
        arp = parse_arp_line(line)
        print arp
