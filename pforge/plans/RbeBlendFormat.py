from pforge.params.DXGIFormats import DXGIFormat
from pforge.TestExpr import Cross, Param, TestDescriptor, Union

# Param values should be a list of objects:
#    which could be converted to string OR
#    enums.
# 
# ToName is a function to convert the param value to a string which is a part of test name.abs
#     e.g.: ToName=lambda v: f"b{v[0]}" for value v[0] of BlendOp generates "test_bt" and "test_bf" for values "true" and "false".
# ToArg is a function to convert the param value to a string for C++ code generation.
# ToDisplay is a function to convert the param value to a string for web view.
# BlendOp = Param("BlendOp", ["true", "false"])
BlendEn = Param(
    "BlendEn",
    [""],
    ToArg=lambda f: f"true",
)


Format = Param(
    "Format",
    [f for f in DXGIFormat if f.value.blendable==True],
    ToArg=lambda f: f"Format::{f.value.alias}",
)


clear_tests = TestDescriptor(
    # Test description
    SuiteName="RasterPsbBlend",

    # Post filter is not implemented yet.
    # PostFilter=lambda test: test.name.endswith("_f"),

    GenExpr=BlendEn*Format,

    # C++ code generation
    Cpp_IncludeFiles=[
        "TestFramework/RbeBlendFormatTest.hpp",
    ],
    Cpp_TestGeneratorMacro="ADD_BLEND_FORMAT_TEST",
    Cpp_CaseNamePrefix="rbe_blend_",
)
