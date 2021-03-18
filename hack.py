import os
import arviz as az
from maud.analysis import load_infd
from maud.io import load_maud_input_from_toml

DATA_DIR = (
    "data/example_maud_outputs/maud_output-methionine_cycle-20210308163837/"
)
SAMPLE_FILE = os.path.join(
    DATA_DIR, "samples", "inference_model-202103081638-1.csv"
)
mi = load_maud_input_from_toml(os.path.join(DATA_DIR, "user_input"))
infd = load_infd([SAMPLE_FILE], mi)
infd.to_netcdf("data/example_netcdf.ncdf")
