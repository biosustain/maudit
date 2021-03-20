#%%

from plotnine import *
import pandas as pd

def plot_var_time_series(var_df, var_name):
    p = (
        ggplot(var_df, aes(x = 'draw', y = var_name, color = 'factor(chain)'))
        +geom_line()
    )
    return p

#%%
