from ggplot import *
import pandas as pd
import numpy as np

def dateConvert(df):
  df['timeformat'] = df.index
  df.reset_index(drop=True)
  return df

df = pd.read_csv("/home/crawl-dev/sizzell/vps/data.csv")
df = df[['timeformat','cpu1','cpu5','cpu15']]

timerange=df.iloc[0]
df = df[1:]

df_converted=dateConvert(df)
data = pd.melt(df_converted, id_vars='timeformat').dropna()

data = data.rename(columns ={'timeformat':'Date', 'variable':'TimeRange', 'value':'CPU_Load'})

retPlot = ggplot(data, aes('Date','CPU_Load',color='TimeRange')) \
  + geom_line(size=2.) \
  + geom_hline(yintercept=0, color='black', size=1.7, linetype='-.') \
  + scale_y_continuous() \
  + scale_x_date(labels='%m/%d %H:%M',breaks=date_breaks('1 hour') ) \
  + theme_seaborn(style='whitegrid') \
  + ggtitle(('CPU Load')) \

fig = retPlot.draw()
ax = fig.axes[0]
offbox = ax.artists[0]
offbox.set_bbox_to_anchor((1, 0.5), ax.transAxes)

ggsave(plot=retPlot, filename="/home/crawl-dev/sizzell/vps/cpu-actual.png", dpi=100)

retPlot = ggplot(data, aes('Date','CPU_Load',color='TimeRange')) \
  + geom_hline(yintercept=0, color='black', size=1.7, linetype='-.') \
  + scale_y_continuous() \
  + scale_x_date(labels='%m/%d %H:%M',breaks=date_breaks('1 hour') ) \
  + theme_seaborn(style='whitegrid') \
  + ggtitle(('CPU Load')) \
  + stat_smooth(span=0.2)

fig = retPlot.draw()
ax = fig.axes[0]
offbox = ax.artists[0]
offbox.set_bbox_to_anchor((1, 0.5), ax.transAxes)

ggsave(plot=retPlot, filename="/home/crawl-dev/sizzell/vps/cpu-smooth.png", dpi=100)
