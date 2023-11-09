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
        ##result = recursive(grammar, strings, "S")
        result = recursive(grammar, strings, 'S')
        print("yes" if result else "no")


main()


-------
        
        for a in remaining_string:
            for symbol in grammar_rule:

                if symbol == '':   # '' == epsilon
                    continue

                    if a == symbol:
                        continue # Follow this instruction
                    else: # Next grammar_rule
                        if current_nonterminal_index+1 < len(nonterminal_array):
                            current_nonterminal = nonterminal_array[current_nonterminal_index+1]  # maybe recursive here doing the same
                        else:
                            break




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


        for symbol in grammar_rule:
            if symbol in nonterminal_array:
                result, current_nonterminal_index = recursive(grammar, string, nonterminal_array, current_nonterminal_index, symbol)
                if not result:
                    break
                else:
                    if current_nonterminal_index < len(string) and symbol == string[current_nonterminal_index]:
                        current_nonterminal_index += 1
                    else:
                        result = False
                        break
