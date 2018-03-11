a=[1,1,2,3,5,8,13,21,34,55,89,144,233,377,610,987]
x=input('')
y=input('')
print (['F', 'T'][sum([a[int(i)]*int(x[int(i)]) for i in x[::-1]])==sum([a[int(i)]*int(y[int(i)]) for i in y[::-1]])])
