def parse_input(data):
    authors = {}
    for line in data.splitlines():
        parts = line.split()
        author_name = parts[0]
        coauthors = parts[1:]
        authors[author_name] = set(coauthors)
    return authors

def find_erdos_numbers(authors):
    erdos_number = { 'PAUL_ERDOS': 0 }
    queue = [ 'PAUL_ERDO