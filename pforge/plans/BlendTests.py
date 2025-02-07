from pforge.params.DXGIFormats import DXGIFormat
from pforge.TestExpr import Cross, Param, TestDescriptor, Union

BlendOp = Param("BlendOp", ["true"], ToName=lambda _: None)
Format_4B = Param(
    "Format",
    [f for f in DXGIFormat if f.value.size == 4],
    ToArg=lambda f: f"Format::{f.name}",
)
Format_8B = Param("Format", [f for f in DXGIFormat if f.value.size == 8])

blend_tests = TestDescriptor(
    # Test description
    SuiteName="BlendTests",
    TestGen=BlendOp * Format_4B,
    # C++ code generation
    Cpp_IncludeFiles=[
        "TestFramework/BlendFormatTest.hpp",
    ],
    Cpp_TestGeneratorMacro="ADD_BLEND_FORMAT_TEST",
    Cpp_CaseNamePrefix="rbe_blend_",
)
