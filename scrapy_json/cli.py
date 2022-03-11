"""Console script for scrapy_json."""
import sys
import click


@click.command()
def main(args=None):
    """Console script for scrapy_json."""
    click.echo("Replace this message by putting your code into "
               "scrapy_json.cli.main")
    click.echo("See click documentation at https://click.palletsprojects.com/")
    return 0


if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover
