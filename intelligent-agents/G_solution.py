class AgentWithState(BaseAgent):

    
    def __init__(self):
        self.latest_turn = "Right"
        self.previous_action_bump = False
    
    class State:
        def __init__(self):
            self.bump = False
            self.previous_action = ""

        def __repr__(self):
            if self.bump:
                return self.previous_action + " resulted in a bump"
            else:
                return self.previous_action

            
            

    def update_state_with_percept(self, percept, state):
        """Update the state based on percept"""
        if percept[1] == "bump":
            state.bump = True
        else:
            state.bump = False
        return state

    

    def choose_action(self, state):
        """Return an action"""
        
        # If the agents latest turn was to the right and the agent just bumped
        # into a wall, make it turn left twice.
        if self.latest_turn == "Right":
            
            if state.bump:
                
                # If the agent bumps into a wall twice in a row, 
                # it means it has cleared the entire map.
                if self.previous_action_bump:
                    return "Stop"
                
                self.previous_action_bump = True
                return "GoLeft"
            
            else:
                self.previous_action_bump = False

            if state.previous_action == "GoLeft":
                self.latest_turn = "Left"
                return "GoLeft"
        
        # If the agents latest turn was to the left and the agent just bumped
        # into a wall, make it turn right twice.
        if self.latest_turn == "Left":
            
            if state.bump:
                
                # If the agent bumps into a wall twice in a row, 
                # it means it has cleared the entire map.
                if self.previous_action_bump:
                    return "Stop"
                
                self.previous_action_bump = True
                return "GoRight"
            
            else:
                self.previous_action_bump = False
            
            if state.previous_action == "GoRight":
                self.latest_turn = "Right"
                return "GoRight"
        
        # The agent's default action is to go forward if no other condition is satisfied.
        return "GoForward"
        
        

    def update_state_with_action(self, action, state):
        state.previous_action = action
        # Print the representation (i.e. __repr__) of the state
        print(state)
        return state