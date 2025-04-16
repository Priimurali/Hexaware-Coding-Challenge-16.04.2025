def get_connection_string(filename):
    props = {}
    with open(filename, 'r') as file:
        for line in file:
            if '=' in line:
                key, val = line.strip().split('=', 1)
                props[key] = val
    return props
