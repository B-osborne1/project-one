## Wheat price sources

### Internatioinal Grains council

#### GMR Summary

* `https://www.igc.int/en/gmr_summary.aspx`
* GMR summary tables display the amount of production, trade, consumption, and carry over rates in millions of tonnes.
* This isn't directly benificial for the price data, however it is production data.
* A few of these files have been downloaded and put into the `GMR Summary` folder.

#### Grains and Oilseed Index (GOI)
* `https://www.igc.int/en/markets/marketinfo-goi.aspx`
* The GOI provides some other data relating to the Index and volitilty of wheat and other comodities.
* Personally I don't understand how the index relates to the price of this so this may be useless data.
* The GOI excel doccument has been put into the `Grains and Oilseed Index` folder.

### Trading economics wheat commodities price

* `https://tradingeconomics.com/commodity/wheat`
* Has data on global wheat prices, however it requires a subscription.

### Carghill Pricing Hub

* `https://au.mycargill.com/PricingHub/Overview`
* A local hub for pricing wheat
* Data is available here, but it needs to be scraped from the website or collected manually.
* This looks a bit more complex than basic HTML scraping so collecting data may be time consuming.

### International Monitary Fund (Primary Commodity Pricing Index)

* `https://data.imf.org/?sk=471dddf8-d8a7-499a-81ba-5b332c01f8b9`
* This provides data on both the global price and index of Wheat.
* The annual price in USD and the anual index have been saved to the `IMF PCP` folder.
* Having the index and price here may help us reverse engineer the prce out of the index from the IGC Grains and Oilseed Index.