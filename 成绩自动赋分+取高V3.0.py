#后续版本如果有更新，除非特别强调Excel文件也要更新的版本外，所依赖的Excel文件与上一个代码所依赖的版本一致（也会在README里面说明，如果Excel文件有更新）
#V3.0版本中，添加了断层赋分中间部分自动删除（照顾某些用户忘记删除空缺的赋分，如61赋分到70，62赋分到73，71~72没有删除）和考生原始分和首考空缺自动填写（0分）的功能
import pandas as pd
def check_jixian():   #确保1~100分的都可以赋到分（0分仍然是0分，拟认定为涂了缺考标记）
    if score[100][0]!=100:
        score[100][0]=100.0
    if score[40][1]!=1:
        score[40][1]=1.0
def give_score(o_s):  #给与赋分结果（单一）
    for i in range(40,101):
        if i not in score:   #没有赋分值时跳过该数值，以免报错（比如60赋分71，61赋分78，赋分值72~77的跳过，赋分值72~77的在表格中请删除）
            continue
        if score[i][0]>=o_s>=score[i][1]:
            return i
    return 0
df1=pd.read_excel('赋分表.xlsx')
df2=pd.read_excel('成绩表.xlsx')
score={}
df1=df1.dropna(subset=['赋分']) #删除DataFrame中NaN值（照顾某些用户忘记删除空缺的赋分，如61赋分到70，62赋分到73，71~72没有删除）
df1=df1.reset_index(drop=True) # 重新排序索引，其中不将旧索引添加为新列
for temp in range(len(df1)):   #确定赋分区间（表格里面填写的是可以取到的最低值）
    temp_low=df1.at[temp,'原始分']
    orignal_score=int(df1.at[temp,'赋分'])
    if orignal_score==100:
        score[orignal_score]=[100,float(temp_low)]
    else:
        score[orignal_score]=[float(temp_score),float(temp_low)]
    temp_score=temp_low-1
check_jixian()  #检查赋分范围极限值合理性
student_length=len(df2)
df2['首考'] = df2['首考'].fillna(0)
df2['原始分'] = df2['原始分'].fillna(0)
for i in range(student_length):  #给予赋分并且结合首考取高（如果还没有参加首考的，把首考分数设成0）
    sk_score=df2.at[i,'首考']
    orignal_score=df2.at[i,'原始分']
    fufen_score=give_score(orignal_score)
    df2.at[i,'本次赋分']=fufen_score
    if fufen_score>=sk_score:   #首考的比本次的高（没有首考的会跳过去）
        df2.at[i,'赋分（取高）']=fufen_score
    else:
        df2.at[i,'赋分（取高）']=sk_score
df2.to_excel("成绩（结合首考）.xlsx", index=False)  # index=False 表示不保存行索引
print("本次赋分的区间为",score)  #展示赋分区间（主要是给开发人员看的——看有没有错误）
#赋分区间出来之后就可以把交互界面关闭了（交互界面上的赋分区间可以不看）