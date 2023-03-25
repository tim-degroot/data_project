*Developped by Tim de Groot for the course [Data Processing](https://studiegids.uva.nl/xmlpages/page/2022-2023/zoek-vak/vak/98740) of the UvA*
# What explains variation in land rents? 
## Aim and research question
The aim of this project is to empirically identify the impact of various characteristics of locations on land rents. It builds on an important notion in urban economics that land rents capture the attractiveness of locations, as it is a measure of the willingnes to pay for living in a particular location. This willingness is of course influenced by a lot of different characteristics. The question that is central in this project is what the characteristics of locations are for which people are willing to pay, and how much. Or, put simply: what explains variation in land rents? 

The final product presented is a notebook which contains some background information including some plots and two interactive dashboards which give insight on the explanatory variables that cause differences in land rents in the Netherlands. It can serve as a starting point for further development with specialists in the field of urban economics.

## Installation
Download all files (Markdown files are not required for running the program).
Use the following [pip](https://pip.pypa.io/en/stable/) and [conda](https://docs.conda.io/en/latest/) commands to install all required modules and to make a new environment.
```
pip install geopandas pandas matplotlib plotly scikit-learn ipywidgets numpy xlrd
conda create -n landrents python=3.11.0 geopandas pandas matplotlib plotly scikit-learn ipywidgets numpy xlrd
```
With all dependencies installed in an environment you can run the main notebook using [Jupyter Notebook](https://jupyter.org/) or [JupyterLab](https://jupyter.org/).


## File structure
- Directory ```data/``` contains the data files used. Sources are listed below.
- ```notebook.ipynb``` contains the final functions and dashboards.
- ```logbook.md``` contains a daily logbook of what was done, what documentation or help was used and what problems where encountered.
- ```readme.md``` this file.
- ```variables.py``` contains variables (lists and dictionaries) used in ```notebook.ipynb```.

## Data structure
The program requires a GeoPandas DataFrame which contains at least the following:
- a column containing **shapes**, which are used for the different maps.
- a column ```p_m2_FE``` containing **land rents**, which are used for the economic analysis.
- a column containing ***statistics*** (variables), which can be used to investigate their effect on land rents.
    - The program theoretically allows for an unlimited number of statistics.

### Data used
This version uses the following publicly available data sources:
- [Kerncijfers per postcode, 2018](https://www.cbs.nl/nl-nl/dossier/nederland-regionaal/geografische-data/gegevens-per-postcode) was used as the source for shapefiles of postal codes and for statistics per 4-digit zip code.
- [Grondprijzen per postcode, 2011](http://landvalues.nl/) was used as the source for land rents per 4-digit zip code.

## Prerequisites
- [GeoPandas](https://github.com/geopandas/geopandas) is used to work with shapefiles within pandas.
- [pandas](https://github.com/pandas-dev/pandas) is used for data importing and analysis
- [Matplotlib](https://github.com/matplotlib/matplotlib) is used for plotting maps.
- [plotly.py](https://github.com/plotly/plotly.py) is used for plotting scatterplots and bar charts.
- [scikit-learn](https://github.com/scikit-learn/scikit-learn) is used as the Linear Regression model backend.
- [ipywidgets](https://github.com/jupyter-widgets/ipywidgets) is used to make interactive html widgets within the jupyter notebook.
- [numpy](https://github.com/numpy/numpy) is used as backend for nan values.
- [xlrd](https://github.com/python-excel/xlrd) is a required dependency for pandas read_excel.