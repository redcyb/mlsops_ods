import click
import pandas as pd


@click.command()
@click.argument("input_path", type=click.Path(exists=True))
@click.argument("output_path", type=click.Path())
def _clean_data(input_path, output_path):
    clean_data(input_path, output_path)


def clean_data(input_path, output_path):
    """
    Dummy func to satisfy ods course examples

    :param input_path:
    :param output_path:
    :return:
    """

    df = pd.read_csv(input_path, header="infer")

    df = df.apply(lambda row: row * 10, axis=1)

    df.to_csv(output_path, index=False)


if __name__ == "__main__":
    _clean_data()
