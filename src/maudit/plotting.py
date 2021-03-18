#%%

from plotnine import *
import pandas as pd

def plot_var_time_series(dict_of_idata):
    lp_df = pd.DataFrame({
        chain: idata.sample_stats["lp"].to_series()
        for chain, idata in dict_of_idata.items()
    }).droplevel('chain').rename_axis('chain', axis='columns').stack().rename('lp').reset_index()   
    p = (
        ggplot(lp_df, aes(x = 'draw', y = 'lp', color = 'factor(chain)'))
        +geom_line()
    )
    return p

#%%
