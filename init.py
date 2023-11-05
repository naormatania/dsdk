import os
import numpy as np
import random
import pytorch as torch

# Custom colors
class clr:
    S = '\033[1m' + '\033[91m'
    E = '\033[0m'

    @staticmethod
    def color(cls, text):
        return cls.S + text + cls.E

def set_seed(seed = 1234):
    '''Sets the seed so results are the same every time we run.
    This is for REPRODUCIBILITY.'''
    np.random.seed(seed)
    random.seed(seed)
    torch.manual_seed(seed)
    torch.cuda.manual_seed(seed)
    # When running on the CuDNN backend, two further options must be set
    torch.backends.cudnn.deterministic = True
    torch.backends.cudnn.benchmark = False
    # Set a fixed value for the hash seed
    os.environ['PYTHONHASHSEED'] = str(seed)
