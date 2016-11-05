#!/bin/sh
csvfile=/home/crawl-dev/sizzell/vps/data.csv

crawlers=`/home/crawl-dev/sizzell/numplayers`
DF=`df |head -2 |awk '{print $5}' |tail -1|sed 's/\%//g'|sed 's/^/./g'`
RAM=`free -m | head -2|tail -1|awk '{print int($3 / ($3 + $4) * 100), "%" }'|sed 's/ //g'|sed 's/\%//g'|sed 's/^/./g'`
CPU1=`uptime|awk '{print $10}'|sed 's/,//g'`
CPU5=`uptime|awk '{print $11}'|sed 's/,//g'`
CPU15=`uptime|awk '{print $12}'|sed 's/,//g'`
TIME=`date "+%Y,%m,%d,%H,%M,%S"`
timeformat=`date "+%Y-%m-%d %H:%M:%S"`
year=`echo $TIME | awk -F',' '{print $1}'`
month=`echo $TIME | awk -F',' '{print $2}'`
day=`echo $TIME | awk -F',' '{print $3}'`
hour=`echo $TIME | awk -F',' '{print $4}'`
minute=`echo $TIME | awk -F',' '{print $5}'`
second=`echo $TIME | awk -F',' '{print $6}'`
plottime=$((day*24*60*60 + hour*60*60 + minute*60 + second))

numlines=`cat $csvfile |wc -l`
if [ ${numlines} -le "0" ];then
  echo "timeformat,plottime,year,month,day,hour,minute,second,disk,ram,cpu1,cpu5,cpu15,crawlers">$csvfile
fi

echo "$timeformat,$plottime,$year,$month,$day,$hour,$minute,$second,$DF,$RAM,$CPU1,$CPU5,$CPU15,$crawlers">>$csvfile

python /home/crawl-dev/sizzell/vps/cpu.py
python /home/crawl-dev/sizzell/vps/ram-disk.py
python /home/crawl-dev/sizzell/vps/crawlers.py




