import graphviz

def getPrecedence(c):
    precedence = ''
    match c:
        case '(':
            precedence =  1
        case '|':
            precedence =  2
        case '°':
            precedence =  3
        case '?':
            precedence =  4
        case '*':
            precedence =  4
        case '+':
            precedence =  4
        case '^':
            precedence =  5
        case _:
            precedence =  6
    return precedence

def formatRegEx(regex):
    res = ''
    allOperators = ['|', '?', '+', '*', '^']
    binaryOperators = ['^', '|']

    unique_characters = []

    for i in range(len(regex)):
        c1 = regex[i]

        if c1 not in allOperators and c1 not in binaryOperators and c1 not in unique_characters and c1 != '(' and c1 != ')' and c1 != 'ε':
            unique_characters.append(c1)
        
        if (i + 1 < len(regex)):
            c2 = regex[i + 1]
            
            res += c1

            if c1 != '(' and c2 != ')' and c2 not in allOperators and c1 not in binaryOperators:
                res += '°'

    res += regex[-1]
    
    return res, unique_characters

def infixToPostfix(regex):
    left_count = 0
    right_count = 0
    validate = True

    for i in range(len(regex)):
        c1 = regex[i]

        if c1 == '(':
            left_count += 1
        if c1 == ')':
            right_count += 1
    
    if left_count != right_count:
        validate = False
    
    if '(|' in regex or '|)' in regex or '||' in regex:
        validate = False

    if validate:
        postfix = ''
        stack = []
        formattedRegEx, unique_characters = formatRegEx(regex)

        for character in formattedRegEx:
            match character:
                case '(':
                    stack.append(character)

                case ')':
                    while stack[-1] != '(':
                        postfix += stack.pop()

                    stack.pop()
                
                case _:
                    while len(stack) > 0:
                        peekedChar = stack[-1]
                        peekedCharPrecedence = getPrecedence(peekedChar)
                        currentCharPrecedence = getPrecedence(character)

                        if (peekedCharPrecedence >= currentCharPrecedence):
                            postfix += stack.pop()
                        else:
                            break
                    
                    stack.append(character)
        
        while len(stack) > 0:
            postfix += stack.pop()
        
        return postfix, unique_characters
    else:
        print('There is a mistake with the input string')
        return ''

def graphNFA(postfix):
    if len(postfix) > 0:
        nfa_stack = []

        nfa = graphviz.Digraph('NFA', filename='NFA', format='png')
        nfa.attr(rankdir='LR', size='20')
        counter = 1

        for c in postfix:
            match c:
                case '|':
                    new_nfa = []

                    up_nfa = nfa_stack[-2]
                    down_nfa = nfa_stack[-1]

                    start_point = up_nfa[0][0] - 1

                    diference = 0

                    while up_nfa[-1][1] >= down_nfa[0][0] + diference:
                        diference += 1

                    new_down_nfa = []

                    for edges in down_nfa:
                        new_down_nfa.append([edges[0] + diference, edges[1] + diference, edges[2]])
                    
                    new_nfa.append([start_point, up_nfa[0][0], 'ε'])
                    new_nfa.append([start_point, new_down_nfa[0][0], 'ε'])

                    for edges in up_nfa:
                        new_nfa.append(edges)
                    
                    for edges in new_down_nfa:
                        new_nfa.append(edges)
                    
                    final_point = new_down_nfa[-1][1] + 1

                    new_nfa.append([up_nfa[-1][1], final_point,'ε'])
                    new_nfa.append([new_down_nfa[-1][1], final_point,'ε'])

                    nfa_stack.pop()
                    nfa_stack.pop()
                    nfa_stack.append(new_nfa)

                case '°':
                    #for this code, '°' has the same function as '.' in postfix format

                    new_nfa = []
                    first_nfa = nfa_stack[-2]
                    second_nfa = nfa_stack[-1]

                    for edges in first_nfa:
                        new_nfa.append(edges)
                    
                    first_last_point = first_nfa[-1][1]
                    second_first_point = second_nfa[0][0]
                    
                    dif = 0

                    if first_last_point >= second_first_point:
                        while first_last_point > second_first_point:
                            second_first_point += 1
                            dif += 1

                    new_nfa.append([first_last_point, second_first_point, 'ε'])
                    
                    #dif += 1

                    for edges in second_nfa:
                        new_nfa.append([edges[0] + dif, edges[1] + dif, edges[2]])

                    nfa_stack.pop()
                    nfa_stack.pop()
                    nfa_stack.append(new_nfa)

                case '?':
                    new_nfa = []

                    actual_nfa = nfa_stack[-1]

                    initial_point = actual_nfa[0][0]
                    final_point = actual_nfa[-1][1]

                    new_nfa.append([initial_point, final_point, 'ε'])

                    for edges in actual_nfa:
                        new_nfa.append(edges)

                    nfa_stack.pop()
                    nfa_stack.append(new_nfa)

                case '*':
                    new_nfa = []
                    
                    actual_nfa = nfa_stack[-1]

                    initial_point = actual_nfa[0][0] - 1
                    final_point = actual_nfa[-1][1] + 1

                    new_nfa.append([initial_point, initial_point + 1, 'ε'])

                    for edges in actual_nfa:
                        new_nfa.append(edges)
                    
                    new_nfa.append([final_point - 1, initial_point + 1, 'ε'])
                    new_nfa.append([initial_point, final_point, 'ε'])
                    new_nfa.append([final_point - 1, final_point, 'ε'])

                    nfa_stack.pop()
                    nfa_stack.append(new_nfa)

                case '+':
                    new_nfa = []

                    actual_nfa = nfa_stack[-1]

                    initial_point = actual_nfa[0][0] - 1
                    final_point = actual_nfa[-1][1] + 1

                    new_nfa.append([initial_point, initial_point + 1, 'ε'])

                    for edges in actual_nfa:
                        new_nfa.append(edges)
                    
                    new_nfa.append([final_point - 1, initial_point + 1, 'ε'])
                    new_nfa.append([initial_point, final_point, 'ε'])
                    new_nfa.append([final_point - 1, final_point, 'ε'])
                    
                    new_nfa.append([final_point, final_point + 1, 'ε'])           

                    dif = new_nfa[-1][1] - initial_point - 1

                    for edges in actual_nfa:
                        new_nfa.append([edges[0] + dif, edges[1] + dif, edges[2]])
                    
                    nfa_stack.pop()
                    nfa_stack.append(new_nfa)
                    
                case '^':
                    continue
                case _:
                    new_nfa = []
                    new_nfa.append([counter, counter+1, c])
                    nfa_stack.append(new_nfa)
                    counter += 2

        star_node = nfa_stack[0][0][0]
        final_node = nfa_stack[0][-1][1]
        star_diference = 0

        while star_node + star_diference < 0:
            star_diference += 1
        
        NFA = []

        for node in nfa_stack[0]:
            NFA.append([node[0] + star_diference, node[1] + star_diference, node[2]])
        
        
        nfa.attr('node', shape='circle', color = 'lightblue2', style = 'filled')
        nfa.node(str(star_node + star_diference))

        nfa.attr('node', shape='doublecircle', color = 'black', fillcolor='white')
        nfa.node(str(final_node + star_diference))
        
        nfa.attr('node', shape='circle', color = 'black', fillcolor='white')
        
        print('-------------------------TABLA DE TRANSCISIONES-------------------------')
        for node in nfa_stack[0]:
            print(node[0] + star_diference,',',node[2],',',node[1] + star_diference)
            nfa.edge(str(node[0] + star_diference), str(node[1] + star_diference), label=node[2])

        nfa.view()
        

        return NFA
        
def get_lambda_transitions(character, states, NFA):
    nodes = []

    for state in states:
        for connections in NFA:
            if state == connections[0] and connections[2] == character:
                nodes.append(connections[1])

    for state in nodes:
        for connections in NFA:
            if state == connections[0] and connections[2] == 'ε' and connections[1] not in nodes:
                nodes.append(connections[1])

    nodes.sort()
    #print(nodes)
    return nodes

def graph_sub_DFA(NFA, characters):
    new_states = []
    initial_new_state = []

    start_state = NFA[0][0]
    final_state = NFA[-1][1]

    new_edges = []
    new_states_fixed = []
    final_states = []
    state_counter = 0

    initial_new_state.append(start_state)

    for state in initial_new_state:
        for connections in NFA:
            if state == connections[0] and connections[2] == 'ε' and state != connections[1] and connections[1] not in initial_new_state:
                initial_new_state.append(connections[1])
    
    new_states.append(initial_new_state)
    new_states_fixed.append('S'+str(state_counter))

    if final_state in initial_new_state:
        final_states.append('S'+str(state_counter))

    for state in new_states:
        for character in characters:
            transition = get_lambda_transitions(character, state, NFA)
            
            if transition not in new_states:
                new_states.append(get_lambda_transitions(character, state, NFA))
                state_counter += 1
                new_states_fixed.append('S'+str(state_counter))

                if final_state in transition:
                    final_states.append('S'+str(state_counter))
            
            new_edges.append([new_states_fixed[new_states.index(state)], new_states_fixed[new_states.index(transition)], character])
    
    # print(initial_new_state)
    # print(new_states)
    # print(new_states_fixed)
    # print(final_states)
    # print(new_edges)
    # print('\n')

    
    nfd_sub = graphviz.Digraph('NFD_sub', filename='NFD_sub', format='png')
    nfd_sub.attr(rankdir='LR', size='20')

    nfd_sub.attr('node', shape='doublecircle', color = 'black', fillcolor='white')
    for node in final_states:
        nfd_sub.node(node)
    
    nfd_sub.attr('node', shape='circle', color = 'black', fillcolor='white')
    
    print('-------------------------TABLA DE TRANSCISIONES-------------------------')
    for node in new_edges:
        print(node[0],',',node[2],',',node[1])
        nfd_sub.edge(node[0], node[1], label=node[2])

    nfd_sub.view()
    

    return new_edges, new_states_fixed, final_states

def minimization(subgroups, transitions, final_states, DFA, states):
    final_states = final_states
    DFA = DFA
    states = states

    new_transitions = {}
    states_combinations = []
    new_subgroups = []

    for sub_group in subgroups:
        for node in sub_group:
            nodes_connected = []

            for connections in transitions[node]:
                nodes_connected.append(connections[0])
            
            if node not in final_states:
                nodes_connected.append('n')
            else:
                nodes_connected.append('f')
            
            if nodes_connected not in states_combinations:
                states_combinations.append(nodes_connected)
                new_subgroups.append([node])
            else:
                new_subgroups[states_combinations.index(nodes_connected)].append(node)

    for state in states:
        connections = []

        for node in DFA:
            if state == node[0]:
                connection = []

                for subgroup in new_subgroups:
                    if node[1] in subgroup:
                        connection.append(new_subgroups.index(subgroup))

                connection.append(node[2])
                connections.append(connection)
        
        new_transitions[state] = connections

    # print('\n')
    # print(new_transitions)
    # print(new_subgroups)
    # print('\n')

    if new_transitions != transitions:
        return minimization(new_subgroups, new_transitions, final_states, DFA, states)
    
    #minimization(new_subgroups, new_transitions, final_states, DFA, states)
    else:
        return new_transitions, new_subgroups

def minimize_dfa(DFA, states, final_states):
    sub_groups = []

    non_final_states = []

    transitions = {}

    for state in states:
        connections = []

        for node in DFA:
            if state == node[0]:
                connection = []
                connection.append(node[1])
                connection.append(node[2])
                connections.append(connection)
        
        transitions[state] = connections

        if state not in final_states:
            non_final_states.append(state)
    
    # print(dead_states)
    # print(final_states)
    sub_groups.append(non_final_states)
    sub_groups.append(final_states)

    for state in states:
        connections = []

        for node in DFA:
            if state == node[0]:
                connection = []
                if node[1] in non_final_states:
                    connection.append(0)
                else:
                    connection.append(1)
                connection.append(node[2])
                connections.append(connection)
        
        transitions[state] = connections

    x, y = minimization(sub_groups, transitions, final_states, DFA, states)
    
    # print(x)
    # print(y)

    
    sub_groups_concatenate = []

    for sub_group in y:
        final_text = '{'
        for node in sub_group:
            final_text += node

            if node != sub_group[-1]:
                final_text += ','
            else:
                final_text += '}'
        
        sub_groups_concatenate.append(final_text)
    
    # print(sub_groups_concatenate)
    # print(x)

    final_transitions = []

    for sub_group in y:
        first_state = sub_group[0]
        for connections in x[first_state]:
            final_transitions.append([sub_groups_concatenate[y.index(sub_group)], sub_groups_concatenate[connections[0]], connections[1]])

    #print(final_transitions)

    
    nfd_min = graphviz.Digraph('NFD_min', filename='NFD_min', format='png')
    nfd_min.attr(rankdir='LR', size='20')

    nfd_min.attr('node', shape='doublecircle', color = 'black', fillcolor='white')

    for sub_group in y:
        first_state = sub_group[0]
        if first_state in final_states:
            #print(sub_groups_concatenate[y.index(sub_group)])
            nfd_min.node(sub_groups_concatenate[y.index(sub_group)])
    # for node in final_states:
    #     nfd_sub.node(node)
    
    nfd_min.attr('node', shape='circle', color = 'black', fillcolor='white')
    
    print('-------------------------TABLA DE TRANSCISIONES-------------------------')
    for node in final_transitions:
        print(node[0],',',node[2],',',node[1])
        nfd_min.edge(node[0], node[1], label=node[2])

    nfd_min.view()
    
    
    return x, y

def nfd_sub_sim(nfd, w, final_states, unique_characters):
    print('\nINICIANDO SIMULACION')
    accepted = True
    initial_state = nfd[0][0]
    w_list = []
    last_transition = []

    for c in w:
        w_list.append(c)

    while len(w_list) != 0:
        current_character = w_list[0]
        if current_character not in unique_characters:
            accepted = False
            break
        else:
            for transitions in nfd:
                if initial_state == transitions[0] and current_character == transitions[2]:
                    initial_state = transitions[1]
                    print(transitions)
                    last_transition = transitions
                    break
            try:
                w_list.pop(0)
            except IndexError:
                print('Finalizado')

    #print('Ultima transicion', last_transition)
    if last_transition[1] not in final_states:
        accepted = False

    if accepted:
        print('The string was accepted')
    else:
        print('The string wasnt nos accepted')

def nfd_min_sim(nfd, subgroups, final_states, w, unique_characters):
    print('\nINICIANDO SIMULACION')
    accepted = True
    initial_state = 'S0'
    w_list = []
    last_transition = []

    for c in w:
        w_list.append(c)
    
    while len(w_list) != 0:
        current_character = w_list[0]
        if current_character not in unique_characters:
            accepted = False
            break
        else:
            for transitions in nfd[initial_state]:
                if current_character == transitions[1]:
                    initial_state = subgroups[transitions[0]][0]
                    print(transitions)
                    last_transition = transitions
                    break
            try:
                w_list.pop(0)
            except IndexError:
                print('Finalizado')

    # print('Last', last_transition)
    # print(subgroups[last_transition[0]])
    if subgroups[last_transition[0]][0] not in final_states:
        accepted = False

    if accepted:
        print('The string was accepted')
    else:
        print('The string wasnt nos accepted')

prueba = 'a'
postfix, unique_characters = infixToPostfix(prueba)

nfa = graphNFA(postfix)

DFA, states, final_states = graph_sub_DFA(nfa, unique_characters)

nfd_min, subgroups = minimize_dfa(DFA, states, final_states)


#print(nfa)
#print(unique_characters)

#graphNFA(infixToPostfix(prueba))
#print(infixToPostfix(prueba))
#ε

#(a|b)*(b|a)*abb
# ((ε|a)b*)*
# (.|;)*-/.(.|;)*
# (x|t)+((a|m)?)+ 
# (\"(.(;(.;(.|;)+)*)*)*)

c1 = [
    'bbabb',
    'babb',
    'aaaaaaaaaabbbbbbabababababababababababababbb',
    'abb'
]

c2 = ['a',
'aba',
'abba'] 

c3 = [    
    '.;-/.',
    '-/..;',
    '-/.',
    ';;;;;;;......;.;.;.;.;.;.;./.;.;.;.;.;'
]

c4 = [    
    'x',
    'txm',
    'ma',
    'a'
]

c5 = [
    '\".;.;.',
'\".;.;;.',
'\".;.;',
'\".;;.'
]


# for cadena in c5:
#     nfd_sub_sim(DFA, cadena, final_states, unique_characters)

for cadena in c5:
    nfd_min_sim(nfd_min, subgroups, final_states, cadena, unique_characters)

