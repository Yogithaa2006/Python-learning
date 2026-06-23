students={
    "Arun": 85,
    "Priya": 92,
    "Kavin": 78,
    "Meena": 88,
    "Rahul": 92
}
highest_mark=max(students.values())
avg = sum(students.values())/len(students)
unique_mark=set(students.values() )
toppers = []

for name, mark in students.items():
    if mark == highest_mark:
        toppers.append(name)
        toppers.append(mark)
       
        
toppers_detail=tuple(toppers)
for name,mark in students.items():
    print(name,":",mark)
print("Highest score: ",highest_mark)
print("unique marks: ",unique_mark)
print("Toppers details: ",toppers_detail)
