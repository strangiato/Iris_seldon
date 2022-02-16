from Iris import Iris

X = [[5,3,1.6,0.2]]
columns = ['sepal length', 'sepal width', 'petal length', 'petal width']

tmp = Iris()

ans = tmp.predict(X,columns)

print(ans)
