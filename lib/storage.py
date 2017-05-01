import os
import arrow
from tinydb import TinyDB
from tinydb.storages import JSONStorage
from tinydb_serialization import Serializer, SerializationMiddleware
from tinydb import Query

class DateTimeSerializer(Serializer):
    OBJ_CLASS = arrow.arrow.Arrow  # The class this serializer handles

    def encode(self, obj):
        return obj.format('YYYY-MM-DD HH:mm:ss ZZ')

    def decode(self, s):
        return arrow.get(s, 'YYYY-MM-DD HH:mm:ss ZZ')


class Storage(object):

    def __init__(self, database_file):
        serialization = SerializationMiddleware()
        serialization.register_serializer(DateTimeSerializer(), 'ArrowDateTime')

        self.db = TinyDB(database_file, storage=serialization)

    def store_by_mac_address(self, mac_address, data):
        Record = Query()
        result = self.db.search(Record.mac_address == mac_address)

        if not result:
            data.update({
                'last_updated': None,
                'created': arrow.utcnow(),
                'last_ip_change': arrow.utcnow(),
            })
            self.db.insert(data)
        else:
            data.update({'last_updated': arrow.utcnow()})

            if data['ip_address'] != result[0]['ip_address']:
                data.update({'last_ip_change': arrow.utcnow()})

            self.db.update(data, Record.mac_address == mac_address)
