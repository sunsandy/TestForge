import enum
from dataclasses import dataclass

@dataclass

class BlendOperation(enum.Enum):
    
    add = 1
    subrtact = 2
    revsubstract = 3
    min = 4
    max = 5
