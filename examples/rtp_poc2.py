#proof of concept script to download document files using OSINT module
#Extract metadata with: exiftool -r * | egrep -i "Author|Creator|Email|Producer|Template" | sort -u

from redteam import RedTeam
x = RedTeam()
x.metagoofil('example.org',60.0, download_files=True)
