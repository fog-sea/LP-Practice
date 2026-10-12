import pulp #4.x.x

myprobLP = pulp.LpProblem('LPProbDemo1',sense = pulp.LpMaximize)
x1 = myprobLP.add_variable('x1',lowBound = 0 ,upBound = 8 , cat = 'Continuous')
x2 = myprobLP.add_variable('x2',lowBound = 0 , cat = 'Continuous')

myprobLP += 10*x1 + 9*x2
myprobLP += (6*x1 + 5*x2 <= 60)
myprobLP += (10*x1 + 20*x2 <= 150)

result = myprobLP.solve(pulp.HiGHS())
print(result)
for v in myprobLP.variables():
    print(f"{v.name} = {v.varValue}")

myprobLP2 = pulp.LpProblem('LPProbDemo2',sense = pulp.LpMaximize)
x1 = myprobLP2.add_variable('x1',lowBound = 0 ,upBound = 8 , cat = 'Continuous')
x2 = myprobLP2.add_variable('x2',lowBound = 0 , cat = 'Continuous')
y  = myprobLP2.add_variable('y',lowBound = 0 , cat = 'Continuous')
myprobLP2 += 10*x1 + 9*x2 - y
myprobLP2 += (6*x1 + 5*x2 <= 60 + y/0.8)
myprobLP2 += (10*x1 + 20*x2 <= 150 )

result = myprobLP2.solve(pulp.HiGHS())
print(result)
for v in myprobLP2.variables():
    print(f"{v.name} = {v.varValue}")

myprobLP3 = pulp.LpProblem('LPProbDemo3',sense = pulp.LpMaximize)
x1 = myprobLP3.add_variable('x1',lowBound = 0 ,upBound = 8 , cat = 'Continuous')
x2 = myprobLP3.add_variable('x2',lowBound = 0 , cat = 'Continuous')
n  = myprobLP3.add_variable('n',lowBound = 0 , cat = 'Integer') #可以单个变量设为整数
myprobLP3 += 10*x1 + 9*x2 + n   #运算中不可以使用整除等运算函数
myprobLP3 += (6*x1 + 5*x2 <= 60 )
myprobLP3 += (10*x1 + 20*x2 <= 150 )
myprobLP3 += (n <= x1 )
#myprobLP3 += (x1 <= n+1-0.0000000001 ) #约束条件中不可以使用<或>,需要使用<=,>= 
result = myprobLP3.solve(pulp.HiGHS())
print(result)
for v in myprobLP3.variables():
    print(f"{v.name} = {v.varValue}")

myprobLP5 = pulp.LpProblem('LPProbDemo3',sense = pulp.LpMaximize)
x1 = myprobLP5.add_variable('x1',lowBound = 0 ,upBound = 8 , cat = 'Integer')
x2 = myprobLP5.add_variable('x2',lowBound = 0 , cat = 'Integer')
myprobLP5 += 10*x1 + 9*x2
myprobLP5 += (6*x1 + 5*x2 <= 60 )
myprobLP5 += (10*x1 + 20*x2 <= 150 )

result = myprobLP5.solve(pulp.HiGHS())
print(result)
for v in myprobLP5.variables():
    print(f"{v.name} = {v.varValue}")
