import pandas as pd
from matplotlib import pyplot as plt
import scipy.stats as st
import numpy

state_df = pd.read_csv("Resources/Wheat_StateByState_formatted.csv")
print(state_df)
year_range = numpy.arange(1,7,1)

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

# Pearsons R values for year range vs yield
# nsw_y_r, nsw_y_p = st.pearsonr(state_df[NSW_kt], year_range)
# print(f"NSW correlation of yield per year is {round(nsw_y_r,2)}r.")
# vic_y_r, vic_y_p = st.pearsonr(state_df[VIC_kt], year_range)
# print(f"NSW correlation of yield per year is {round(vic_y_r,2)}r.")


fig, axs = plt.subplots(3, 2)
fig.suptitle('NSW and VIC wheat production')
axs[0,0].scatter(nsw_wheat_prod['Year'], nsw_wheat_prod['Yield'], c=nsw_wheat_prod['Hectares'], cmap="viridis")
axs[0,0].set_title('NSW wheat prod per year')
# axs[0,0].ylabel('Yeild')
# axs[0,0].xlabel('Year')

axs[0,1].scatter(vic_wheat_prod['Year'], vic_wheat_prod['Yield'], c=vic_wheat_prod['Hectares'], cmap="viridis")
axs[0,1].set_title('Vic wheat prod per year')
# axs[0,1].ylabel('Yeild')
# axs[0,1].xlabel('Year')

axs[1,0].scatter(state_df['Year'], state_df['QLD_kt'], c=state_df['QLD_ha'], cmap="viridis")
axs[1,0].set_title('QLD wheat prod per year')
# axs[1,0].ylabel('Yeild')
# axs[1,0].xlabel('Year')

axs[1,1].scatter(state_df['Year'], state_df['SA_kt'], c=state_df['SA_ha'], cmap="viridis")
axs[1,1].set_title('SA wheat prod per year')
# axs[2,0].ylabel('Yeild')
# axs[2,0].xlabel('Year')

axs[2,0].scatter(state_df['Year'], state_df['WA_kt'], c=state_df['WA_ha'], cmap="viridis")
axs[2,0].set_title('WA wheat prod per year')
# axs[2,0].ylabel('Yeild')
# axs[2,0].xlabel('Year')

axs[2,1].scatter(state_df['Year'], state_df['TAS_kt'], c=state_df['TAS_ha'], cmap="viridis")
axs[2,1].set_title('TAS wheat prod per year')
# axs[2,1].ylabel('Yeild')
# axs[2,1].xlabel('Year')

# DONE: implement r value
# TODO: figure out how to get lables on x and y axis
# TODO: Line of best fit on graphs
# TODO: try all states on a single scatter plot
# TODO: Try states on a bar graph
#


plt.show()

