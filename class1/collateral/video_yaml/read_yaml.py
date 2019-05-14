
import yaml

def read_yaml(filename):
    with open(filename) as f:
        return yaml.safe_load(f)

def write_yaml(filename, output, style=None):
    with open(filename, "wt") as f:
        if style=="compressed":
            yaml.dump(output, f, default_flow_style=True)
        else:
            yaml.dump(output, f, default_flow_style=False)

