"""
pygnmi script
"""

from pygnmi.client import gNMIclient

TELEMETRY_REQUEST1 = {
                        'subscription': [
                            {
                                'path': 'openconfig:/interfaces/interface[name=Ethernet2]/state/counters',
                                'mode': 'target_defined'
                            }
                        ],
                        'mode': 'once',
                        'encoding': 'proto'
                    }

# For snapshot_time
EXTENSION1 = {
                'history': {
                    'snapshot_time': '2022-07-24T8:57:00Z'
                }
            }

with open("token.tok") as f:
    TOKEN = f.read().strip('\n')

with gNMIclient(target=('192.168.0.5', '443'), token=TOKEN, skip_verify=True) as gconn:
    for item in gconn.subscribe2(subscribe=TELEMETRY_REQUEST1, target="leaf1", extension=EXTENSION1):
        print(item)

