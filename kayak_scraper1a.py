import json
import requests
import pandas as pd
import calendar
from datetime import datetime
from time import gmtime, strftime

# https://github.com/rafabelokurows/scraping-kayak

def scrape_kayak():
    """
    This function scrapes flight information from the kayak explore page.
    Parameters:
    start, end, airport - integer representing earliest possible departure date
    in YYYYMMDD format, integer representing latest return date, string with
    three letter code for starting airport. When both are start and end are
    left blank, results are returned from present date to one year in the
    future.
    Returns:
    df - a data frame containing all destination cities and corresponding
    flight information returned by the scrape
    """

    # Format the beginning and end dates to insert them into the URL
    # start = '&depart=' + str(start)
    # end = '&return=' + str(end)
    # "https://www.kayak.pt/s/horizon/exploreapi/destinations?airport=OPO&budget=&depart=20230601&return=20230630&tripdurationrange=4%2C7&duration=&flightMaxStops=&stopsFilterActive=false&topRightLat=51.82490080841914&topRightLon=8.962652968749989&bottomLeftLat=28.636584579286538&bottomLeftLon=-26.32543296874999&zoomLevel=5&selectedMarker=&themeCode=&selectedDestination="

    url = 'https://www.kayak.com/flights/EWR-DEN/2024-01-26/2024-01-29?sort=price_a'

    response = requests.post(url).json()


    for i in range(len(response['destinations'])):
        destination = response['destinations'][i]
        row = list([destination['city']['name'], destination['country']['name'],
                    destination['flightMaxDuration'],
                    destination['flightInfo']['price'], destination['airline'],
                    destination['airport']['shortName'], pd.to_datetime(destination['departd']).date(),
                    pd.to_datetime(destination['returnd']).date(),
                    str('http://kayak.com' + destination['clickoutUrl'])])

scrape_kayak()


