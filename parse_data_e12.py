import json
import sys
import re

kssj_list = []
classrooms = {}

def add_kssj_to_list(kssj):
    if(kssj not in kssj_list):
        kssj_list.append(kssj)


def print_empty_classroom(msg_prefix, start=0, end=None):
    buffer = []
    msg = msg_prefix
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
    if(len(sys.argv) < 1):
        print("Usage: python3 parse_data.py YYYY-MM-DD")
        sys.exit()
    filename = "东十二楼" + "/" + sys.argv[1] + ".txt"
    with open(filename, 'r') as file:
        data = file.read().replace('\n', '')
    pattern=r'"borrowDate":"....-..-[0-9]+"'
    print("日期：{0}".format(re.findall(pattern, data)[0][14:-1]))
    pattern = r'\[.*\]'
    json_raw = re.findall(pattern, data)[0]
    json_data = json.loads(json_raw)
    for classroom in json_data:
        add_kssj_to_list(classroom['KSSJ'])
        if classroom['JSMC'] not in classrooms:
            classrooms[classroom['JSMC']] = []
        classrooms[classroom['JSMC']].append(classroom['KSSJ'])
    print_empty_classroom("发现全天空闲教室：")
    print_empty_classroom("发现上午空闲教室：", 0, 4)
    print_empty_classroom("发现下午空闲教室：", 4, 8)
    print_empty_classroom("发现白天空闲教室：", 0, 8)
    print_empty_classroom("发现晚上空闲教室：", 8, 12)
