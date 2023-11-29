# HelenIssues

This script is a small tool used to detect an ongoing or upcoming Helen district heating maintenance window on a specified geolocation. The information originates from Helen's API which their [browser interface](https://www.helen.fi/ajankohtaista/jakelukeskeytykset) to see the maintenance windows uses.

## Motivation

Motivation to create this rose when one morning I almost had a cold shower and I figured out that the district heating was cut off without any kind of a prior notice to me.

## Usage

Simply input your coordinates of interest in the config.py file based on the sample and run the script, and also create an application token in Pushover to receive notifications and insert also your user token for Pushover. The requirements.txt contains the necessary dependencies. As usual, it is recommended to run this in a venv to prevent messing up the local Python installation.

### Running in cron

Running this in cron could be achieved by the following entry. Considering 5 am would be an optimal time to run this script:

`0 5 * * * /path/to/VENV/bin/python /path/to/your_script.py >/dev/null 2>&1`

## Known issues

In tightly packed districts there is a small chance that checking a GPS coordinate against provided GeoJSON bounding box instead of a Polygon/Multipolygon. However due to how the API provides the different kinds of polygons, a bounding box is instead preferred.