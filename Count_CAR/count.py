f = open("text.txt" ,"r")

STR =f.read()
print("Total Characters:" , len(STR))
print("Total Word: ",len(STR.split()))
print("Total Line: ",len(STR.split("\n")))