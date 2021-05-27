import json

def load(path):
    # プラグインのjson読み込み
    f = open(path, "r")
    file = json.load(f)
    
    # キーからデータの取得
    rec = dict()
    rec["name"] = file["name"]
    rec["version"] = file["version"]
    rec["desc"] = file["description"]
    rec["path"] = str(path)
    
    return rec
        
        
def record(rec):
    try:
        f = open("plugins.json", "a")
        f.write()
    finally:
        f.close()

rec = load("sample.json")
print(rec)
record(rec)