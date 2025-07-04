import matplotlib.pyplot as plt
import numpy as np

from matplotlib.widgets import Button, Slider
import requests
import datetime




# Fetch data from the API
response = requests.get(
    "https://api.dp.la/v2/items?q=Minnesota+AND+parks&page_size=50&page=2&api_key=73d36b254495172e23eb84f3343ff7cf"
)
data = response.json()

# Extract dates and titles
items = data.get("docs", [])
dates = []
titles = []
for item in items:
    date_str = item.get("sourceResource", {}).get("date", [{}])[0].get("begin")
    title = item.get("sourceResource", {}).get("title", "No Title")
    if date_str:
        try:
            date = int(date_str)
            dates.append(date)
            titles.append(title)
        except ValueError:
            continue

if not dates:
    dates = [2000]
    titles = ["No Data"]

# Sort by date
sorted_items = sorted(zip(dates, titles))
dates, titles = zip(*sorted_items)

# Create slider for date
fig, ax = plt.subplots()
plt.subplots_adjust(bottom=0.25)
text = ax.text(0.5, 0.5, f"{dates[0]}: {titles[0]}", ha='center', va='center', wrap=True)
ax.axis('off')

axdate = fig.add_axes([0.25, 0.1, 0.65, 0.03])
date_slider = Slider(
    ax=axdate,
    label='Date',
    valmin=0,
    valmax=len(dates) - 1,
    valinit=0,
    valstep=1
)

def update(val):
    idx = int(date_slider.val)
    text.set_text(f"{dates[idx]}: {titles[idx]}")
    fig.canvas.draw_idle()

date_slider.on_changed(update)

