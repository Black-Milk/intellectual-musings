from mesa import Agent, Model
from mesa.time import SimultaneousActivation
from mesa.space import MultiGrid
from mesa.datacollection import DataCollector
from mesa.visualization.modules import CanvasGrid
from mesa.visualization.ModularVisualization import ModularServer


class LifeAgent(Agent):
    """An agent representing a single cell in the Game of Life."""

    def __init__(self, pos, model, is_alive=True):
        super().__init__(pos, model)
        self.pos = pos
        self.is_alive = is_alive
        self.next_state = self.is_alive

    def step(self):
        """Compute the next state based on the current state and neighbors."""

        # Find the neighbors of the current cell within a Moore neighborhood
        neighbors = self.model.grid.get_neighbors(
            self.pos, moore=True, include_center=False
        )

        # Count the number of alive neighbors within neighborhood
        alive_neighbors = sum(neighbor.is_alive for neighbor in neighbors)

        # Apply the rules of the Game of Life
        if self.is_alive:
            if alive_neighbors < 2 or alive_neighbors > 3:
                self.next_state = False  # Cell dies
        else:
            if alive_neighbors == 3:
                self.next_state = True  # Cell becomes alive

    def advance(self):
        """Update the state to the next state."""
        self.is_alive = self.next_state


class LifeModel(Model):
    """Model class for the Game of Life."""

    def __init__(self, width, height, density=0.2):
        super().__init__()  # Properly initialize the parent Model class
        self.grid = MultiGrid(width, height, torus=True)
        self.schedule = SimultaneousActivation(self)
        self.datacollector = DataCollector(agent_reporters={"Alive": "alive"})

        for contents, (x, y) in self.grid.coord_iter():
            is_alive = self.random.random() < density
            agent = LifeAgent((x, y), self, is_alive=is_alive)
            self.grid.place_agent(agent, (x, y))
            self.schedule.add(agent)

    def step(self):
        """Advance the model by one step."""
        self.schedule.step()
        self.datacollector.collect(self)


def agent_portrayal(agent):
    """Portrayal method for visualization."""
    portrayal = {"Shape": "rect", "w": 1, "h": 1, "Filled": "true"}
    if agent.is_alive:
        portrayal["Color"] = "black"
    else:
        portrayal["Color"] = "white"
    portrayal["Layer"] = 0
    return portrayal


if __name__ == "__main__":
    # Parameters for the grid and server
    width, height = 100, 100
    grid = CanvasGrid(agent_portrayal, width, height, 500, 500)
    server = ModularServer(
        LifeModel,
        [grid],
        "Game of Life",
        {"width": width, "height": height, "density": 0.2},
    )
    # Launch the server
    server.port = 8521
    server.launch()
