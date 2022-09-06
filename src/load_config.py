"""Load configuration from .yaml file."""
import yaml
from rich import print

with open("./config.yml", "r") as f:
    conf = yaml.safe_load(f)
print(conf)
