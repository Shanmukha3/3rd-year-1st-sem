def accuracy(tp,tn,fp,fn):
    acc=(tp+tn)/(tp+tn+fp+fn)
    return acc

def precision(tp,fp):
    pre=tp/(tp+fp)
    return pre
    
def recall(tp,fp):
    rec=tp/(tp+fn)
    return rec

def f1score(pre,rec):
    score=(2*pre*rec)/(pre+rec)
    return score


m=int(input("enter the no of classes: "))
matrix=[]
d={}
e={}
tp=tn=fp=fn=0
print("Enter the names of the class: ")
for i in range(m):
    p=input()
    d[i]=p
print("Now enter the values:")
for i in range(m):
    l=[]
    for j in range(m):
        n=int(input())
        l.append(n)
    matrix.append(l)
for i in range(m):
    tp=matrix[i][i]
    for j in range(m):
        if(i!=j):
            fp=fp+matrix[i][j]
            fn=fn+matrix[j][i]
        for k in range(m):
            tn=tn+matrix[j][k]
    tn=tn-(tp+fp+fn)
    acc=accuracy(tp,tn,fp,fn)
    e[acc]=i
    pre=precision(tp,fp)
    rec=recall(tp,fp)
    score=f1score(pre,rec)
    print("*******************for class ",d[i]," values are: ")
    print()
    print("tp tn fp tn :",tp ,tn ,fp ,fn)
    print("Accuracy is: ",acc)
    print("precision is: ",pre)
    print("Recall is: ",rec)
    print("F1 Score is: ",score)
    print()
    tp=tn=fp=fn=0
print("Class with maximum accuracy is :")
print(d[e[max(e)]])
    



