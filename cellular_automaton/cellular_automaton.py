def generate_state(
	length = 64,          # number of cells
	position : int = None # position of active cell
):
	if position == None:
		position = (length-1) // 2 # centered by default
	state = "." * position + '0' + "." * (length - position - 1)
	# we repeat '.' position times, put the active cell, then fill with '.'
	return state

def is_valid_state(state):
	return set(state) == {'.', '0'}

def apply_rule(rule, triplet):
	bits = (1 if i == '0' else 0 for i in triplet) # convert to binary digits
	# (bits is a generator, can be iterated only once)
	# here the magic begins
	pos = 0
	for bit in bits:
		pos = (pos << 1) | bit    # convert binary digits to an integer
		# we left-shift all previous bits by one position and then add the current bit at the rightmost position
	active = (rule >> pos) & 1    # read bit in position 'pos' from integer 'rule'
	# explanation: 'pos' is a 3-bit number which refers to the states of adjacent cells in a triplet;
	# 'rule' is a 8-bit number, so that each possible value of 'pos' is associated with a rule bit;
	# we access to a specific rule bit by right-shifting 'rule' by 'pos' positions
	# and taking only the rightmost (least significant) bit
	return '0' if active else '.' # convert back to character
	# no need for floody dictionaries :-)

def evolve(state, rule = 30, circular = False):
	if circular: # circular (periodic) boundary condition
		lstate = state[-1] + state[:-1] # right shift -> gives the states on the left
		rstate = state[1:] + state[0]   # left shift -> gives the states on the right
	else:        # copy cell on the border
		lstate = state[0] + state[:-1]
		rstate = state[1:] + state[-1]
	new_state = "".join(apply_rule(rule, triplet) for triplet in zip(lstate, state, rstate))
	# zip(., ., .) returns the ordered list of all triplets of adjacent cells
	# then we apply the rule for each cell and join all cells in the resulting list into a single string
	return new_state

def simulate(
	initial_state = generate_state(),
	nsteps = 31,     # number of steps
	rule = 30,       # rule to use (Wolfram rule by default)
	circular = False # boundary condition
):
	if not is_valid_state(initial_state):
		raise Exception("Initial state is not a valid state")

	states = [initial_state]     # add initial state to a list
	for i in range(nsteps):
		old_state = states[-1]   # last computed state
		new_state = evolve(old_state, rule, circular)
		states.append(new_state) # append new state to the list iteratively
	return states

if __name__ == "__main__": # this part is not executed when this file is imported from another place
	print( "\n".join(simulate()) )
	# join all the states returned by simulate() into a single string separated by a newline ('\n')





















