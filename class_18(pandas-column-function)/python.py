import pandas as cd
import pandera as pa
import numpy as np
from nptyping import NDArray, Shape, Int64


total : int = 10000
s1 : NDArray[Shape[str(total)+"5"], Int64] = np.random.randint(80, 100, (total,5))
ss1 : cd.DataFrame = cd.DataFrame(s1,columns=['s1','s2','s3','s4','s5'])

s2 : NDArray[Shape[str(total)+"5"], Int64] = np.random.randint(70, 79,(total,5))
ss2 : cd.DataFrame = cd.DataFrame(s2,columns=['s1','s2','s3','s4','s5'])

s3 : NDArray[Shape[str(total)+"5"], Int64] = np.random.randint(60, 69, (total,5))
ss3 : cd.DataFrame = cd.DataFrame(s3,columns=['s1','s2','s3','s4','s5'])

s4 : NDArray[Shape[str(total)+"5"], Int64] = np.random.randint(50, 59, (total,5))
ss4 : cd.DataFrame = cd.DataFrame(s4,columns=['s1','s2','s3','s4','s5'])

s5 : NDArray[Shape[str(total)+"5"], Int64] = np.random.randint(40, 49, (total,5))
ss5 : cd.DataFrame = cd.DataFrame(s5,columns=['s1','s2','s3','s4','s5'])

s6 : NDArray[Shape[str(total)+"5"], Int64] = np.random.randint(33, 39, (total,5))
ss6 : cd.DataFrame = cd.DataFrame(s6,columns=['s1','s2','s3','s4','s5'])

s7 : NDArray[Shape[str(total)+"5"], Int64] = np.random.randint(0, 32, (total,5))
ss7 : cd.DataFrame = cd.DataFrame(s7,columns=['s1','s2','s3','s4','s5'])


print(len(ss1))
print(len(ss2))
print(len(ss3))
print(len(ss4))
print(len(ss5))
print(len(ss6))
print(len(ss7))

print(ss2)

df : cd.DataFrame = cd.concat([ss1,ss2,ss3,ss4,ss5,ss6,ss7]).reset_index(drop=True)

print(df.info()) # type: ignore
print("==============================================================================================================================================================================================")
print(df.describe())
print("======================================================================================================================================================")
print(df.head())# .head(n=60)
print("=============================================================================================================================================================")
print(df.tail())


# import pandas as pd
# values=[1,2,3,4,5]
# indexes=[["Artificial Intelligence","Artificial Intelligence","BlockChain","BlockChain","BlockChain"],["a1","a1","b1","b1","b1"],["0","1","2","3","4"]]
# s1=pd.Series(values,index=indexes)

# print(s1)
