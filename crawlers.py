from ggplot import *
import pandas as pd
import numpy as np

def dateConvert(df):
  df['timeformat'] = df.index
  df.reset_index(drop=True)
  return df

df = pd.read_csv("/home/crawl-dev/sizzell/vps/data.csv")
df = df[['timeformat','crawlers']]

timerange=df.iloc[0]
df = df[1:]

df_converted=dateConvert(df)
data = pd.melt(df_converted, id_vars='timeformat').dropna()

data = data.rename(columns ={'timeformat':'Date', 'variable':'Crawlers', 'value':'Number_of_Players'})

retPlot = ggplot(data, aes('Date','Number_of_Players',color='Crawlers')) \
  + geom_line(size=2.) \
  + geom_hline(yintercept=0, color='black', size=1.7, linetype='-.') \
  + scale_y_continuous() \
  + scale_x_date(labels='%m/%d %H:%M',breaks=date_breaks('1 hour') ) \
  + theme_seaborn(style='whitegrid') \
  + ggtitle(('Number of Crawlers Currently Playing')) \

fig = retPlot.draw()
ax = fig.axes[0]
offbox = ax.artists[0]
offbox.set_bbox_to_anchor((1, 0.5), ax.transAxes)

ggsave(plot=retPlot, filename="/home/crawl-dev/sizzell/vps/crawlers.png", dpi=100)
