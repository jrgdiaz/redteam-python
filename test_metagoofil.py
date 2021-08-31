from redteam import RedTeam
from datetime import datetime
domain = 'example.org'
x = RedTeam(domain)
x.metagoofil('example.org',60.0, download_files=True)
