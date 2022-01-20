"""perform test"""
import settings
import yaml


def read_yaml(file="config.yaml"):
    with open(file, "r", encoding="utf-8") as f:
        return yaml.load(f, Loader=yaml.FullLoader)


config = read_yaml()
for k, v in config.items():
    assert getattr(settings, k) == v, f"test failed for field : {k}"

print("test pass")
