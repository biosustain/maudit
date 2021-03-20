import os
import re

import plotnine as p9
import arviz as az
import pandas as pd

from maud.analysis import load_infd

def return_dict_of_infd(csvs, mi):
    """Return dict of chain with associated infd object.
    :params csvs: a list of csv file paths
    :params mi: a MaudInput object
    """
    return {
        re.split("\.", re.split('-', chain)[-1])[0]: load_infd(chain, mi)
        for chain in csvs
        }

def return_pd_var(infd_dict: dict(), var_name: str(), WARMUP_TAG: bool() = False):
    """Returns a df of sample stat variable.
    :params infd_dict: a dictionary of infd objects
    :params var_name: a string indicating the variable of interest
    :params WARMUP_TAG: indicator of if warmup draws are of interest
    """
    if WARMUP_TAG is True:
        sample_stats = "warmup_sample_stats"
    else:
        sample_stats = "sample_stats"
    var_dict = {
            chain: idata[sample_stats][var_name].to_series()
            for chain, idata in infd_dict.items()
        }
    var_df = pd.DataFrame(var_dict).droplevel('chain').rename_axis('chain', axis='columns').stack().rename(var_name).reset_index()
    return var_df