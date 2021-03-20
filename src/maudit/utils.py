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