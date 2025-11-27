import requests, os, sys

USER = os.environ.get("GH_USER", "ltpzxgit")
OUT = "bunny-runner.svg"

url = f"https://github.com/users/{USER}/contributions"
r = requests.get(url)

if r.status_code != 200:
    sys.exit("fetch failed")

svg = r.text

bunny = '''
<g id="rabbit" transform="translate(12,12)">
  <ellipse cx="10" cy="12" rx="6" ry="4" fill="#0af"/>
  <rect x="7" y="5" width="3" height="7" fill="#0af"/>
  <rect x="10" y="5" width="3" height="7" fill="#0af"/>
  <circle cx="9" cy="12" r="1.5" fill="#000"/>
</g>
'''

new = svg.replace("</svg>", bunny + "</svg>")
open(OUT, "w", encoding="utf-8").write(new)

print("ok:", OUT)
