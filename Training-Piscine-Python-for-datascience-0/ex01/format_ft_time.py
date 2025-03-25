# Ressource
# https://www.programiz.com/python-programming/datetime/strftime

from datetime import datetime

dt = datetime.now()
ts = datetime.timestamp(dt)

def format_timestamp(ts):
    return f"{ts:,.4f}"

def format_scientic(ts):
    return f"{ts:0.2e}"

formatted_ts = format_timestamp(ts)
scientific_ts = format_scientic(ts)

# Using utils function
print(f"Seconds since {datetime(1970, 1, 1).strftime('%b %-d, %Y')}: {format_timestamp(ts)} or {format_scientic(ts)} in scientific notation")

# One liner
# print(f"Seconds since {datetime(1970, 1, 1).strftime('%b %-d, %Y')}: {datetime.timestamp(datetime.now()):,.4f} or {datetime.timestamp(datetime.now()):0.2e} in scientific notation")
