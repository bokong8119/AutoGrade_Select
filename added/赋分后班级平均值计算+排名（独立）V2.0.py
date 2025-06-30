#添加了0分同学不计入平均分的功能（如果不用，请下载V1.0版本）
#兼容主程序V1.0、V2.0、V3.0，本程序是计算赋分后的班级平均分+排名（独立的程序，请务必运行主程序再运行插件）
import pandas as pd
df1=pd.read_excel('成绩（结合首考）.xlsx')
for i in range(len(df1)):
    if df1.at[i,'赋分（取高）']==0:
        df1=df1.drop(i)
df2=df1.groupby('班级',as_index=False).mean()
df3=df2[['班级','赋分（取高）']]
df3=df3.sort_values('赋分（取高）',ascending=False)
print(df3)   #展示平均分（直观展示）
df3.to_excel("赋分后班级排名.xlsx", index=False)  # index=False 表示不保存行索引