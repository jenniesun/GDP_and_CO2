import pandas as pd
wdi = pd.read_csv("wdi_small_tidy_2015.csv")
wdi.head()
wdi2=wdi[['Mortality rate, infant (per 1,000 live births)', 'GDP per capita (constant 2010 US$)', "Country Name"]]
wdi2
from plotnine import *
(ggplot(wdi2,aes(x='GDP per capita (constant 2010 US$)', y='Mortality rate, infant (per 1,000 live births)')) + geom_point()) + theme_classic()
