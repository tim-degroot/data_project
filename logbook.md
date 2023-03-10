# Data Processing Project Logbook

## Wednesday 22/02/2023

### Goal: Determine project topic

- Discussed project ideas with teaching assistant.
    - Starting with a [dataset](http://landvalues.nl/) of land values per m2 in every postal code, find and analyze
      other datasets to discover influential factors on land values.

### Goal: Visualize the dataset of land values on a map using a color scale

- Find a suitable python module for mapping geographic data
    - Found
      a [Stack Overflow thread](https://stackoverflow.com/questions/58043978/display-data-on-real-map-based-on-postal-code)
      discussing mapping of Canadian postal code data. Answer showed the usage of geopandas.
- Found a [shapefile](https://public.opendatasoft.com/explore/dataset/georef-netherlands-postcode-pc4/information/) for
  4 letter postal codes of the Netherlands from opendatasoft
- Plotted the Weighted_avg_landprice_pc4_1985-2007 in Amsterdam on a map on a map. Decided to use a log of the price for
  better readability, as the price distribution is not linear.
    - Used [GeoDataFrame.plot](https://geopandas.org/en/stable/docs/reference/api/geopandas.GeoDataFrame.plot.html)
      documentation
    - Used [Stack Overflow thread](https://stackoverflow.com/a/63907917) method to normalize color mapping to a
      logarithmic scale

### Goal: Analyse trend between data and price per m2

- Used [Plotly](https://plotly.com/python/linear-fits/) to analyse trends using Ordinary Least Squares regression
  trendlines. The function also returns a fitted linear regression model so it can be stored to predict values.

## Thursday 23/02/2023

### Goal: Get more data from the CBS

- Found out that the CBS has data per postal code in a shapefile for different
  years [site](https://www.cbs.nl/nl-nl/dossier/nederland-regionaal/geografische-data/gegevens-per-postcode). Used this
  as shapefile instead of opendatasoft dataset.
    - Used data from 2018 as this has the most data (version 3).
- Looked at the correlation between avg. land rent and population density on a country level (all locations and heavily
  urbanized locations) which showed a relation between land rent and population density (which is not apparent within
  data containing only the same level of urbanization) within the Netherlands and the Metropoolreigo Amsterdam (MRA).
- Defined function reg() which finds the score of the linear regression of a certain column to the price (loglog).

## Friday 24/02/2023

### Goal: Analyse trends in data without the influence of population density

- Implemented a
  new [Linear Regression](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LinearRegression.html)
  model with more inputs to train a model that has predictive qualities using these inputs.
- [idek](https://scikit-learn.org/stable/auto_examples/cross_decomposition/plot_pcr_vs_pls.html#sphx-glr-auto-examples-cross-decomposition-plot-pcr-vs-pls-py)
- Tried a lot. Didn't work.

## Friday 03/03/2023

### Goal: Analyse influence of certain data factors on land values in a specific postal code

- Details: Implement a method to variate a certain factor while keeping the others on the average and seeing the influence.
- Set the PC4 as index for easier access without influencing regression. [Used site](https://datatofish.com/column-as-index-pandas-dataframe/)
  - Reworked region selection which previously used PC4 column. Now drops a row by index as per [pandas.DataFrame.drop documentation](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.drop.html)
- Issue: While trying to make two copies of a postal code and changing the factor to the minimum and maximum in the entire dataset the min and max remain the same. Using [pandas.DataFrame.copy](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.copy.html#) fixed this issue.
- Added Mean absolute percentage error (MAPE) regression loss rating from [sklearn.metrics.mean_absolute_percentage_error](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.mean_absolute_percentage_error.html#sklearn.metrics.mean_absolute_percentage_error)
- Calculated influence.
- Problems: Currently has very high errors (as the minimum and maximum are outliers). 
  - Solution: Used [pandas.DataFrame.quintile](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.quantile.html) instead of min/max.
- Problem: Currently the program only analyses whether changing the factor in one specific postal code would change land values in that postal code. 
  - Modified the function under ```influence_two``` which changes the factor in the entire dataset and returns the influence. Used this to add all influences to a dictionary.

- Issue: Does not seem to use the correct dataset. Or all datasets have the same average within the Netherlands.

## Sunday 05/03/2023

### Goal: Improve influence methods

- Added percentage of land value caused by a certain factor to influence function.
- Got regression coefficients from regression model in a DataFrame using method from [StackOverflow](https://stackoverflow.com/a/54027001)
- Adapted ```influence``` to give the total influence in land values in €/m2 instead of per km as this is the same as the regression coefficient.

### Goal: Make a new decomposition method

- The decomposition should get similar values as ```influence``` but for all factors. By default it should compare to the dataset average but an optional postal code to compare to should be possible.
- Made decomposition work for comparing to average in function ```decompose```. Yields graph.
- Found [StackOverflow](https://stackoverflow.com/questions/34755707/how-to-show-all-x-axis-tick-values-in-plotly#comment128241200_51059933) trick on how to show all y-axis labels as some were skipped. 
- Trial & error selection of factors to use to get a high R^2 on the regression without too many similar factors.

## Tuesday 07/03/2023
### Goal: Use interactive widgets to select which decomposition to show

- Used [Jupyter Widgets](https://ipywidgets.readthedocs.io/en/latest/). Used documentation: [Using Interact](https://ipywidgets.readthedocs.io/en/latest/examples/Using%20Interact.html) and [Widget List](https://ipywidgets.readthedocs.io/en/latest/examples/Widget%20List.html)
- Added selection for postal code and factors to take into the decomposition.
- Made decompose into a class to easily use different datasets.

### Goal: Plot decomposition of one variable on a map

- Reworked code and plot to loop over locations instead of postal code and managed to get working.
- Used Jupyter Widgets to make interactive.

### Goal: Make notebook into one nicely structured final project.

- Made ```notebook.ipynb``` which is the final project file.
    - Added the progress through the project with added explanation.
    - Reworked the functions to work properly and in a new order.
    - Added new text description

## Friday 10/03/2023
## Goal: Work on final hand in version

- Rewrote docstring documentation in notebook.ipynb
- Rewrote and added to readme.md documentation