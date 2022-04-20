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
        f"\nNetworks dumped to  {config.bcolors.OKGREEN}{config.NETWORKS_FILE}\n{config.bcolors.ENDC}"
    )


def dump_stations(network_uid: str):
    print(
        f"\nFetching stations for network {config.bcolors.OKGREEN}{network_uid}{config.bcolors.ENDC}...\n"
    )
    bot = Stations(network_uid=network_uid)
    stations = [s.dict() for s in bot.get()]
    pprint(stations)
    stations_file = config.STATIONS_FILE.format(network_uid=network_uid)
    dump(stations_file, stations)
    print(
        f"\n Stations dumped to {config.bcolors.OKGREEN}{stations_file}\n{config.bcolors.ENDC}"
    )


def dump_parameters(network_uid: str, station_uids: list[str]):
    stations_rep = ",".join(station_uids)
    print(
        f"\nFetching parameters for station(s) {config.bcolors.OKGREEN}{stations_rep}{config.bcolors.ENDC} (from network {config.bcolors.OKGREEN}{network_uid}{config.bcolors.ENDC})...\n"
    )
    bot = Parameters(network_uid=network_uid)
    parameters = [s.dict() for s in bot.get(station_uids)]
    parameters_file = config.PARAMETERS_FILE.format(stations=stations_rep)
    pprint(parameters)
    dump(parameters_file, parameters)
    print(
        f"\n Parameters dumped to {config.bcolors.OKGREEN}{parameters_file}\n{config.bcolors.ENDC}"
    )


def dump_data(station_uids: list[str], parameter_uids: list[str], tmin: str, tmax: str):
    stations_rep = ",".join(station_uids)
    parameters_rep = ",".join(parameter_uids)
    print(stations_rep)
    print(
        f"""\nFetching data for 
        station(s) {config.bcolors.OKGREEN}{stations_rep}{config.bcolors.ENDC} 
        parameter(s) {config.bcolors.OKGREEN}{parameters_rep}{config.bcolors.ENDC} 
        between {config.bcolors.OKGREEN}{tmin}{config.bcolors.ENDC} and {config.bcolors.OKGREEN}{tmax}{config.bcolors.ENDC}\n
        """
    )
    bot = GetData()
    data = bot.get_data(
        station_uids=station_uids,
        parameter_uids=parameter_uids,
        tmin=parse_datetime(tmin, format="%Y-%m-%d"),
        tmax=parse_datetime(tmax, format="%Y-%m-%d"),
    )
    data_file = config.DATA_FILE.format(
        stations=stations_rep, parameters=parameters_rep, tmin=tmin, tmax=tmax
    )
    dump(data_file, data.json())
    print(
        f"\n Data dumped to {config.bcolors.OKGREEN}{data_file}\n{config.bcolors.ENDC}"
    )
