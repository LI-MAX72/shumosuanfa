import pulp as pp
if __name__ == '__main__':
    c = [40,90]
    A_gq = [[9,7],[7,20]]
    b_gq = [56,70]

    m = pp.LpProblem(sense = pp.LpMaximize)

    x = [pp.LpVariable(f'x{i}',lowBound = 0,cat = 'Integer') for i  in [1,2]]

    m+=pp.lpDot(c,x);
    for i in  range(len(A_gq)):
        m+=(pp.lpDot(A_gq[i],x)<=b_gq[i])
    m.solve()
    print(f'优化结果：{pp.value(m.objective)}')
    print(f'参数取值：{[pp.value(var) for var in x]}')
