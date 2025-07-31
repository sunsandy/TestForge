import enum
class DXGIDescriptor:
    def __init__(self, alias: str, dtype: str, size: int, colorable: bool, blendable: bool):
        self.alias = alias
        self.dtype = dtype
        self.size = size
        self.colorable = colorable
        self.blendable = blendable
    
class DXGIFormat(enum.Enum):
    R8_UINT = DXGIDescriptor("R8_UINT","uint", 1, True, False)
    R8_SINT = DXGIDescriptor("R8_SINT","sint", 1, True, False)
    R8_UNORM = DXGIDescriptor("R8_UNORM","unorm", 1, True, True)
    R8_SNORM = DXGIDescriptor("R8_SNORM","snorm", 1, True, True)
    R8G8_UINT = DXGIDescriptor("RG8_UINT","uint", 2, True, False)
    R8G8_SINT = DXGIDescriptor("RG8_SINT","sint", 2, True, False)
    R8G8_UNORM = DXGIDescriptor("RG8_UNORM","unorm", 2, True, True)
    R8G8_SNORM = DXGIDescriptor("RG8_SNORM","snorm", 2, True, True)
    B4G4R4A4_UNORM = DXGIDescriptor("BGRA4_UNORM","unorm", 2, True, True)
    R4G4B4A4_UNORM = DXGIDescriptor("RGBA4_UNORM","unorm", 2, True, True)
    A4R4G4B4_UNORM = DXGIDescriptor("ARGB4_UNORM","unorm", 2, True, True)
    A4B4G4R4_UNORM = DXGIDescriptor("ABGR4_UNORM","unorm", 2, True, True)
    B5G6R5_UNORM = DXGIDescriptor("B5G6R5_UNORM","unorm", 2, True, True)
    R5G6B5_UNORM = DXGIDescriptor("R5G6B5_UNORM","unorm", 2, True, True)
    B5G5R5A1_UNORM = DXGIDescriptor("B5G5R5A1_UNORM","unorm", 2, True, True)
    R5G5B5A1_UNORM = DXGIDescriptor("R5G5B5A1_UNORM","unorm", 2, True, True)
    A1B5G5R5_UNORM = DXGIDescriptor("A1B5G5R5_UNORM","unorm", 2, True, True)
    A1R5G5B5_UNORM = DXGIDescriptor("A1R5G5B5_UNORM","unorm", 2, True, True)
    R8G8B8_UINT = DXGIDescriptor("RGB8_UINT","uint", 3, True, False)
    R8G8B8_SINT = DXGIDescriptor("RGB8_SINT","sint", 3, True, False)
    R8G8B8_UNORM = DXGIDescriptor("RGB8_UNORM", "unorm", 3, True, True)
    R8G8B8_SNORM = DXGIDescriptor("RGB8_SNORM", "snorm", 3, True, True)
    R8G8B8A8_UINT = DXGIDescriptor("RGBA8_UINT","uint", 4, True, False)
    R8G8B8A8_SINT = DXGIDescriptor("RGBA8_SINT","sint", 4, True, False)
    R8G8B8A8_UNORM = DXGIDescriptor("RGBA8_UNORM", "unorm", 4, True, True)
    R8G8B8A8_SNORM = DXGIDescriptor("RGBA8_SNORM", "snorm", 4, True, True)
    B8G8R8A8_UNORM = DXGIDescriptor("BGRA8_UNORM", "unorm", 4, True, True)
    R8G8B8A8_UNORM_SRGB = DXGIDescriptor("SRGBA8_UNORM", "unorm", 4, True, True)
    R8G8B8_UNORM_SRGB = DXGIDescriptor("SRGB8_UNORM","unorm", 3, True, True)
    R8G8_UNORM_SRGB = DXGIDescriptor("SRG8_UNORM", "unorm", 2, True, True)
    R8_UNORM_SRGB = DXGIDescriptor("SR8_UNORM", "unorm", 1, True, True)
    R10G10B10A2_UNORM = DXGIDescriptor("R10G10B10A2_UNORM","unorm", 4, True, True)
    B10G10R10A2_UNORM = DXGIDescriptor("B10G10R10A2_UNORM","unorm", 4, True, True)
    R10G10B10A2_UINT = DXGIDescriptor("R10G10B10A2_UINT","unorm", 4, True, True)
    R11G11B10_FLOAT = DXGIDescriptor("R11G11B10_FLOAT","float", 4, True, True)
    R16_UINT = DXGIDescriptor("R16_UINT","uint", 2, True, False)
    R16_SINT = DXGIDescriptor("R16_SINT","sint", 2, True, False)
    R16_UNORM = DXGIDescriptor("R16_UNORM","unorm", 2, True, True)
    R16_SNORM = DXGIDescriptor("R16_SNORM","snorm", 2, True, True)
    R16_FLOAT = DXGIDescriptor("R16_FLOAT","float", 2, True, True)
    R16G16_UINT = DXGIDescriptor("RG16_UINT","uint", 4, True, False)
    R16G16_SINT = DXGIDescriptor("RG16_SINT","sint", 4, True, False)
    R16G16_UNORM = DXGIDescriptor("RG16_UNORM","unorm", 4, True, True)
    R16G16_SNORM = DXGIDescriptor("RG16_SNORM","snorm", 4, True, True)
    R16G16_FLOAT = DXGIDescriptor("RG16_FLOAT","float", 4, True, True)
    R16G16B16_UINT = DXGIDescriptor("RGB16_UINT","uint", 6, False, False)
    R16G16B16_SINT = DXGIDescriptor("RGB16_SINT","sint", 6, False, False)
    R16G16B16_FLOAT = DXGIDescriptor("RGB16_FLOAT","float", 6, True, True)
    R16G16B16_UNORM = DXGIDescriptor("RGB16_UNORM","unorm", 6, True, True)
    R16G16B16_SNORM = DXGIDescriptor("RGB16_SNORM","snorm", 6, True, True) 
    R16G16B16A16_UINT = DXGIDescriptor("RGBA16_UINT","uint", 8, True, False)
    R16G16B16A16_SINT = DXGIDescriptor("RGBA16_SINT","sint", 8, True, False)
    R16G16B16A16_FLOAT = DXGIDescriptor("RGBA16_FLOAT","float", 8, True, True)
    R16G16B16A16_UNORM = DXGIDescriptor("RGBA16_UNORM","unorm", 8, True, True)
    R16G16B16A16_SNORM = DXGIDescriptor("RGBA16_SNORM","snorm", 8, True, True)
    R32_UINT = DXGIDescriptor("R32_UINT","uint", 4, True, False)
    R32_SINT = DXGIDescriptor("R32_SINT","sint", 4, True, False)
    R32_FLOAT = DXGIDescriptor("R32_FLOAT","float", 4, True, True)
    R32G32_UINT = DXGIDescriptor("RG32_UINT","uint", 8, True, False)
    R32G32_SINT = DXGIDescriptor("RG32_SINT","sint", 8, True, False)
    R32G32_FLOAT = DXGIDescriptor("RG32_FLOAT","float", 8, True, True)
    R32G32B32_UINT = DXGIDescriptor("RGB32_UINT","uint", 12, True, False)
    R32G32B32_SINT = DXGIDescriptor("RGB32_SINT","sint", 12, True, False)
    R32G32B32_FLOAT = DXGIDescriptor("RGB32_FLOAT","float", 12, True, True)
    R32G32B32A32_UINT = DXGIDescriptor("RGBA32_UINT","uint", 16, True, False)
    R32G32B32A32_SINT = DXGIDescriptor("RGBA32_SINT","sint", 16, True, False)
    R32G32B32A32_FLOAT = DXGIDescriptor("RGBA32_FLOAT","float", 16, True, True)
    D16 = DXGIDescriptor("D16","unorm", 2, False, False)
    D24S8 = DXGIDescriptor("D24S8","unorm", 4, False, False)
    D24X8 = DXGIDescriptor("D24X8","unorm", 4, False, False)
    D32 = DXGIDescriptor("D32","float", 4, False, False)
    D32S8 = DXGIDescriptor("D32S8","float", 4, False, False)

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
