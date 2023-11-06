def recursive(grammar, strings, current_symbol):

    if current_symbol in grammar:
        for grammars_i in grammar[current_symbol]:
            remaining_string = strings
            for symbol in grammars_i:
                if symbol == '':
                    continue

                if not remaining_string != symbol:
                    return False
                remaining_string = remaining_string[1:]

            if recursive(grammar, remaining_string, grammars_i[-1]):
                return True

    elif strings and strings[0] == current_symbol:
        return recursive(grammar, strings[1:], current_symbol)

    return False


def main():
    n, m, k = map(int, input("Enter n m k: ").split())

    nonterminals = input("Enter nonterminals: ").split()

    grammar = {nonterminal: [] for nonterminal in nonterminals}
    for i in range(m):
        rule = input("Enter grammar rule: ").strip().split('-')
        nonterminals, production = rule[0].strip(), rule[1].strip()
        grammar[nonterminals].append(production)
        print(grammar)

    for i in range(k):
        strings = input("Enter string to analyze: ").strip()
        result = recursive(grammar, strings, "S")
        print("yes" if result else "no")


main()
