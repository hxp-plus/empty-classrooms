#!/bin/bash
if [ $# -le 2 ]; then
    echo "Usage: ./run.sh <start_day> <end_day> <month>"
    exit 1
fi
start_day=$1
end_day=$2
month=$3
rm -f $month月西十二楼空闲教室.txt
rm -f $month月东十二楼空闲教室.txt
for (( i=$start_day; i<=$end_day; i++ ))
do
    python3 parse_data_w12.py 2021-$month-$i >> $month月西十二楼空闲教室.txt
    echo >> $month月西十二楼空闲教室.txt;
    python3 parse_data_e12.py 2021-$month-$i >> $month月东十二楼空闲教室.txt
    echo >> $month月东十二楼空闲教室.txt;
done
echo $month月西十二楼空闲教室.txt
cat $month月西十二楼空闲教室.txt
echo $month月东十二楼空闲教室.txt
cat $month月东十二楼空闲教室.txt
