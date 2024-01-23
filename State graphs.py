import pandas as pd
from matplotlib import pyplot as plt
import scipy.stats as st
from scipy.stats import linregress
import numpy as np

state_df = pd.read_csv("Resources/Wheat_StateByState_formatted.csv")
print(state_df)
year_range = np.arange(1.0,8.0,1.0)
print(year_range)

nsw_wheat_prod = {'Year' : ['2017-18', '2018-19', '2019-20', '2020-21', '2021-22', '2022-23', '2023-24'],
                  'Hectares': [2793.5, 2382.0, 2132.0, 4037.0, 3607.7, 3600.0, 3300.0],
                  'Yield' : [4702.8, 1850.3, 1772.4, 12972.2, 12029.4, 10620.0, 6600.0]}
vic_wheat_prod = {'Year' : ['2017-18', '2018-19', '2019-20', '2020-21', '2021-22', '2022-23', '2023-24'],
                  'Hectares' : [1446.8, 1402.9, 1428.9, 1413.4, 1444.6, 1500.0, 1540.4],
                  'Yield' : [3682.1, 2276.6, 3714.3, 4525.0, 4246.4, 5392.9, 4618.9]}

# Pearsons R values for yield vs hectares
nsw_h_r, nsw_h_p = st.pearsonr(nsw_wheat_prod['Yield'], nsw_wheat_prod['Hectares'])
print(f"NSW correlation of yield to hectares is {round(nsw_h_r,2)}r.")
# we can see from this correlation that NSW yield is dependant on space
vic_h_r, vic_h_p = st.pearsonr(vic_wheat_prod['Yield'], vic_wheat_prod['Hectares'])
print(f'VIC correlation of yield to hectares is {round(vic_h_r,2)}r.')
# we can see from this correlation that VIC yield is not dependent on
# space and may be effected by external factors


# Creating a multi plot
fig, axs = plt.subplots(3, 2)
fig.suptitle('State wheat production per year')

#NSW graph
axs[0,0].scatter(nsw_wheat_prod['Year'], nsw_wheat_prod['Yield'], c=nsw_wheat_prod['Hectares'], cmap="viridis")
nsw_x_values = year_range
nsw_y_values = state_df['NSW_kt'].to_numpy()
(nsw_slope, nsw_intercept, nsw_rvalue, nsw_pvalue, nsw_stderr) = st.linregress(nsw_x_values, nsw_y_values)
nsw_regress = year_range * nsw_slope + nsw_intercept
axs[0,0].plot(year_range,nsw_regress,"r-")
axs[0,0].set_title('NSW wheat prod per year')
axs[0,0].set_ylabel('Yeild')
axs[0,0].set_xlabel('Year')

axs[0,1].scatter(vic_wheat_prod['Year'], vic_wheat_prod['Yield'], c=vic_wheat_prod['Hectares'], cmap="viridis")
(vic_slope, vic_intercept, vic_rvalue, vic_pvalue, vic_stderr) = linregress(year_range, state_df['VIC_kt'])
vic_regress = year_range * vic_slope + vic_intercept
axs[0,0].plot(year_range,vic_regress,"r-")
axs[0,1].set_title('Vic wheat prod per year')
axs[0,1].set_ylabel('Yeild')
axs[0,1].set_xlabel('Year')

axs[1,0].scatter(state_df['Year'], state_df['QLD_kt'], c=state_df['QLD_ha'], cmap="viridis")
(qld_slope, qld_intercept, qld_rvalue, qld_pvalue, qld_stderr) = linregress(year_range, state_df['QLD_kt'])
qld_regress = qld_range * qld_slope + qld_intercept
axs[0,0].plot(year_range,qld_regress,"r-")
axs[1,0].set_title('QLD wheat prod per year')
axs[1,0].set_ylabel('Yeild')
axs[1,0].set_xlabel('Year')

axs[1,1].scatter(state_df['Year'], state_df['SA_kt'], c=state_df['SA_ha'], cmap="viridis")
(sa_slope, sa_intercept, sa_rvalue, sa_pvalue, sa_stderr) = linregress(year_range, state_df['SA_kt'])
sa_regress = year_range * sa_slope + sa_intercept
axs[0,0].plot(year_range,sa_regress,"r-")
axs[1,1].set_title('SA wheat prod per year')
axs[2,0].set_ylabel('Yeild')
axs[2,0].set_xlabel('Year')

axs[2,0].scatter(state_df['Year'], state_df['WA_kt'], c=state_df['WA_ha'], cmap="viridis")
(wa_slope, wa_intercept, wa_rvalue, wa_pvalue, wa_stderr) = linregress(year_range, state_df['WA_kt'])
wa_regress = year_range * wa_slope + wa_intercept
axs[0,0].plot(year_range,wa_regress,"r-")
axs[2,0].set_title('WA wheat prod per year')
axs[2,0].set_ylabel('Yeild')
axs[2,0].set_xlabel('Year')

axs[2,1].scatter(state_df['Year'], state_df['TAS_kt'], c=state_df['TAS_ha'], cmap="viridis")
(tas_slope, tas_intercept, tas_rvalue, tas_pvalue, tas_stderr) = linregress(year_range, state_df['TAS_kt'])
tas_regress = year_range * tas_slope + tas_intercept
axs[0,0].plot(year_range,tas_regress,"r-")
axs[2,1].set_title('TAS wheat prod per year')
axs[2,1].set_ylabel('Yeild')
axs[2,1].set_xlabel('Year')

# DONE: implement r value
# DONE: figure out how to get lables on x and y axis
# TODO: Line of best fit on graphs
# TODO: try all states on a single scatter plot
# TODO: Try all states on a line chart
# TODO: Try states on a stacked bar chart
#


plt.show()

