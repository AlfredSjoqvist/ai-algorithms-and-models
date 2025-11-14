class AgentWithState(BaseAgent):

    def __init__(self):
        # The agent must remember its latest turning action 
        # as the next one will be in the opposite direction.
        self.latest_turn = "Right"
        
        # The agent will remember the size of the map so it 
        # knows when to turn.
        self.map_length = 0
        self.map_height = 0
        
        # The step_counter and step_counter_max determines the agent's
        # turning condition during the clearing phase.
        self.step_counter = 0
        self.step_counter_max = 0
        
        # The line_counter and line_counter_max determine the agent's
        # stopping condition if it ever comes to the clearing phase.
        self.line_counter = 0
        self.line_counter_max = 0
        
        # If the agent chooses to clear the map vertically it has to
        # turn left at the initiation of the clearing phase, whether
        # the agent turns or not is determined by this variable:
        self.initial_left_turn = None
        
        # When the agent turns during the clearing phase, it must turn
        # twice so it has to keep in its memory whether the last action
        # was a turn.
        self.is_turning = False
        
        # The clearing consist of three phases: "length_scan", "height_scan" and "clear" in 
        # which the agent will behave differently.
        self.phase = "length_scan"

        
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

        # The phase where the agent scans the length of the map.
        if self.phase == "length_scan":
            
            self.map_length += 1
            
            # When the agent reaches the wall, it will turn left and scan upwards instead.
            if state.bump:
                self.phase = "height_scan"
                return "GoLeft"
            
            return "GoForward"
        
        # The phase where the agent scans the height of the map.
        if self.phase == "height_scan":
            
            self.map_height += 1
            
            # When the agent reaches the wall, the size of the map
            # is known and the clearing phase can start.
            if state.bump:
                self.phase = "clear"
                
                # The agent will clear differently 
                # depending on if the map is wide or high.
                if self.map_height > self.map_length:
                    
                    # The agent's turning condition will be determined by the
                    # map's height if the map is more high than wide.
                    self.step_counter_max = self.map_height - 2
                    
                    # The agent's turning condition will be determined by the
                    # map's length if the map is more high than wide.
                    self.line_counter_max = self.map_length - 2
                    
                    # The agent's first turn will be to the right if it is to
                    # clear the map vertically, after it has turned left on
                    # the start of the clearing phase.
                    self.latest_turn = "Left"
                    self.initial_left_turn = True
                    
                else:
                    
                    # Check the documentation for the if-statement 
                    # above and think vice versa:
                    self.step_counter_max = self.map_length - 3
                    self.line_counter_max = self.map_height - 2
                    self.latest_turn = "Right"
                
                # If the map has the height or length of one, the clearing phase 
                # doesn't have to be initiated since the entire map has already been covered.
                if self.map_length == 1 or self.map_height == 1:
                    return "Stop"
                
                # Do a left turn before the clearing phase to avoid another bump.
                return "GoLeft"
            
            # If the agent hasn't yet reached the wall, just keep going forward.
            return "GoForward"
        
        # The phase where the agent with the knowledge of the map size, clears the remains of it.
        if self.phase == "clear":
            
            # This can only be the case on a 2x2 map, and at this point it
            # means that the agent has cleared the entire map.
            if self.step_counter_max == 0:
                return "Stop"
            
            # If the step counter has reached it's maximal value,
            # the agent's turning condition has been fulfilled.
            if self.step_counter == self.step_counter_max:
            
                # This means that the end of the map has been reached and
                # the agent therefore stops to avoid an unecessary bump.
                if self.line_counter == self.line_counter_max:
                    return "Stop"
                
                # If the agent is about to turn, it means that an
                # entire line has been surpassed.
                self.line_counter += 1
                
                # Reset the step counter so the agent doesn't get
                # stuck in the turning condition.
                self.step_counter = 0
                
                # Make the agent remember that it has to turn again next state.
                self.is_turning = True
                
                # With the knowledge of the direction the last turn was in,
                # determine which direction the next turn is going to be.
                if self.latest_turn == "Right":
                    return "GoLeft"
                elif self.latest_turn == "Left":
                    return "GoRight"
            
            # If the agent is about to go in a direction which isn't tangentical
            # to the clearing direction, add one to the step counter.
            self.step_counter += 1
            
            # The agent always performs turning actions twice, therefore we
            # have to check if it is in the middle of a turn.
            if self.is_turning:
                
                # Set this to false so the agent doesn't turn more than twice.
                self.is_turning = False
                
                # With the knowledge of the direction the last turn was in,
                # determine which direction the next turn is going to be.
                # Also remember which turn it just made so the next turn can
                # be in the opposite direction.
                if self.latest_turn == "Right":
                    self.latest_turn = "Left"
                    return "GoLeft"
                elif self.latest_turn == "Left":
                    self.latest_turn = "Right"
                    return "GoRight"
            
            # If the map is to be cleared vertically, the agent has to do an 
            # inital turn to the left before starting to go forward.
            if self.initial_left_turn:
                self.initial_left_turn = False
                return "GoLeft"
            
            # If no other condition is satisfied, the agent just keeps on moving forward.
            return "GoForward"
            
                
    def update_state_with_action(self, action, state):
        state.previous_action = action
        # Print the representation (i.e. __repr__) of the state
        print(state)
        return state