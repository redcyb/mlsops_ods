import click
import pandas as pd


@click.command()
@click.argument("input_path", type=click.Path(exists=True))
@click.argument("output_path", type=click.Path())
def _select_region(input_path, output_path):
    select_region(input_path, output_path)


def select_region(input_path, output_path):
    """
    Dummy func to satisfy ods course examples.
    This reads a dataset from json file and dumps into csv.

    :param input_path:
    :param output_path:
    :return:
    """

    df = pd.read_json(input_path)

    df.to_csv(output_path, index=False)


if __name__ == "__main__":
    _select_region()
