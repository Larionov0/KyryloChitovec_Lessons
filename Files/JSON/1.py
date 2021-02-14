import json

dct = {
    'Alex': ['math', 'swimming'],
    'Bob': ['fishing', 'football']
}

string = json.dumps(dct)
ob = json.loads(string)

print(dct)
print(ob)
