import os
import yaml

def app_cfg(device= 'leidian1', yamlname="zhixing.yaml"):
    curpath = os.path.dirname(os.path.realpath(__file__))
    yamlpath = os.path.join(curpath,  yamlname)
    f = open(yamlpath , "r", encoding="utf-8")
    a = f.read()
    f.close()
    # 把yaml文件转字典
    d = yaml.load(a)  # list对象，多个配置
    for i in d:
        if device in i['desc']:
            return i

if __name__ == '__main__':
     a = app_cfg(device= 'leidian2')
     print(a)
