NO_OF_CHARS = 256


def get_ascii(char):
    return ord(char)


def get_next_state(str_to_find, pat_len, state, x):
    # helper func to get upcoming state

    # If the upcoming character is the same as the next state, simply increment the state
    if state < pat_len and x == get_ascii(str_to_find[state]):
        return state + 1

    # Starting value
    i = 0

    # Start from the largest possible value and
    # stop when you find a prefix which is also suffix
    for next_state in range(state, 0, -1):
        if get_ascii(str_to_find[next_state - 1]) == x:
            while i < next_state - 1:
                if str_to_find[i] != str_to_find[state - next_state + 1 + i]:
                    break
                i += 1
            if i == next_state - 1:
                return next_state
    return 0


def compute_transition_states(pat_to_search, pat_len):
    trans_states = [[0 for i in range(NO_OF_CHARS)] for _ in range(pat_len + 1)]

    for state in range(pat_len + 1):
        for x in range(NO_OF_CHARS):
            z = get_next_state(pat_to_search, pat_len, state, x)
            trans_states[state][x] = z

    return trans_states


def search_pattern(pattern_to_search, full_txt):
    pattern_len = len(pattern_to_search)
    full_len = len(full_txt)
    transition_states = compute_transition_states(pattern_to_search, pattern_len)

    state = 0
    state_found = False

    for i in range(full_len):
        state = transition_states[state][get_ascii(full_txt[i])]
        if state == pattern_len:
            state_found = True
            print("Pattern found at index: {}".format(i - pattern_len + 1))

    if not state_found:
        print ("The pattern doesn't exist")


# Program initiator
def main():
    full_text = "Hello there! My name is Mohammed Siddiqui."
    pattern_to_find = "Siddiqui"

    search_pattern(pattern_to_find, full_text)


main()
