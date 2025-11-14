# pacmanAgents.py
# ---------------
# Licensing Information: Please do not distribute or publish solutions to this
# project. You are free to use and extend these projects for educational
# purposes. The Pacman AI projects were developed at UC Berkeley, primarily by
# John DeNero (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# For more info, see http://inst.eecs.berkeley.edu/~cs188/sp09/pacman.html

from pacman import Directions
from game import Agent
import copy
import random
import game
import util
import time
from graphicsUtils import *


class BaseAgent(game.Agent):
    solution = None
    printing = False

    def registerInitialState(self, state):
        """AgentState is stored in state"""
        self._dir = 0
        self._dirsMap = {(1,0) : "East",
                         (0,-1) : "South",
                         (-1,0) : "West",
                         (0,1) : "North"}
        self._dirs = [(1,0), (0,-1), (-1,0), (0,1)]
        self._percept = ("clear", None)
        self._actions = ["GoRight", "GoLeft", "GoForward", "GoBack"]
        start_map = {}

        # Get all walls
        walls = state.data.layout.walls.asList()
        for wall in walls: start_map[wall] = "w"

        # Get all food
        food = state.data.layout.food.asList()
        for f in food: start_map[f] = "*"

        # Set map
        self._state = self.State((1,1), (1,0), start_map)

        
    def getAction(self, state):
        """Get the next action. Note that the state passed here is used only
        to identify legal actions."""
        self._state = self.update_state_with_percept(self._percept, self._state)
        action = self.choose_action(copy.deepcopy(self._state))
        self._state = self.update_state_with_action(action, self._state)

        # Map the action
        do = self.mapAction(action, state.getLegalPacmanActions())
        return do

    def mapAction(self, action, legalActions):
        """Map vacuum action to pacman action"""
        d = self._dir
        if action == "GoRight": d += 1
        elif action == "GoLeft": d -= 1
        elif action == "GoBack": d += 2
        elif action == "GoForward": pass
        elif action == "Stop": return "Stop"
        else: return "Nothing"
        d %= 4
        
        do = self._dirsMap[self._dirs[d]]
        if do in legalActions:
            self._dir = d
        return do

    def update_state_with_percept(self, percept, state):
        """Update the state based on percept"""
        return state
    
    def choose_action(self, state):
        """Return action from actions list"""
        if self.printing:
            state.print_state()
        action = ""
        if self.mode == "keyboard":
            while True:
                keys = wait_for_keys()
                if "Up" in keys:
                    action = "GoForward"
                elif "Down" in keys:
                    action = "GoBack"
                elif "Left" in keys:
                    action = "GoLeft"
                elif "Right" in keys:
                    action = "GoRight"
                if action != "": break
        elif self.mode == "random":
            sleep(0.5)
            action = random.choice(["GoRight", "GoLeft", "GoForward", "GoBack"])
        elif self.mode == "search":
            if self.solution == None:
                self.solution = self.search(state)
                print("Found solution:", self.solution)
            if len(self.solution) == 0:
                return "Stop"
            else:
                action = self.solution[0]

        return action
    
    def update_state_with_action(self, action, state):
        """Update the state based on the action performed"""
        if self.solution != None and self.solution != []:
            self.solution.pop(0)

        if action == "GoRight":
            new_state = state.move_right()
        elif action == "GoLeft":
            new_state = state.move_left()
        elif action == "GoForward":
            new_state = state.move_forward()
        elif action == "GoBack":
            new_state = state.move_back()
        else:
            return state

        if new_state == state:
            print("Error: Only copies of a state should be returned")
            
        if new_state != None:
            return new_state
        
        return state

    class State:
        def print_state(self):
            print("*** State ***")
            print("Position: ", self.get_position())
            print("Direction:", self.get_direction())
            print("Actions:  ", self.get_actions())
            print("Food:     ", self.get_food(), "\n")
