#!/bin/python3

n = int(input())
if(n%2!=0 or (n%2==0 and 6<=n<=20)):
    print("Weird")
if(n%2==0 and 2<=n<=5 or (n%2==0 and n>20)):
    print("Not Weird")
