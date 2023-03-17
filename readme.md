*Developped by Tim de Groot for the course [Data Processing](https://studiegids.uva.nl/xmlpages/page/2022-2023/zoek-vak/vak/98740) of the UvA*
# Land Rent Dashboards - Data Processing project
The aim of this project is to analyse different factors and their effect on land rents. The final product presented is a notebook which contains some plots and background information and two interactive dashboards which give insight on the factors that cause difference in land rents in the Netherlands.

## Research question

## Installation
Download all files (Markdown files are not required for running the program).
Use the following [pip](https://pip.pypa.io/en/stable/) command to install all required modules:
```pip install geopandas pandas matplotlib plotly scikit-learn ipywidgets numpy```
With all dependencies installed you can run the main notebook using Jupyter Notebook.


## File structure
- Directory ```data/``` contains the data files used.
- ```notebook.ipynb``` contains the final functions and dashboards.
- ```logbook.md``` contains a daily logbook of what was done, what documentation or help was used and what problems where encountered.
- ```readme.md``` this file.
- ```variables.py``` contains variables (lists and dictionaries) used by ```notebook.ipynb```

## Data structure
The program requires a GeoPandas DataFrame which contains at least the following:
- a column containing **shapes**, which are used for the different plots.
- a column ```p_m2_FE``` containing **land rents**, which are used for the financial analysis.
    - with some small modifications another (financial) statistic can be used.
- a column containing ***statistics***, which can be used to investigate their effect on land rents.
    - The program theoretically allows for unlimited statistics.

### Data used
This version uses the following publicly available data sources:
- [Kerncijfers per postcode, 2018](https://www.cbs.nl/nl-nl/dossier/nederland-regionaal/geografische-data/gegevens-per-postcode) was used as the source for shapefiles of postal codes and for statistics per postal code.
- [Grondprijzen per postcode, 2011](http://landvalues.nl/) was used as the source for land rents per postal code.

## Prerequisites
- [GeoPandas](https://github.com/geopandas/geopandas) is used to work with shapefiles within pandas.
- [pandas](https://github.com/pandas-dev/pandas) is used for data importing and analysis
- [Matplotlib](https://github.com/matplotlib/matplotlib) is used for plotting maps.
- [plotly.py](https://github.com/plotly/plotly.py) is used for plotting scatterplots and bar charts.
- [scikit-learn](https://github.com/scikit-learn/scikit-learn) is used as the Linear Regression model backend.
- [ipywidgets](https://github.com/jupyter-widgets/ipywidgets) is used to make interactive html widgets within the jupyter notebook.
- [numpy](https://github.com/numpy/numpy) is used as backend for nan values.

