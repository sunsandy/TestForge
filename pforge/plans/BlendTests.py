from TestExpr import Param, Cross, Union, TestDescriptor
from params.DXGIFormats import DXGIFormat

BlendOp = Param("BlendOp", ["true"])
Format_4B = Param("Format", [f for f in DXGIFormat if f.value.size == 4])
Format_8B = Param("Format", [f for f in DXGIFormat if f.value.size == 8])

Tests = TestDescriptor(
    # Test description
    SuiteName = "BlendFormat",
    TestGen = BlendOp * Format_4B,

    # C++ code generation
    Cpp_IncludeFiles = [
        "TestFramework/BlendFormatTest.hpp",
    ],
    Cpp_TestGeneratorMacro = "ADD_BLEND_FORMAT_TEST",
    Cpp_CaseNamePrefix = "rbe_blend",
)
