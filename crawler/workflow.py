import json
from pprint import pprint
from typing import Union

from utils import parse_datetime

from crawler.data import GetData
from crawler.networks import Networks
from crawler.parameters import Parameters
from crawler.stations import Stations
import crawler.config as config


def dump(filename: str, data: Union[list, dict, str]):
    config.create_data_dir()
    with open(filename, "w") as f:
        json.dump(data, f)


def dump_networks():
    print(f"{config.bcolors.UNDERLINE}\nFetching networks...\n{config.bcolors.ENDC}")
    bot = Networks()
    networks = [n.dict() for n in bot.get()]
    pprint(networks)
    dump(config.NETWORKS_FILE, networks)
    print(
        f"\nNetworks dumped to  {config.bcolors.OKGREEN}{config.NETWORKS_FILE}\n{config.bcolors.ENDC}")


def dump_stations(network_id: str):
    print(
        f"\nFetching stations for network {config.bcolors.OKGREEN}{network_id}{config.bcolors.ENDC}...\n"
    )
    bot = Stations(network_id=network_id)
    stations = [s.dict() for s in bot.get()]
    pprint(stations)
    stations_file = config.STATIONS_FILE.format(network_id=network_id)
    dump(stations_file, stations)
    print(
        f"\n Stations dumped to {config.bcolors.OKGREEN}{stations_file}\n{config.bcolors.ENDC}")


def dump_parameters(network_id: str, station_id: str):
    print(
        f"\nFetching parameters for station {config.bcolors.OKGREEN}{station_id}{config.bcolors.ENDC} (from network {config.bcolors.OKGREEN}{network_id}{config.bcolors.ENDC})...\n"
    )
    bot = Parameters(network_id=network_id)
    parameters = [s.dict() for s in bot.get(station_id)]
    parameters_file = config.PARAMETERS_FILE.format(station_id=station_id)
    pprint(parameters)
    dump(parameters_file, parameters)
    print(
        f"\n Parameters dumped to {config.bcolors.OKGREEN}{parameters_file}\n{config.bcolors.ENDC}")


def dump_data(station_uid: str, parameter_uid: str, tmin: str, tmax: str):
    print(
        f"""\nFetching data for 
        parameter {config.bcolors.OKGREEN}{parameter_uid}{config.bcolors.ENDC} 
        station {config.bcolors.OKGREEN}{station_uid}{config.bcolors.ENDC} 
        between {config.bcolors.OKGREEN}{tmin}{config.bcolors.ENDC} and {config.bcolors.OKGREEN}{tmax}{config.bcolors.ENDC}\n
        """
    )
    bot = GetData()
    data = bot.get_data(
        station_uid=station_uid,
        parameter_uid=parameter_uid,
        tmin=parse_datetime(tmin, format="%Y-%m-%d"),
        tmax=parse_datetime(tmax, format="%Y-%m-%d"),
    )
    data_file = config.DATA_FILE.format(
        station_id=station_uid, parameter_id=parameter_uid, tmin=tmin, tmax=tmax
    )
    dump(data_file, data.json())
    print(
        f"\n Data dumped to {config.bcolors.OKGREEN}{data_file}\n{config.bcolors.ENDC}")
