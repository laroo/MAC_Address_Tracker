# MAC Address Tracker

Uses `arp` to extract MAC address & IP to find machines on your local network and stores the result in a JSON file database

## Installation

create virtual environment (optional)

Install dependencies `pip install -r requirements.txt`

## Running

Run `python mac_address_tracker.py`

Output `db.json`:

```
----------------------------------------------------------------------------------------------------------------------------------
mac_address             ip_address              created                       last_updated                  last_ip_change
----------------------------------------------------------------------------------------------------------------------------------
00:1a:10:ab:ab:ab       192.168.192.1           2017-05-01 23:22:26           None                          2017-05-01 23:22:26
00:1b:11:00:00:00       192.168.192.180         2017-05-01 23:22:26           None                          2017-05-01 23:22:26
01:1c:12:11:11:11       192.168.192.181         2017-05-01 23:22:26           2017-05-01 23:41:14           2017-05-01 23:41:14
01:1d:13:7f:7f:7f       192.168.192.182         2017-05-01 23:22:26           2017-05-01 23:41:14           2017-05-01 23:22:26
----------------------------------------------------------------------------------------------------------------------------------
```
