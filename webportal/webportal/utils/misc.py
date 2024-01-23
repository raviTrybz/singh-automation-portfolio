import yaml


def yaml_coerce(value):
    # Convert value to proper python
    if isinstance(value, str):
        # yaml.load returns a python object (we are just creating some quick yaml data with)
        # Converts string dict "{"'apples': 1, 'bacon': 2}" to python dict
        # Useful because sometimes we need to stringify settings this way (like in Dockerfile)
        return yaml.load(f'dummy:  {value}', Loader=yaml.SafeLoader)['dummy']

    return value
