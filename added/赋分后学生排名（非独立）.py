#兼容主程序V1.0、V2.0、V3.0，本程序是计算赋分后的每位同学的排名（分为班级内部和全部）（非独立的程序，请务必复制在主程序后面）
flag=False   #False表示未进行正确性检查或者state状态填写有误，True表示state状态填写正确
state=0 #0表示班级内部排名，1表示全部学生排名
def state0(df_orignal,class_list):
    result= pd.DataFrame() 
    for i in class_list:
        df_temp=df_orignal[df_orignal['班级']==i]
        df_temp=df_temp.sort_values('赋分（取高）',ascending=False)
        result=pd.concat([result, df_temp], ignore_index=True)    #DataFrame合并操作,ignore_index=True表示索引重新排序
    return result
def get_class_list(df):
    list = df['班级'].unique().tolist()   #读取班级信息
    return list
def state1(df_orignal):
    df_orignal=df_orignal.sort_values('赋分（取高）',ascending=False)
    return df_orignal
if state==0:
    list=get_class_list(df2)
    df2=state0(df2,list)
    flag=True
elif state==1:
    df2=state1(df2)
    flag=True
else:
    print('输入的状态有误，请检查')
if flag==True:
    if state==1:
        df2.to_excel("赋分后学生排名.xlsx", index=False)
    elif state==0:
        df2.to_excel("赋分后学生排名(以班级独立排名).xlsx", index=False)
