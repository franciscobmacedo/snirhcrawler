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
            self.add_stations_arg()
            self.add_params_arg()
            self.add_tmin_arg()
            self.add_tmax_arg()
            args = self.parser.parse_args()
            print(args.stations)
            workflow.dump_data(
                station_uids=args.stations,
                parameter_uids=args.parameters,
                tmin=args.tmin,
                tmax=args.tmax,
            )

        else:
            self.add_network_arg()
            if args.CrawlerType == CrawlerType.stations:
                args = self.parser.parse_args()
                workflow.dump_stations(args.network)

            if args.CrawlerType == CrawlerType.parameters:
                self.add_stations_arg()
                args = self.parser.parse_args()
                workflow.dump_parameters(args.network, args.stations)

    def add_network_arg(self):
        self.parser.add_argument("-n", "--network", help="network id", required=True)

    def add_stations_arg(self):
        self.parser.add_argument(
            "-s", "--stations", nargs="+", help="station id", required=True
        )

    def add_params_arg(self):
        self.parser.add_argument(
            "-p", "--parameters", help="parameter id", nargs="+", required=True
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
