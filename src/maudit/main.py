import os

from utils import return_dict_of_infd

import pandas as pd

from maud.io import load_maud_input_from_toml

HERE = os.path.dirname(os.path.abspath(__file__))
PATHS = {
    "MAUD_OUTPUT": "../../data/example_maud_outputs/maud_output-methionine_cycle-20210308163837"
}

def main():
    MAUD = os.path.join(HERE, PATHS["MAUD_OUTPUT"], "samples")
    ui_path = os.path.join(HERE, PATHS["MAUD_OUTPUT"], "user_input")
    mi = load_maud_input_from_toml(ui_path)
    csvs = [
        os.path.join(HERE, PATHS["MAUD_OUTPUT"], "samples", f)
        for f in os.listdir(os.path.join(HERE, PATHS["MAUD_OUTPUT"], "samples"))
        if f.endswith(".csv")
    ]
    infd_dict = return_dict_of_infd(csvs, mi)

    print(infd_dict)

    return

if __name__ == "__main__":
    main()