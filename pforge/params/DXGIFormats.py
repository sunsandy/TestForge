import enum
from dataclasses import dataclass

@dataclass
class DXGIDescriptor:
    dtype: str
    size: int

class DXGIFormat(enum.Enum):
    RGBA32_FLOAT = DXGIDescriptor("float", 16)
    RGB32_FLOAT = DXGIDescriptor("float", 12)
    R32_FLOAT = DXGIDescriptor("float", 4)
    RGBA16_FLOAT = DXGIDescriptor("float", 8)
    RGB16_FLOAT = DXGIDescriptor("float", 6)
    R16_FLOAT = DXGIDescriptor("float", 2)
    RGBA16_UNORM = DXGIDescriptor("uint", 8)
    RGB16_UNORM = DXGIDescriptor("uint", 6)
    R16_UNORM = DXGIDescriptor("uint", 2)
    RGBA16_SNORM = DXGIDescriptor("int", 8)
    RGB16_SNORM = DXGIDescriptor("int", 6)
    R16_SNORM = DXGIDescriptor("int", 2)
    RGBA8_UNORM = DXGIDescriptor("uint", 4)
    RGB8_UNORM = DXGIDescriptor("uint", 3)
    R8_UNORM = DXGIDescriptor("uint", 1)
    RGBA8_SNORM = DXGIDescriptor("int", 4)
    RGB8_SNORM = DXGIDescriptor("int", 3)
    R8_SNORM = DXGIDescriptor("int", 1)
    A8_UNORM = DXGIDescriptor("uint", 1)

    def SRGB(self):
        return ("SRGB" in self.name)

    def Channels(self):
        channels = self.name.split("_")[0]
        return set(channels) & {"R", "G", "B", "A", "X"}

    def IsUnorm(self):
        return ("UNORM" in self.name)

    def IsSnorm(self):
        return ("SNORM" in self.name)

    def IsFloat(self):
        return ("FLOAT" in self.name)

    def IsUint(self):
        return ("UINT" in self.name)
