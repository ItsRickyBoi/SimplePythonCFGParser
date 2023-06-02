class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def is_empty(self):
        return len(self.items) == 0

    def read_top(self):
        return self.items[-1]


def ll1_parser(input_string):
    stack = Stack()
    stack.push('#')
    stack.push('S')
    input_string += '#'
    i = 0

    parsing_table = {
        'S': {
            'x': 'AB',
            'y': 'AB',
            'a': 'CD',
            'b': 'CD',
        },
        'A': {
            'x': 'xA',
            'y': 'y',
            'a': '-',
            'b': '-',
        },
        'B': {
            'x': 'x',
            'y': 'yB',
            'a': '-',
            'b': '-',
        },
        'C': {
            'x': '-',
            'y': '-',
            'a': 'aD',
            'b': 'b',
        },
        'D': {
            'x': '-',
            'y': '-',
            'a': 'a',
            'b': 'bC',
        },
    }

    while not stack.is_empty():
        top = stack.read_top()

        if top == input_string[i]:
            stack.pop()
            i += 1
        elif top in parsing_table:
            production = parsing_table[top].get(input_string[i])
            stack.pop()
            if production != '-':
                for char in reversed(production):
                    stack.push(char)
        else:
            return 'Declined'

        if i >= len(input_string):
            return 'Declined'

    return 'Accepted'


def print_table(parsing_table):
    headers = [''] + list(parsing_table['S'].keys())
    rows = [headers]
    for non_terminal, production in parsing_table.items():
        row = [non_terminal] + list(production.values())
        rows.append(row)

    max_lengths = [max(map(len, col)) for col in zip(*rows)]
    format_string = ' | '.join(['{{:{}}}'.format(length)
                               for length in max_lengths])
    table = [format_string.format(*row) for row in rows]

    print('\n'.join(table))


parse_table = {
    'S': {
        'x': 'AB',
        'y': 'AB',
        'a': 'CD',
        'b': 'CD',
    },
    'A': {
        'x': 'xA',
        'y': 'y',
        'a': '-',
        'b': '-',
    },
    'B': {
        'x': 'x',
        'y': 'yB',
        'a': '-',
        'b': '-',
    },
    'C': {
        'x': '-',
        'y': '-',
        'a': 'aD',
        'b': 'b',
    },
    'D': {
        'x': '-',
        'y': '-',
        'a': 'a',
        'b': 'bC',
    },
}

grammar_rules = [
    "S -> AB | CD",
    "A -> xA | y",
    "B -> yb | x",
    "C -> aD | b",
    "D -> bC | a"
]

print("LL(1) with simple notations:")
for rule in grammar_rules:
    print(rule + "\n")

print('Parsing Table:')
print_table(parse_table)
input_string = input('Enter the input string: ')

if not input_string.endswith("#"):
    input_string += "#"

result = ll1_parser(input_string)
print('Result:', result)
