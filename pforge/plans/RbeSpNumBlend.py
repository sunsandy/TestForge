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
SP_NUM = Param(
    "SP_NUM",
    ["ninf", "pinf", "nan", "maxval", "denorm", "zero"]
)

OP = Param(
    "OP",
    ["mp", "add", "sub"]
)


PRECISION = Param(
    "PRECISION",
    ["fp16", "fp32", "unorm8", "fp1110"]
)


clear_tests = TestDescriptor(
    # Test description
    SuiteName="RasterPsbBlend",

    # Post filter is not implemented yet.
    # PostFilter=lambda test: test.name.endswith("_f"),

    GenExpr=SP_NUM * PRECISION,

    # C++ code generation
    Cpp_IncludeFiles=[
        "TestFramework/RbeBlendOperationTest.hpp",
    ],
    Cpp_TestGeneratorMacro="ADD_SPECIAL_NUM_WO_TEST",
    Cpp_CaseNamePrefix="rbe_snum_wo_",
)
