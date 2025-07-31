import enum
from dataclasses import dataclass

@dataclass

class BlendOp(enum.Enum):
    add = 1
    subrtact = 2
    revsubstract = 3
    min = 4
    max = 5

class StateDescriptor:
    def __init__(self, alias: str):
        self.alias = alias

class CHMSK_O(enum.Enum):
    r = StateDescriptor("O_R")
    rg = StateDescriptor("O_RG")
    rgb = StateDescriptor("O_RGB")

class LOGIC_OP(enum.Enum):
    CLEAR = StateDescriptor("CLEAR")    
    SET= StateDescriptor("SET")           
    COPY= StateDescriptor("COPY")         
    COPY_INVERTED= StateDescriptor("COPY_INVERTED")
    NOOP= StateDescriptor("NOOP")         
    INVERT= StateDescriptor("INVERT")       
    AND= StateDescriptor("AND")          
    NAND= StateDescriptor("NAND")         
    OR= StateDescriptor("OR")           
    NOR= StateDescriptor("NOR")          
    XOR= StateDescriptor("XOR")           
    EQUIV= StateDescriptor("EQUIV")        
    AND_REVERSE= StateDescriptor("AND_REVERSE")  
    AND_INVERTED= StateDescriptor("AND_INVERTED") 
    OR_REVERSE= StateDescriptor("OR_REVERSE")   
    OR_INVERTED= StateDescriptor("OR_INVERTED")  


class WMASK(enum.Enum):
    NONE = StateDescriptor("WM_NONE")    
    R= StateDescriptor("WM_R")           
    G= StateDescriptor("WM_G")         
    B= StateDescriptor("WM_B")
    A= StateDescriptor("WM_A")  
    GA= StateDescriptor("WM_GA")         
    RB= StateDescriptor("WM_RB")       
    RG= StateDescriptor("WM_RG")          
    RGB= StateDescriptor("WM_RGB")         
    GBA= StateDescriptor("WM_GBA")           
    RBA= StateDescriptor("WM_RBA")               

class DUALSRC(enum.Enum):
    SRC1_COLOR= StateDescriptor("Src1Color")           
    SRC1_ALPHA= StateDescriptor("Src1Alpha")         
    INVSRC1_COLOR= StateDescriptor("InvSrc1Color")
    INVSRC1_ALPHA= StateDescriptor("Src1Alpha")  


class SPNUM(enum.Enum):   
    _PINF= StateDescriptor("_PINF")           
    _NINF= StateDescriptor("_NINF")         
    _NAN= StateDescriptor("_NAN")
    _DENRM= StateDescriptor("_DENRM")  
    _PMAX= StateDescriptor("_PMAX")         
    _NMAX= StateDescriptor("_NMAX")         
    _TINY= StateDescriptor("_TINY")
    _RND_PNORM= StateDescriptor("_RND_PNORM")
    _RND_NNORM= StateDescriptor("_RND_NNORM")
        