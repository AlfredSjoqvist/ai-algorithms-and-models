# Artificial Intelligence Algorithms & Models

This repository collects a series of small but focused projects touching on the Foundations of Artificial Intelligence.  
Each folder contains a self contained experiment that implements a classic AI technique and evaluates it on a concrete task.

## Skills demonstrated

- Python based AI prototyping with Jupyter
- Design of autonomous agents and internal state representations
- State space search and path planning (uninformed and informed search)
- Knowledge representation with OWL and ontology modeling in Protégé
- Domain independent planning in PDDL using research planners (IPP and FF)
- Probabilistic reasoning and Bayesian networks
- Decision tree learning, evaluation and experiment design
- Reproducible experiments and written analysis of results

## Project overview

### intelligent-agents-pacman

Implements a Pacman style grid world agent that must clear all food in rooms of arbitrary size using only local percepts.  
The agent maintains an internal state, updates it from percepts such as `('clear', 'bump')`, and selects actions (`GoForward`, `GoLeft`, `GoRight`, `GoBack`, `Stop`) to systematically explore and clean the environment.

Focus:

- Agent architectures, state design and memory
- Handling partial observability and action failure
- Simple coverage strategies in unknown environments

---

### search-agents-path-planning

Builds a fully observable Pacman world where the agent plans its path through a maze that may contain randomly placed walls.  
The agent keeps track of its position, direction, food coordinates and action history, then uses a search strategy to generate a plan that eats all food.

Focus:

- Classical search algorithms on grid worlds
- State encoding and loop detection
- Plan execution and debugging of search based agents

---

### knowledge-representation-ontologies

Models small domains using OWL ontologies in Protégé.  
Part 1 defines a simple student and course ontology and uses reasoning to infer class memberships.  
Part 2 develops an animal ontology with classes like mammals, reptiles and carnivores and uses class expressions and restrictions to classify example animals.

Focus:

- OWL classes, individuals and properties
- Class expressions with existential and universal restrictions
- Practical use of Protégé and description logic reasoning

---

### automated-planning-pddl-logistics

Encodes logistics delivery scenarios in PDDL and solves them with the IPP and FF planners.  
Starts from a simple truck and package domain, then extends it with new vehicle types (for example mopeds and planes), additional locations, capacity constraints and more complex goals.

Focus:

- Domain and problem modeling in PDDL (STRIPS subset)
- Understanding strengths and weaknesses of different planners
- Experimenting with problem difficulty and action design

---

### probabilistic-logic-bayesian-networks

Uses a Bayesian network tool to model the safety of a nuclear power plant.  
The initial network is used to answer queries about failure modes and alarms, then extended with a model of the owner's escape car and finally a probabilistic model of a human safety officer.

Focus:

- Bayesian network structure design and conditional probability tables
- Probabilistic inference and effect of evidence
- Extending networks with new variables while keeping them interpretable

---

### decision-tree-learning

Runs experiments with decision tree learners on a small classification task in a notebook environment.  
The tree is trained and evaluated under different settings to study overfitting, generalisation and the impact of feature selection.

Focus:

- Decision tree learning and information gain
- Evaluation metrics and train test splits
- Interpreting tree structure and experiment results
