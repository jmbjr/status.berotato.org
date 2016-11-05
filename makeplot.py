from ggplot import *
import pandas as pd
import numpy as np
df = pd.read_csv("/home/crawl-dev/sizzell/vps/data.csv")
df = df[['timeformat','plottime','year', 'month', 'day', 'hour', 'minute', 'second', 'disk', 'ram','cpu1','cpu5','cpu15']]

p = ggplot(aes(x='plottime', y='cpu5', color='cpu1', size='cpu15', label="ram"), data=df) + geom_point()
ggsave(p, "/home/crawl-dev/sizzell/vps/test.png")

#p3 = ggplot(aes(x='MonsHD', y='MonsXP', color='Num'), data=df) + geom_point() + facet_wrap(x="Monster", y=None, scales="free")

#ggsave(p3, "Monsters.faceted.png")


