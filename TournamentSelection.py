import random

from Selection import Selection

class TournamentSelection(Selection):

    def __init__(self, population, tournament_size):
        super().__init__(population)
        self.tournament_size = tournament_size

    def select(self):
        selected_individuals = []

        for _ in range(len(self.population)):
            tournament = random.sample(self.population, self.tournament_size)
            
            if self.minimization:
                best_individual = min(tournament)
            else:
                best_individual = max(tournament)
                
            selected_individuals.append(best_individual)

        return selected_individuals
