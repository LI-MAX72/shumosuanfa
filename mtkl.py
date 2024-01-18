import numpy as np
if __name__ == '__main__':
    def objfun(x):
        z = x[0]**2 + x[1]**2 + 3*x[2]**2 + 4*x[3]**2 + 2*x[4]**2 - 8*x[0] - 2*x[1] - 3*x[2] - x[3] - 2*x[4]
        return z
    def confun(x):
        c = [x[0] + x[1] + x[2] + x[3] + x[4] - 400,
             x[0] + 2*x[1] + 2*x[2] + x[3] + 6*x[4] - 800,
             2*x[0] + x[1] + 6*x[2] - 200,
             x[2] + x[3] + 5*x[4] - 200]
        if all(i <= 0 for i in c):
            return 1
        else:
            return 0
    n = 10000000  # 模拟次数
    lb = np.zeros(5)  # 变量下界
    ub = np.full(5, 99)  # 变量上界
    sol = []  # 保存满足约束条件的解
    fval = float('-inf')  # 保存最大值
    for i in range(n):
        x = np.floor(lb + (ub - lb + 1) * np.random.rand(5))  # 生成随机解
        if confun(x) == 1:  # 判断是否满足约束条件
            z = objfun(x)  # 计算目标函数值
            if z > fval:  # 更新最大值
                fval = z
                sol = x
    print(fval)
    print(sol)
