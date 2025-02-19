import enum
from dataclasses import dataclass

@dataclass
class DXGIDescriptor:
    dtype: str
    size: int
    blend: bool # blending 
    #dtype: bool # logic

class DXGIFormat(enum.Enum):

    R8_UINT = DXGIDescriptor("uint", 1, False)
    R8_SINT = DXGIDescriptor("sint", 1, False)
    R8_UNORM = DXGIDescriptor("unorm", 1, True)
    R8_SNORM = DXGIDescriptor("snorm", 1, True)
    R8G8_UINT = DXGIDescriptor("uint", 2, False)
    R8G8_SINT = DXGIDescriptor("sint", 2, False)
    R8G8_UNORM = DXGIDescriptor("unorm", 2, True)
    R8G8_SNORM = DXGIDescriptor("snorm", 2, True)
    B4G4R4A4_UNORM = DXGIDescriptor("unorm", 2, True)
    R4G4B4A4_UNORM = DXGIDescriptor("unorm", 2, True)
    A4R4G4B4_UNORM = DXGIDescriptor("unorm", 2, True)
    B5G6R5_UNORM = DXGIDescriptor("unorm", 2, True)
    R5G6B5_UNORM = DXGIDescriptor("unorm", 2, True)
    B5G5R5A1_UNORM = DXGIDescriptor("unorm", 2, True)
    R5G6B5A1_UNORM = DXGIDescriptor("unorm", 2, True)
    A1R5G6B5_UNORM = DXGIDescriptor("unorm", 2, True)
    R8G8B8A8_UINT = DXGIDescriptor("uint", 4, False)
    R8G8B8A8_SINT = DXGIDescriptor("sint", 4, False)
    R8G8B8A8_UNORM = DXGIDescriptor("unorm", 4, True)
    R8G8B8A8_SNORM = DXGIDescriptor("snorm", 4, True)
    B8G8R8A8_UNORM = DXGIDescriptor("unorm", 4, True)
    R8G8B8A8_UNORM_SRGB = DXGIDescriptor("unorm", 4, True)
    B8G8R8A8_UNORM_SRGB = DXGIDescriptor("unorm", 4, True)
    R8G8B8_UNORM_SRGB = DXGIDescriptor("unorm", 3, True)
    R8G8_UNORM_SRGB = DXGIDescriptor("unorm", 2, True)
    R8_UNORM_SRGB = DXGIDescriptor("unorm", 1, True)
    R10G10B10A2_UNORM = DXGIDescriptor("unorm", 4, True)
    A2R10G10B10_UNORM = DXGIDescriptor("unorm", 4, True)
    A2B10G10R10_UNORM = DXGIDescriptor("unorm", 4, True)
    R11G11B10_FLOAT = DXGIDescriptor("float", 4, True)
    B10G11R11_FLOAT = DXGIDescriptor("float", 4, True)
    R16_UINT = DXGIDescriptor("uint", 2, False)
    R16_SINT = DXGIDescriptor("sint", 2, False)
    R16_UNORM = DXGIDescriptor("unorm", 2, True)
    R16_SNORM = DXGIDescriptor("snorm", 2, True)
    R16_FLOAT = DXGIDescriptor("float", 2, True)
    R16G16_UINT = DXGIDescriptor("uint", 4, False)
    R16G16_SINT = DXGIDescriptor("sint", 4, False)
    R16G16_UNORM = DXGIDescriptor("unorm", 4, True)
    R16G16_SNORM = DXGIDescriptor("snorm", 4, True)
    R16G16_FLOAT = DXGIDescriptor("float", 4, True)
    R16G16B16_UINT = DXGIDescriptor("uint", 8, True)
    R16G16B16_SINT = DXGIDescriptor("sint", 8, True)
    R16G16B16_FLOAT = DXGIDescriptor("float", 8, True)
    R16G16B16_UNORM = DXGIDescriptor("unorm", 8, True)
    R16G16B16_SNORM = DXGIDescriptor("snorm", 8, True)
    R16G16B16A16_UINT = DXGIDescriptor("uint", 8, False)
    R16G16B16A16_SINT = DXGIDescriptor("sint", 8, False)
    R16G16B16A16_FLOAT = DXGIDescriptor("float", 8, True)
    R16G16B16A16_UNORM = DXGIDescriptor("unorm", 8, True)
    R16G16B16A16_SNORM = DXGIDescriptor("snorm", 8, True)
    R32_UINT = DXGIDescriptor("uint", 4, False)
    R32_SINT = DXGIDescriptor("sint", 4, False)
    R32_FLOAT = DXGIDescriptor("float", 4, True)
    R32G32_UINT = DXGIDescriptor("uint", 8, False)
    R32G32_SINT = DXGIDescriptor("sint", 8, False)
    R32G32_FLOAT = DXGIDescriptor("float", 8, True)
    R32G32B32_UINT = DXGIDescriptor("uint", 12, False)
    R32G32B32_SINT = DXGIDescriptor("sint", 12, False)
    R32G32B32_FLOAT = DXGIDescriptor("float", 12, True)
    R32G32B32A32_UINT = DXGIDescriptor("uint", 16, False)
    R32G32B32A32_SINT = DXGIDescriptor("sint", 16, False)
    R32G32B32A32_FLOAT = DXGIDescriptor("float", 16, True)
    D16 = DXGIDescriptor("unorm", 2, False)
    D24S8 = DXGIDescriptor("unorm", 4, False)
    D24X8 = DXGIDescriptor("unorm", 4, False)
    D32 = DXGIDescriptor("float", 4, False)
    D32S8 = DXGIDescriptor("float", 4, False)
        

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
