import json
from argparse import ArgumentParser
from pathlib import Path

from doci.bot import Doci


def main():
    parser = ArgumentParser()
    parser.add_argument(
        "-c", "--config", type=Path, default=Path("config.json")
    )
    options = parser.parse_args()

    with options.config.open() as f:
        config = json.load(f)

    doci = Doci()
    doci.load_extensions()
    doci.run(config["token"])


if __name__ == "__main__":
    main()
