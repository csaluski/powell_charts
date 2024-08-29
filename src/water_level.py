import plotly.express as px
import pandas as pd

import json
import requests

sources = json.load(open('../sources.json'))
r = requests.get(sources[0]['source_url'])

from io import StringIO
string = StringIO(r.text)
tab = pd.read_csv(string,parse_dates=['datetime']) 

fig = px.line(tab, x="datetime", y="pool elevation", title='Lake Powell Pool Elevation')
# fig.show()

fig.write_html("water_level.html")