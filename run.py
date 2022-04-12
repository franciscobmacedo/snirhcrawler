import argparse
import crawler.workflow as workflow


class CrawlerType:
    networks = "networks"
    stations = "stations"
    parameters = "parameters"
    data = "data"


class Run:
    def __init__(self) -> None:
        self.parser = argparse.ArgumentParser(description="snirh crawler.")

        self.parser.add_argument(
            "CrawlerType",
            metavar="crawler_type",
            type=str,
            help='set the crawler type: "networks", "stations" or "parameters"',
            choices=[
                CrawlerType.networks,
                CrawlerType.stations,
                CrawlerType.parameters,
                CrawlerType.data,
            ],
        )
        args, _ = self.parser.parse_known_args()

        if args.CrawlerType == CrawlerType.networks:
            workflow.dump_networks()
        elif args.CrawlerType == CrawlerType.data:
            self.add_station_arg()
            self.add_param_arg()
            self.add_tmin_arg()
            self.add_tmax_arg()
            args = self.parser.parse_args()
            workflow.dump_data(args.station, args.parameter, args.tmin, args.tmax)

        else:
            self.add_network_arg()
            if args.CrawlerType == CrawlerType.stations:
                args = self.parser.parse_args()
                workflow.dump_stations(args.network)

            if args.CrawlerType == CrawlerType.parameters:
                self.add_station_arg()
                args = self.parser.parse_args()
                workflow.dump_parameters(args.network, args.station)

    def add_network_arg(self):
        self.parser.add_argument("-n", "--network", help="network id", required=True)

    def add_station_arg(self):
        self.parser.add_argument("-s", "--station", help="station id", required=True)

    def add_param_arg(self):
        self.parser.add_argument(
            "-p", "--parameter", help="parameter id", required=True
        )

    def add_tmin_arg(self):
        self.parser.add_argument(
            "-f", "--tmin", help="from tmin (format 'yyyy-mm-dd')", required=True
        )

    def add_tmax_arg(self):
        self.parser.add_argument(
            "-t", "--tmax", help="to tmax (format 'yyyy-mm-dd')", required=True
        )


if __name__ == "__main__":
    Run()
