import copy
import random

class Hat:
    def __init__(self, **kwargs):
        
        self.contents=[key for key,value in kwargs.items() for x in range(value)]
    
    def draw(self, balls):
        if balls>len(self.contents):
            return self.contents
        else:
            result=random.sample(self.contents, k=balls)
            for x in result:
                self.contents.remove(x)
            return result
        

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    
    expected=[key for key,value in expected_balls.items() for x in range(value)]
    counter=0
    
    for x in range(num_experiments):
        hat_copy=copy.deepcopy(hat)
        sample=sorted(hat_copy.draw(num_balls_drawn))
        it=iter(sample)
        check_list=all( x in it for x in sorted(expected))
        if check_list==True: counter+=1

    return counter/num_experiments