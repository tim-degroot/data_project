*Developped by Tim de Groot for the course [Data Processing](https://studiegids.uva.nl/xmlpages/page/2022-2023/zoek-vak/vak/98740) of the UvA*
# Land Rent Dashboards - Data Processing project
The aim of this project is to analyse different factors and their effect on land rents. The final product presented is a notebook which contains some plots and background information and two interactive dashboards which give insight on the factors that cause difference in land rents in the Netherlands.

## Features
The project contains different functions and two interactive dashboards.

Functions:
- ```plot(column, n)```: Plot *column* of the dataset to a map on a 4-digit zipcode level
- ```plot_relation(data, column, title=''):```: Plot the log log correlation of *column* to p_m2_FE from *data* and draw a Ordinary Least Squares (OLS) regression trendlines
- ```coeff_df(dataset, m)```: Fit a Linear Regression model of factors *m* of *dataset* and return the R^2 score and a DataFrame of coefficients
- ```decompose(location, m)```: Plot the decomposition of the land value difference in *location* compared to the average as effected by factors *m*
- ```factor_map(factor, m)```: Plot a map which plots the effect of *factor* as determined by a Linear Regression model which takes *m* as input

**Interactive dashboards**:
- A dashboard of ```decompose(location, m)``` where location and m can be selected.
- A dashboard of ```factor_map(factor, m)``` where factor and m can be selected.

## Usage
The **decomposition dashboard** *(3.1)* shows the decomposition of the effect of the selected factors on the difference of the land rent in postal code compared to the dataset average.
- Any postal code in the Netherlands can be entered.
- Factors in m[0] can be added or removed from the Linear Regression model and thus the decomposition plot.
    - At least two factors must be present

The **effect map dashboard** *(3.2)* shows the decomposed effect of the selected factor on the land rent in all postal postal codes which uses a Linear Regression model of factors m.
- The selected factor should be in the factors m.

### File structure
- Directory ```.ipynb_checkpoints``` contains notebook checkpoints
- Directory ```
- Directory ```data/``` contains the data files used.
- ```notebook.ipynb``` contains the final product of all final functions and dashboards.
- ```working.ipynb``` contains all functions developped in the process of getting to the final functions and dashboards.
- ```logbook.md``` contains a daily logbook of what was done, what documentation or help was used and what problems where encountered.
- ```readme.md``` this file.
- ```variables.py``` contains variables (lists and dictionaries) used by ```notebook.ipynb```

### Data used
The program uses two different data sources which can be replaced by other similar datasets. Multiple different datasets can be used to form one dataframe.
- The primary data source is a shapefile of regions (in this case postal codes). The one used also contains statistics for the regions.
    - [Kerncijfers per postcode, 2018](https://www.cbs.nl/nl-nl/dossier/nederland-regionaal/geografische-data/gegevens-per-postcode) was used as the source for shapefiles of postal codes and for statistics per postal code.
- An additional data source with data per regions is used and the data is added to one dataframe with the shapefiles. More additional data sources can be added for more comprehensive analysis.
    - [Grondprijzen per postcode, 2011](http://landvalues.nl/) was used as the source for land rents per postal code. 

### Techniques used
- [GeoPandas](https://github.com/geopandas/geopandas) is used to work with shapefiles within pandas.
- [pandas](https://github.com/pandas-dev/pandas) is used for data importing and analysis
- [Matplotlib](https://github.com/matplotlib/matplotlib) is used for plotting maps.
- [plotly.py](https://github.com/plotly/plotly.py) is used for plotting scatterplots and bar charts.
- [scikit-learn](https://github.com/scikit-learn/scikit-learn) is used as the Linear Regression model backend.
- [ipywidgets](https://github.com/jupyter-widgets/ipywidgets) is used to make interactive html widgets within the jupyter notebook.
- [numpy](https://github.com/numpy/numpy) is used as backend for nan values.

