# coding:utf-8
import re

iplist = []
portlist = []
isip=False;
datafile = file("ip.txt", "r")

for line in datafile.readlines():
    line = line.strip('\n')
    result=re.findall(r"\b(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\b", line);
    if not result:
        if isip:
            portlist.append(line)
            isip=False
    else:
        isip=True
        iplist.append(result)