import json

path="ESMapper"

for line in open(path) :
    #print line.strip()
    js=json.loads(line.strip())
    for str1 in js["esQuerys"]:
        print str1["jsonPath"]
