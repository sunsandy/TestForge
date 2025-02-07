from TestExpr import Param, Cross, Union, TestDescriptor
from params.DXGIFormats import DXGIFormat

BlendOp = Param("BlendOp", ["true"])
Format_4B = Param("Format", [f for f in DXGIFormat if f.value.size == 4])
Format_8B = Param("Format", [f for f in DXGIFormat if f.value.size == 8])
MSAA = Param("MSAA", [1, 2, 4, 8])
Width = Param("Width", [1024, 2048, 4096])
Height = Param("Height", [1024, 2048, 4096])
UserParams = Param("UserParams", ["a, b", "a, c", "1, 2, 3"])

Tests = TestDescriptor(
    # Test description
    SuiteName = "BlendFormat",
    GenExpr = BlendOp * Format_4B * MSAA + (BlendOp * Format_8B * Union(Width, Height) + UserParams).Doc("Some documentation here, too."),

    # C++ code generation
    Cpp_IncludeFiles = [
        "TestFramework/BlendFormatTest.hpp",
    ],
    Cpp_TestGeneratorMacro = "ADD_BLEND_FORMAT_TEST",
    Cpp_CaseNamePrefix = "rbe_blend",
)
