n = int(input())
m = int(input())
s = int(input())
string = ""
for i in range(m+1, n, -1):
    if m %2==0:
        if m%3==0:
            if m!=s:
                if string =="":
                    string=string+ str(m)
                else:
                    string = string +" "+str(m)
            else:
                break
    m = m-1
print(string)
