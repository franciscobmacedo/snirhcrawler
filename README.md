# :sweat_drops: SNIRH crawler

Forked from [https://github.com/franciscobmacedo/snirhcrawler](franciscobmacedo/snirhcrawler)

Crawler to fetch data from SNIRH


## What is SNIRH?

[SNIRH](https://snirh.apambiente.pt/) (Sistema Nacional de Informação de Recursos Hídricos - National Information System for Water Resources) is a website built in the mid90s that gives access to all sorts of water resources data accross Portugal. It had little to no updates in the last 30 years.

## Motivation

- The user interface is pretty old and hard to get multiple station's data.
- Provide access to the data in an easy and standard format, through a python crawler.

### Setup

_WINDOWS_

```bash
git clone https://github.com/uematsusoft/snirhcrawler
cd  snirhcrawler
py -m venv venv
.\venv\scripts\activate
pip install -r requirements.txt # or requirements/dev.txt for development
```

_MAC/LINUX_

```bash
git clone https://github.com/uematsusoft/snirhcrawler
cd  snirhcrawler
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt # or requirements/dev.txt for development
```

### Run

The crawler accepts multiple commands that will print the data and write it to a `.json` file

```
# all networks
python3 run.py networks

# all stations for a network_uid
python3 run.py stations -n {network_uid}

# all params of a station_uid from a network_uid
python3 run.py params -n {network_uid} -s {station_uid}

# data for a parameter_uid of a station_uid from tmin (yyyy-mm-dd) to tmax (yyyy-mm-dd)
python3 run.py data -s {station_uid} -p {parameter_uid} -f {tmin} -t {tmax}
```

#### Examples

Get all networks - writes it in `data/networks.json`

```
python3 run.py networks
```

Get all stations of the network 920123705 - writes it in `data/stations-network_920123705.json`

```
python3 run.py stations -n 920123705
```

Get all parameters of the station 1627758916 inside the network 920123705 - writes it in `data/parameters-station_1627758916.json`

```
python3 run.py parameters -n 920123705 -s 1627758916
```

Get data for parameter 1849 of the station 1627758916 between 1980-01-01 and 2020-12-31 - writes it in `data/data-station_1627758916-parameter_1849-tmin_1980-01-01-tmax_2020-12-31.json`

```
python3 run.py data -s 1627758916 -p 1849 -f 1980-01-01 -t 2020-12-31
```

Get data for multiple parameters (4237, 1436794570) and multiple stations (920752570, 920752670) between 1930-01-01 and 2020-12-31 - writes it in
Get data for parameter 1849 of the station 1627758916 between 1980-01-01 and 2020-12-31 - writes it in `data/data-stations_920752570,920752670-parameters_4237,1436794570-tmin_1930-01-01-tmax_2020-12-31.json`

```
python3 run.py data -s 920752570 920752670 -p 4237 1436794570 -f 1930-01-01 -t 2020-12-31
```
