# import numpy as np
# arr=np.array([1,2,3,4,5])
# print(arr)
# print(arr+10)
# print(arr*2)


# arr2=np.array([[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15]])
# print(arr2)
# print(arr[0])
# print(arr2[0][0])


# import pandas as pd
# df=pd.DataFrame({
#     "Name":["Alice","Bob","Charlie"],
#     "Age":[25,30,35],
#     "City":['New York','Los Angeles','Chicago'],
#     "Marks":[85,88,90]
# })
# print(df)
# print(df[df['Marks']>85])

import pandas as pd
data={
     "Name":["Alice","Bob","Charlie"],
     "Age":[25,30,35],
     "City":['New York','Los Angeles','Chicago'],
     "Marks":[85,88,90]
 }
df=pd.DataFrame(data)
print(df.describe())
print(df.info())
print(df.corr())


# import matplotlib.pyplot as plt
# names=['Alice','Bob','Charlie']
# marks=[85,88,90]
# plt.scatter(names,marks)
# plt.xlabel('Names')
# plt.ylabel('Marks')
# plt.title('Marks of Students')
# plt.show()

# plt.pie(marks,labels=names,autopct='%1.1f%%')
# plt.title('Marks of Students')
# plt.show()

# plt.plot(names,marks)
# plt.xlabel('Names')
# plt.ylabel('Marks')
# plt.title('Marks of Students')
# plt.show()


# plt.bar(names,marks)
# plt.xlabel('Names')
# plt.ylabel('Marks')
# plt.title('Marks of Students')
# plt.show()

