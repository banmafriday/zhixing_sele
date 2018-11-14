import yaml
import os

curpath = os.path.dirname(os.path.realpath(__file__))
ymPath = os.path.join(curpath, "t1.yaml")

f = open(ymPath, "r", encoding="utf-8")
cfg = f.read()
f.close()
print(type(cfg))
print(cfg)

a = yaml.load(cfg)
print(a)
print(type(a))