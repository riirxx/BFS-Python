# -*- coding: utf-8 -*-
import numpy as np
migong = '''
4   3   4   1   2
0   1   3   3   1
4   2   2   3   3
3   1   2   1   3
2   4   2   4   4'''
data = np.array(migong.split(), dtype = int).reshape((5,5))
 
 
def direction_set(data):
    """
        函数功能，找到data中未被走过的地方，并同时记录该地方能够走的地方
    """
    dir_set = {}
    v, h = np.where(data > -1)
    for i,j in zip(v, h):
        key = str(i) + str(j)
        count = data[i,j]
        if j + count < 5:            #向右
            dir_set[key] = [str(i)+str(j+count)]
        if i + count < 5:            #向下
            if key in dir_set:
                dir_set[key] += [str(i+count)+str(j)]
            else:
                dir_set[key] = [str(i+count)+str(j)]
        #data[i, j-1]
        if j - count < 5 and j-count >=0:            #向左
            if key in dir_set:
                dir_set[key] += [str(i)+ str(j-count)]
            else:
                dir_set[key] = [str(i)+ str(j-count)]
        #data[i-1, j]
        if i - count < 5 and i-count >= 0:            #向上
            if key in dir_set:
                dir_set[key] += [str(i-count)+str(j)]
            else:
                dir_set[key] = [str(i-count) +str(j)]
    return dir_set
 
def get_forward_step(exit_index):
    layer_ori = ['00']   #存放第一层信息 
    while True:     
        layer_sec = []      #存放第二层信息
        for key in layer_ori: #将layer_ori里面所能达到的位置，存放在layer_sec中
            layer_sec += direction[key]
            if exit_index in direction[key]:
                forward_step = key
        if exit_index in layer_sec: break
        layer_ori = layer_sec
    return forward_step
def changeWASD(step):
    wasd = ''
    j = 0;
    for i in step:
        j += 1
        if j > len(step)-1:
            break
        result = int(step[j]) - int(i)
        if result > 0 and result < 10:
            wasd += 'R'
            continue
        if result >= 10:
            wasd += 'D'
            continue
        if result <= -10:
            wasd += 'U'
        else:
            wasd += 'L'
    return wasd
 
if __name__ == '__main__':
    direction = direction_set(data)

    huish = ['10']
    while True:
        forward_step = get_forward_step(huish[-1])
        huish += [forward_step]
        if forward_step == '00':
            break
    step = huish[::-1][:-1]
    num = ''
    for ind in step:
        num += str(data[int(ind[0]), int(ind[1])])
    print(data)
    print(step)
    wasd = changeWASD(step)
    print(wasd+num)



