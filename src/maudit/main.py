import os
import typer

from maudit.plotting import plot_var_time_series

from maudit.utils import return_dict_of_infd, return_pd_var
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
    lp_pd = return_pd_var(infd_dict, "lp")
    step_size_pd = return_pd_var(infd_dict, "step_size")
    lp_pd_w = return_pd_var(infd_dict, "lp", True)
    step_size_pd_w = return_pd_var(infd_dict, "step_size", True)

    lp_plot = plot_var_time_series(lp_pd, "lp")
    lp_plot.save(filename = 'lp_time_series.png')
    step_size_plot = plot_var_time_series(step_size_pd, "step_size")
    step_size_plot.save(filename = 'step_size_time_series.png')
    lp_plot_w = plot_var_time_series(lp_pd_w, "lp")
    lp_plot_w.save(filename = 'lp_time_series_warmup.png')
    step_size_plot_w = plot_var_time_series(step_size_pd_w, "step_size")
    step_size_plot_w.save(filename = 'step_size_time_series_warmup.png')


if __name__ == "__main__":
    typer.run(main)
