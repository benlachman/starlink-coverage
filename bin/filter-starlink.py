import re


active_sats = open("active.txt").read()

regex = r"^STARLINK-\d+.*\n1.*\n2.*$"

starlinks = re.findall(regex, active_sats, re.MULTILINE)

print(len(starlinks))

out = "\n".join(starlinks)

with open('starlink-data.txt', 'w') as f:
  f.write(out)
