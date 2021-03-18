import os
from pathlib import Path
import typer


def main(path_to_output_dir: Path):
    """Run maudit: this is the main entrypoint.

    :param path_to_output_dir: Path to a directory that was created by maud to
    store output files.

    """
    samples_dir = os.path.join(path_to_output_dir, "samples")
    csvs = [f for f in os.listdir(samples_dir) if f.endswith("csv")]
    typer.echo(f"Reading data from {path_to_output_dir}")
    typer.echo(f"Found csv files: {csvs}")


if __name__ == "__main__":
    typer.run(main)
