import ast


def read_ab_file(path):
    with open(path) as content_file:
        content = content_file.read()
        return ast.literal_eval(content)


