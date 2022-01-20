"""scarpy-settings"""
import inspect

import yaml

__all__ = ["load_config"]


def read_yaml(file):

    with open(file, "r", encoding="utf-8") as f:
        return yaml.load(f, Loader=yaml.FullLoader)


def load_config(file="config.yaml"):
    caller_stack = inspect.stack()[1]  # get caller stack
    caller_frame = caller_stack[0]  # get caller frame
    caller_module = inspect.getmodule(caller_frame)
    config = read_yaml(file)
    for k in config:
        setattr(caller_module, k, config[k])
