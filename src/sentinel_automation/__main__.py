"""Command-line interface."""
import fire

from .automation import Automation


def main():
    """Main entry point for the command line interface of sentinel-automation."""
    fire.Fire(Automation)


if __name__ == "__main__":
    main()
