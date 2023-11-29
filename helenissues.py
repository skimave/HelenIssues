import json
import requests
import math
from shapely.geometry import Point, box
from datetime import datetime, timedelta
import urllib.parse
from config import longitude, latitude, pushover_token, pushover_user


def send_pushover_notification(maintenance_data):
    url = "https://api.pushover.net/1/messages.json"
    payload = {
        "token": pushover_token,
        "user": pushover_user,
        "message": maintenance_data
    }
    headers = {
        "Content-Type": "application/x-www-form-urlencoded"
    }
    response = requests.post(url, data=payload, headers=headers)

def is_today_between(start_date, end_date):
    current_date = datetime.now().date()
    tomorrow_date = current_date + timedelta(days=1)
    start_date = datetime.strptime(start_date, "%d.%m.%Y").date()
    end_date = datetime.strptime(end_date, "%d.%m.%Y").date()

    if start_date <= current_date <= end_date:
        return "Today there will be a remote heating maintenance in your area."
    if start_date <= tomorrow_date <= end_date:
        return "Tomorrow there will be a remote heating maintenance in your area."

def get_disruptions():
    url = 'https://www.helen.fi/mapapi/disruptions'
    r = requests.get(url)
    disruptions = json.loads(r.text)
    features = disruptions['features']
    return features


def main():
    features = get_disruptions()
    for feature in features:
        point = Point(latitude, longitude)
        geometry = feature['geometry']
        bbox_coordinates = geometry['bbox']
        pagelink = 'https://www.helen.fi/' + feature['properties']['pageLink']
        pagelink = urllib.parse.quote(pagelink, safe=':/?&=')
        #Splitting for the convenience because sometimes the timestamp from Helen is included and sometimes it isn't
        startdate = feature['properties']['startDate'].split(' ')[0]
        enddate = feature['properties']['endDate'].split(' ')[0]

        #Note: tuple unpacking with *
        bbox = box(*bbox_coordinates)
        is_contained = bbox.contains(point)

        if bbox.contains(point):
            maintenance_data = is_today_between(startdate, enddate)
            if maintenance_data is not None:
                maintenance_data = maintenance_data + "\n Check for details: {pagelink}".format(pagelink=pagelink)
                send_pushover_notification(maintenance_data)

if __name__ == "__main__":
    main()
