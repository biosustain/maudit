#%%
import arviz
from plotnine import *

#%%

dat_ncdf = arviz.from_netcdf('../../data/example_netcdf.ncdf')
# %%

def plot_var_time_series(ncdf, var_name):
    lp_df = ncdf.sample_stats[var_name].to_dataframe()
    p = (
        ggplot(lp_df.reset_index(), aes(x = 'draw', y = var_name, col = 'chain'))
        +geom_line()
    )
    return p

#%%
plot_var_time_series(dat_ncdf, 'n_steps')