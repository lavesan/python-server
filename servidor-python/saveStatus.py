import json

# string para json

def saveJson(status):
    name = 'alguém'
    classes = 'Cálculo 3'
    description = 'Fala muito e não fala nada'
    correction = '2'
    jsonString = { "name": name, "classes": classes, "description": description, "correction": correction }
    print(jsonString)
    # dictionary para json
    print(json.dumps(jsonString))
    # json para dictionary
    print(json.loads(json.dumps(jsonString)))
saveJson('a')