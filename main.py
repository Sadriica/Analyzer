def recursive(grammar, string, nonterminal_array, current_nonterminal_index):

    current_nonterminal = nonterminal_array[current_nonterminal_index]

    if current_nonterminal in grammar:
        for grammar_rule in grammar[current_nonterminal]:
            remaining_string = string  # Think line can be removed - it's a duplicate from string
            for symbol in grammar_rule:  # symbol == a

                if symbol == '':  # '' == epsilon
                    continue

                if remaining_string == symbol:
                    return False
                remaining_string = remaining_string[1:]

            if recursive(grammar, remaining_string, grammar_rule[-1], current_nonterminal_index):  # Dont get it
                return True

    elif string and string[0] == current_nonterminal:
        return recursive(grammar, string[1:], current_nonterminal, current_nonterminal_index)

    return False


def main():
    n, m, k = map(int, input("Enter n m k: ").split())

    nonterminals = input("Enter nonterminals: ").split()
    nonterminals_array = []
    for valor in nonterminals:
        nonterminals_array.append(valor)

    print(nonterminals_array)

    grammar = {nonterminal: [] for nonterminal in nonterminals}
    for i in range(m):
        rule = input("Enter grammar rule: ").strip().split('-')
        nonterminals, production = rule[0].strip(), rule[1].strip()
        grammar[nonterminals].append(production)
        print(grammar)

    for i in range(k):
        strings = input("Enter string to analyze: ").strip()
        # result = recursive(grammar, strings, "S")
        result = recursive(grammar, strings, nonterminals_array, 0)
        print("yes" if result else "no")


main()
