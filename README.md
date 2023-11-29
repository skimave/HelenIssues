# HelenIssues

This script is a small tool used to detect an ongoing or upcoming Helen district heating maintenance window on a specified geolocation. The information originates from Helen's API which their [browser interface](https://www.helen.fi/ajankohtaista/jakelukeskeytykset) to see the maintenance windows uses.

## Motivation

Motivation to create this rose when one morning I almost had a cold shower and I figured out that the district heating was cut off without any kind of a prior notice to me.

## Usage

Simply input your coordinates of interest in the config.py file based on the sample and run the script.

## TODO

Adding support to Pushover so the script may run with cron daily and notifications could be received automatically.

## Known issues

In tightly packed districts there is a small chance that checking a GPS coordinate against provided GeoJSON bounding box instead of a Polygon/Multipolygon. However due to how the API provides the different kinds of polygons, a bounding box is instead preferred.