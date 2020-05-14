import json
cat = ['car', 'bus', 'person', 'bike', 'truck', 'motor', 'train', 'rider', 'traffic sign', 'traffic light']
def extract(jsonfile):
    file = open(jsonfile)
    info = json.load(file)
    objects = info['frames'][0]['objects']
    res = []
    obj = []
    for i in objects:
        if i['category'] in cat:
            obj.append(int(i['box2d']['x1']))
            obj.append(int(i['box2d']['y1']))
            obj.append(int(i['box2d']['x2']))
            obj.append(int(i['box2d']['y2']))
            obj.append(i['category'])
            res.append(obj)
            obj = []
    return res

