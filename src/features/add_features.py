import click
import pandas as pd


@click.command()
@click.argument("input_path", type=click.Path(exists=True))
@click.argument("output_path", type=click.Path())
def _add_features(input_path, output_path):
    add_features(input_path, output_path)


def add_features(input_path, output_path):
    """
    Dummy func to satisfy ods course examples
    :return:
    """
    df = pd.read_csv(input_path)

    df["col3"] = df["col1"] + df["col2"]

    df.to_csv(output_path, index=False)


if __name__ == "__main__":
    _add_features()
