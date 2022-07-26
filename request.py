import requests
import json
a=requests.get("http://saral.navgurukul.org/api/courses")
b=a.json()
with open("courses.json","w") as a:
    json.dump(b,a,indent=4)
i=0
id=[]
while i<len(b["availableCourses"]):
    Name=b["availableCourses"][i]["name"]
    Id=b["availableCourses"][i]["id"]
    id.append(Id)
    print(i," ",Name," ",Id)
    i=i+1
choose=int(input("enter the number:"))
r=0
k=requests.get("http://saral.navgurukul.org/api/courses/"+id[choose]+"/exercises")
m=k.json()
l=[]
for i in m["data"]:
    print(r,i["slug"])
    l.append(i["slug"])
    r=r+1
choose2=int(input("enter the slug number"))
n=requests.get("http://saral.navgurukul.org/api/courses/"+str(choose)+"exercises/getbyslug?slug="+l[choose2])
o=n.json()

l1=[]
c=0
for i in o["slug"]:
    print(c,i["slug"])
    l1.append(i["slug"])
    c=c+1
print(o) 
