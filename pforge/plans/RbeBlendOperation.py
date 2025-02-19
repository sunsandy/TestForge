from pforge.params.DXGIFormats import DXGIFormat
from pforge.params.BlendParams import BlendOperation
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
Format = Param(
    "Format",
    [f for f in DXGIFormat if f.value.blend==True],
    ToArg=lambda f: f"Format::{f.name}",
)

BlendOP = Param(
    "BlendOP",
    [f for f in BlendOperation]
)

clear_tests = TestDescriptor(
    # Test description
    SuiteName="RasterPsbBlend",

    # Post filter is not implemented yet.
    # PostFilter=lambda test: test.name.endswith("_f"),

    GenExpr=BlendOP * Format,

    # C++ code generation
    Cpp_IncludeFiles=[
        "TestFramework/RbeBlendOperationTest.hpp",
    ],
    Cpp_TestGeneratorMacro="ADD_BLEND_OP_TEST",
    Cpp_CaseNamePrefix="rbe_blend_",
)
