from scipy import optimize
import numpy as np
if __name__ == '__main__':
    #对应笔记上的例题
    c = np.array([2,3,-5])
    A = np.array([[-2,5,-1],[1,3,1]])#系数矩阵，第一个为大于不等式需要乘以-1
    b = np.array([-10,12])#增广矩阵
    Aeq = np.array([[1,1,1]])
    beq = np.array([7])#等式约束
    ###五个系数决定方程
    #res  = optimize.linprog(-c,A,b,Aeq,beq)
    c = np.array([2,3,1])
    A = np.array([[-1,-4,-2],[-3,-2,0]])
    b = np.array([-8,-6])
    Aeq = np.array([[0,0,0]])
    beq = np.array([0])
    res = optimize.linprog(c,A,b,Aeq,beq)
    print(res)
