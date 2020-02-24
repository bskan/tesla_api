from tesla_api import TeslaApiClient

client = TeslaApiClient('MY-USERNAME', 'MY-PASSWORD')

energy_sites = client.list_energy_sites()
print("Number of energy sites = %d" % (len(energy_sites)))
assert(len(energy_sites)==1)
print energy_sites[0]

energy_sites[0].set_operating_mode('autonomous')

import json

start = '1800'
finish = '16200'

settings = '{Content-Type: application/json}\n'
settings = '{"tou_settings":{"optimization_strategy": "economics", "schedule":['
settings = settings + '{"end_seconds": ' + finish + ', "week_days": [6, 0], "target": "off_peak", "start_seconds": ' + start + '},'
settings = settings + '{"end_seconds": ' + start +', "week_days": [6, 0], "target": "peak", "start_seconds": ' + finish + '},'
settings = settings + '{"end_seconds": ' + finish + ', "week_days": [1, 2, 3, 4, 5], "target": "off_peak", "start_seconds": ' + start+ '},'
settings = settings + '{"end_seconds": ' + start + ', "week_days": [1, 2, 3, 4, 5], "target": "peak", "start_seconds": ' + finish + '}]}}'


jsonsettings = json.loads(settings)

energy_sites[0].set_tou_settings(jsonsettings)

