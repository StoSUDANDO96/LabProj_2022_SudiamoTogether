import cellular_automaton as ca

def test_generation_valid_state():
	state = ca.generate_state()
	assert ca.is_valid_state(state)

def test_generation_single_active():
	state = ca.generate_state()
	num_active = sum(1 for i in state if i == '0')
	assert num_active == 1

def test_evolution_valid_state():
	state = ca.evolve(ca.generate_state())
	assert ca.is_valid_state(state)

def test_evolution_length():
	state = ca.generate_state()
	new_state = ca.evolve(state)
	assert len(state) == len(new_state)

def test_simulation_steps():
	nsteps = 35
	states = ca.simulate(nsteps=nsteps)
	assert len(states) == nsteps+1 # including initial state





















