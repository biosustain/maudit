import os
import typer

from .utils import return_dict_of_infd
from pathlib import Path
from maud.io import load_maud_input_from_toml

app = typer.Typer()


@app.command()
def main(path_to_output_dir: Path):
    """Run maudit: this is the main entrypoint.

    :param path_to_output_dir: Path to a directory that was created by maud to
    store output files.

    """
    ui_path = os.path.join(path_to_output_dir, "user_input")
    samples_dir = os.path.join(path_to_output_dir, "samples")
    csvs = [
        os.path.join(samples_dir, f)
        for f in os.listdir(samples_dir)
        if f.endswith("csv")
    ]
    typer.echo(f"Reading data from {path_to_output_dir}")
    typer.echo(f"Found csv files: {csvs}")
    mi = load_maud_input_from_toml(ui_path)
    infd_dict = return_dict_of_infd(csvs, mi)
    print(infd_dict)


if __name__ == "__main__":
    typer.run(main)
