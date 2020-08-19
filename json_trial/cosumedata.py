import json
import jsource as js

data = json.loads(js.newdata)
# print(type(data))

for x in data:
    # if x["date"] == 20200816:
    #     continue
    print(x['date'])

