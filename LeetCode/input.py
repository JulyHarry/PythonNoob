# -*- coding: utf-8 -*- 
"""
Description:
Creator: HarryUp
Create time: 2021-06-05 16:29
"""

while (True):
    a = input("Please input: ")
    try:
        b = 100/int(a)
        print(b)
    except Exception as e:
        print(e)

