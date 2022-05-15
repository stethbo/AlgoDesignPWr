from L6_0_data_structure import create_m_bots
import numpy as np


def quick_sort(arr, low, high):
    if low > high or low < 0:
        return
    
    p, arr =  partition(arr, low, high)

    quick_sort(arr, low, p - 1)
    quick_sort(arr, p + 1, high)

    return arr


def partition(arr, low, high):
    piv = arr[high]

    i = low - 1

    for j in range(low, high):
        if arr[j] <= piv:
            i += 1
            arr[j], arr[i] = arr[i], arr[j]
    
    i += 1
    arr[i], arr[high] = arr[high], arr[i]
    
    return i, arr


def sort_robots(bots, feat):
    """
    :param list bots: wektor robotów
    :param feat: cecha według której sortujemy
    """
    l = [b[feat] for b in bots]
    quick_sort(l, 0, len(l) - 1)
    new_robots = list()

    for r in l:
        for bot in robots:
            if bot['roz'] == r:
                new_robots.append(bot)
                robots.remove(bot)

    return new_robots            
            
        
robots = create_m_bots(20)
robots = [b.save_robot() for b in robots]
robots = sort_robots(robots, feat='roz')

for b in robots:
    print(b)

