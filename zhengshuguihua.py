import pulp as pp
if __name__ == '__main__':
    # 参数设置
    c = [3,4,1]        #目标函数未知数前的系数

    A_gq = [[1,6,2],[2,0,0]]   # 大于等于式子 未知数前的系数集合 二维数组
    b_gq = [5,3]         # 大于等于式子右边的数值 一维数组


    # 确定最大最小化问题，当前确定的是最小化问题
    m = pp.LpProblem(sense=pp.LpMinimize)

    # 定义三个变量放到列表中 生成x1 x2 x3
    x = [pp.LpVariable(f'x{i}',lowBound=0,cat='Integer') for i in [1,2,3]]

    # 定义目标函数，并将目标函数加入求解的问题中
    m += pp.lpDot(c,x) # lpDot 用于计算点积

    # 设置比较条件
    for i in range(len(A_gq)):# 大于等于
        m += (pp.lpDot(A_gq[i],x) >= b_gq[i])

    # 求解
    m.solve()

    # 输出结果
    print(f'优化结果：{pp.value(m.objective)}')
    print(f'参数取值：{[pp.value(var) for var in x]}')
