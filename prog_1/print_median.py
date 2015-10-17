# -*- coding: utf-8 -*-

from __future__ import division
import os.path, sys


def median(arr1,arr2,left,right):
    if left > right:
        return median(arr2, arr1, 0, n-1) #если дошли до края массива - ищем в другом
    i = (left + right) // 2
    j = n - i - 1
    if arr1[i] >= arr2[j] and (i == 0 or arr1[i] <= arr2[j+1]): #нашли медиану
        if i== 0 or arr2[j] > arr1[i-1]:
            return (arr1[i] + arr2[j])/2
        else:
            return (arr1[i] + arr1[i-1])/2
    elif i != 0 and arr1[i] > arr2[j+1]:
        return median(arr1, arr2, left, i-1)
    else:
        return median(arr1, arr2, i + 1, right)

if __name__ == "__main__":
    list1 = []
    list2 = []
    try:
        with open('arrayFile', 'r') as fopen:
            for i in fopen.readline().split(','):
                list1.append(int(i))
            for i in fopen.readline().split(','):
                list2.append(int(i))
    except (IOError, ValueError):
        print "Error occured while reading arrayFile. Trying to continue with hardcoded values..."
        list1 = [1, 2, 3 ,4]
        list2 = [1, 4, 5, 6]

    print list1, list2
    if len(list1) != len(list2):
        print "Length of the arrays is not equal. Aborting..."
        sys.exit(-1)
    else:
        n = len(list1)
    if list1[0] > list2[-1]: #если один массив строго больше другого
        print "Result is", (list1[0] + list2[-1]) / 2
        sys.exit(0)
    elif list2[0] > list1[-1]:
        print "Result is", (list1[-1] + list2[0]) / 2
        sys.exit(0)

    print median(list1, list2, 0, n-1)
    
