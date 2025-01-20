import re

def parse_fact(line):
    line = line.strip()
    name = re.match(r'^\s*([a-zA-Z0-9_]+)\s*\((.*)\)\s*$', line).group(1)
    args = re.match(r'^\s*([a-zA-Z0-9_, ]+)\s*$', re.match(r'^\s*([a-zA-Z0-9_]+)\s*\((.*)\)\s*$', line).group(2)).group(1)
    args = [arg.strip() for arg in re.split(r', *', args)]
    return name, args

def match_args(fact_args, query_args):
    if len(fact_args) != len(query_args):
        return False
    for fact_arg, query_arg in zip(fact_args, query_args):
        if query_arg == '_' or fact_arg == query_arg:
            continue
        if re.match(r'^\s*_\s*$', query_arg):
            continue
        if fact_arg != query_arg:
            return False
    return True

database = {}
while True:
    line = input().strip()
    if not line:
        break
    name, args = parse_fact(line)
    if name not in database:
        database[name] = []
    database[name].append(args)

while True:
    try:
        line = input().strip()
    except EOFError:
        break
    query_name, query_body = re.match(r'^\s*([a-zA-Z0-9_]+)\s*\((.*)\)\s*$', line).groups()
    query_args = [arg.strip() for arg in re.split(r', *', query_body)]
    count = 0
    for name, facts in database.items():
        if name == query_name and len(facts) == len(query_args):
            for fact in facts:
                if match_args(fact, query_args):
                    count += 1
    print(count)