## measuring compost & air temperature

NOAA data docs: <https://www.ncei.noaa.gov/pub/data/cdo/documentation/GHCND_documentation.pdf>

### Downloaded weather data from NOAA

The python noaa sdk can only get current observations, not historical observations. Have to manually download historical data.

Select the station and click "Add to cart":

![<https://www.ncei.noaa.gov/cdo-web/datasets/GHCND/stations/GHCND:USW00094847/detail>](img/noaa_add-to-cart.png)

Select "daily summaries" and the desired date range, then click continue:

![](img/noaa_cart-daily-sums.png)

Check all the options and continue:

![](img/noaa_data-flags.png)

Review the order, enter your email, and submit it:

![](img/noaa_review.png)

Once the dataset arrives in your inbox, place it in `data/`.
Move any prior files to `data/archive/`.
