import os
from lib.arp import get_arp_table
from lib.storage import Storage

print('[start]')

current_dir = os.path.dirname(os.path.abspath(__file__))
database_file = '{}/db.json'.format(current_dir)
storage = Storage(database_file)

arp_table = get_arp_table()
for arp_record in arp_table:
    storage.store_by_mac_address(arp_record['mac_address'], arp_record)

print('-'*130)
print('{:<24}{:<24}{:<30}{:<30}{:<30}'.format(
    'mac_address',
    'ip_address',
    'created',
    'last_updated',
    'last_ip_change',
))
print('-'*130)
for row in storage.db.all():
    print('{:<24}{:<24}{:<30}{:<30}{:<30}'.format(
        row['mac_address'],
        row['ip_address'],
        row['created'].format('YYYY-MM-DD HH:mm:ss') if row['created'] else None,
        row['last_updated'].format('YYYY-MM-DD HH:mm:ss') if row['last_updated'] else None,
        row['last_ip_change'].format('YYYY-MM-DD HH:mm:ss') if row['last_ip_change'] else None,
    ))
print('-'*130)

print('[done]')