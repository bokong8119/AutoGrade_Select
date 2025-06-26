import pandas as pd
def check_jixian():
    if score[100][0]!=100:
        score[100][0]=100
    if score[40][1]!=1:
        score[40][1]=1
def give_score(o_s):
    for i in range(40,101):
        if score[i][0]>=o_s>=score[i][1]:
            return i
    return 0
df1=pd.read_excel('赋分表.xlsx')
df2=pd.read_excel('成绩表.xlsx')
score={}
temp=0
while True:
    temp_low=df1.at[temp,'原始分']
    orignal_score=int(df1.at[temp,'赋分'])
    if orignal_score==100:
        score[orignal_score]=[100,float(temp_low)]
    else:
        b=score[orignal_score+1][1]
        score[orignal_score]=[b,float(temp_low)]
    temp+=1
    if temp==61:
        break
check_jixian()
student_length=len(df2)
for i in range(student_length):
    sk_score=df2.at[i,'首考']
    orignal_score=df2.at[i,'原始分']
    fufen_score=give_score(orignal_score)
    df2.at[i,'本次赋分']=fufen_score
    if fufen_score>=sk_score:
        df2.at[i,'赋分（取高）']=fufen_score
    else:
        df2.at[i,'赋分（取高）']=sk_score
df2.to_excel("成绩（结合首考）.xlsx", index=False)  # index=False 表示不保存行索引
print(score)
