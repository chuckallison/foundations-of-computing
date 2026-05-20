# Implements the automaton "ends-with-b" in Figure 2–1 using a transition table
def ends_with_b(s):
    transitions = {('q0','a'):'q0', ('q0','b'):'q1',
                   ('q1','a'):'q0', ('q1','b'):'q1'}
    state = 'q0'
    for c in s:
        state = transitions[(state,c)]
    return state == 'q1'

print(ends_with_b('aabab')) # True
print(ends_with_b('aaba'))  # False
