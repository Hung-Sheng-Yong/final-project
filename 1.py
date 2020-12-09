# -*- coding: utf-8 -*-
"""
Created on Sat Nov 21 21:11:29 2020

@author: hungs
"""


list1 = input().split(";")
list_weight = list1[1].split(",")

list_text = input().split(",")
list_score = []
for i in range(int(list1[0])):
    list_score.append(input().split(","))

list_sum = []
for i in range(len(list_score)):
    sum_ = 0
    for j in range(1, 5):
        sum_ += float(list_score[i][j])*float(list_weight[j-1])
    list_sum.append([list_score[i][0], sum_])

biggest = [1, -1]
for i in range(len(list_sum)):
    if list_sum[i][1] == biggest[1]:
        if int(list_sum[i][0]) < int(biggest[0]):
            biggest = list_sum[i]
    if list_sum[i][1] > biggest[1]:
        biggest = list_sum[i]


final_score = biggest[1]//100

print(str(biggest[0]) + "," +str(int(final_score)))
