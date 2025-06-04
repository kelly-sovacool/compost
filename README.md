## measuring compost & air temperature

NOAA data docs: <https://www.ncei.noaa.gov/pub/data/cdo/documentation/GHCND_documentation.pdf>

### Downloaded weather data from NOAA

The python noaa sdk can only get current observations, not historical observations.
Have to manually download historical data.

GHCN data for the station at Detroit airport:
<https://www.ncei.noaa.gov/cdo-web/datasets/GHCND/stations/GHCND:USW00094847/detail>

Select the station and click "Add to cart":

![](img/noaa_add-to-cart.png)

Go to the cart,
select "Custom GHCN-Daily CSV",
select the desired date range (e.g. 2024-11-01 to latest available),
then click continue:

![](img/noaa_cart-daily-sums.png)

Check all the options and continue:

![](img/noaa_data-flags.png)

Review the order, enter your email, and submit it:

![](img/noaa_review.png)

Once the dataset arrives in your inbox, place it in `data/`.
Move any prior files to `data/archive/`.
