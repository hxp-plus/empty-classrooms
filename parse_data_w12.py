import json
import sys
import re

kssj_list = []
classrooms = {}

def add_kssj_to_list(kssj):
    if(kssj not in kssj_list):
        kssj_list.append(kssj)


def print_empty_classroom(msg_prefix, start=0, end=None):
    msg = msg_prefix
    buffer = []
    for classroom in classrooms.keys():
        if(all(elem in classrooms[classroom] for elem in kssj_list[start:end])):
            buffer.append(classroom)
    for classroom in sorted(buffer):
            msg += ' '
            msg += classroom
    print(msg)
    msg = "检查过的时间有："
    for kssj in kssj_list[start:end]:
        msg += " "
        msg += kssj
    print(msg)


if __name__ == '__main__':
    if(len(sys.argv) < 2):
        print("Usage: python3 parse_data.py YYYY-MM-DD")
        sys.exit()
    
    filename_n = "西十二楼N" + "/" + sys.argv[1] + ".txt"
    with open(filename_n, 'r') as file:
        data_n = file.read().replace('\n', '')
    pattern=r'"borrowDate":"....-..-[0-9]+"'
    print("日期：{0}".format(re.findall(pattern, data_n)[0][14:-1]))
    pattern = r'\[.*\]'
    json_raw_n = re.findall(pattern, data_n)[0]
    json_data_n = json.loads(json_raw_n)
    
    for classroom in json_data_n:
        add_kssj_to_list(classroom['KSSJ'])
        if classroom['JSMC'] not in classrooms:
            classrooms[classroom['JSMC']] = []
        classrooms[classroom['JSMC']].append(classroom['KSSJ'])

    filename_s = "西十二楼S" + "/" + sys.argv[1] + ".txt"
    with open(filename_s, 'r') as file:
        data_s = file.read().replace('\n', '')
    pattern=r'"borrowDate":"....-..-[0-9]+"'
    pattern = r'\[.*\]'
    json_raw_s = re.findall(pattern, data_s)[0]
    json_data_s = json.loads(json_raw_s)
    for classroom in json_data_s:
        add_kssj_to_list(classroom['KSSJ'])
        if classroom['JSMC'] not in classrooms:
            classrooms[classroom['JSMC']] = []
        classrooms[classroom['JSMC']].append(classroom['KSSJ'])
    
    print_empty_classroom("发现全天空闲教室：")
    print_empty_classroom("发现上午空闲教室：", 0, 4)
    print_empty_classroom("发现下午空闲教室：", 4, 8)
    print_empty_classroom("发现白天空闲教室：", 0, 8)
    print_empty_classroom("发现晚上空闲教室：", 8, 12)
