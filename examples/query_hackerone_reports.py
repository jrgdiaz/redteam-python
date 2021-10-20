from redteam import RedTeam

x = RedTeam()
query = "Manage Engine"
hits = x.googledork("site: hackerone.com -site:docs.hackerone.com inurl:reports "+query,60)
for hit in hits:
        response = requests.get(hit)
        print(hit)
