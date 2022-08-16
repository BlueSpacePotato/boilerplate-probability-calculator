import copy
import random
# Consider using the modules imported above.

class Hat:

  def __init__(self, **kwargs):
    self.contents = [key for key, value in kwargs.items() for _ in range(value)]

  def draw(self, n):
    # check for n min ! not in unittest testet, but needed for the final test ...
    n = min(n, len(self.contents))
    drawn = [self.contents.pop(random.randrange(len(self.contents))) for i in range(n)]
    return drawn

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
  
  m = 0
  for _ in range(num_experiments):
      tmp_hat = copy.deepcopy(hat)
      balls_drawn = tmp_hat.draw(num_balls_drawn)
      balls = sum([1 for key, value in expected_balls.items() if balls_drawn.count(key) >= value])
      m += 1 if balls == len(expected_balls) else 0

  return m / num_experiments

  