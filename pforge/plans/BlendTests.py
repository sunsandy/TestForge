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
BlendOp = Param("BlendOp", ["true", "false"], ToName=lambda v: f"b{v[0]}")
Format_4B = Param(
    "Format",
    [f for f in DXGIFormat if f.value.size == 4],
    ToArg=lambda f: f"Format::{f.name}",
)
Format_8B = Param("Format", [f for f in DXGIFormat if f.value.size == 8])

blend_tests = TestDescriptor(
    # Test description
    SuiteName="BlendTests",

    # Expression to generate test cases.
    # * operator is Cross (a.k.a Cartesian product) 
    # + operator is Union
    GenExpr=BlendOp * Format_4B,        

    # Post filter is not implemented yet.
    # PostFilter=lambda test: test.name.endswith("_f"),

    # C++ code generation
    Cpp_IncludeFiles=[
        "TestFramework/BlendFormatTest.hpp",
    ],
    Cpp_TestGeneratorMacro="ADD_BLEND_FORMAT_TEST",
    Cpp_CaseNamePrefix="rbe_blend_",
)
