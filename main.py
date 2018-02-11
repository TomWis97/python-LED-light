import pygatt
import datetime
import configparser
from astral import Astral

def getSunset(city):
    return Astral()[city].sun()['sunset']

if __name__ == '__main__':
    config = configparser.ConfigParser()
    config.read('settings.ini')
    print(config['general'])
