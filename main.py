import csv
import pygal.maps.world
from pygal.style import RotateStyle
from pygal.maps.world import COUNTRIES


file = 'GDP_percapita_worldwide.csv'
with open(file) as f:
    reader = csv.reader(f)
    full_data = next(reader)
header_row = []
for i in range(len(full_data)):
    if '\n' in full_data[i]:
        header_row = full_data[:i]
        break
data = []
for i in range(len(header_row), len(full_data) - len(header_row)):
    if i % len(header_row) == 0 and full_data[i + len(header_row) - 1][:-2]:
        data.append({
            'country': full_data[i],
            'code': full_data[i + 1],
            'gdp': float(full_data[i + len(header_row) - 1][:-2])
        })
data_mod = {}
for country_key in COUNTRIES.keys():
    for i in range(len(data)):
        if COUNTRIES[country_key].title() in data[i]['country'].title():
            data_mod[country_key] = data[i]['gdp']

wm_style = RotateStyle('#336699')
worldmap_chart = pygal.maps.world.World(style=wm_style)
worldmap_chart.title = 'Worldwide GDP per capita in 2021'
worldmap_chart.add('GDP per capita 2021', data_mod)
worldmap_chart.render_to_file('Worldwide GDP per capita.svg')





