from pforge.params.DXGIFormats import DXGIFormat
from pforge.params.BlendParams import BlendOp
from pforge.params.BlendParams import LOGIC_OP
from pforge.TestExpr import Cross, Param, TestDescriptor, Union

# Param values should be a list of objects:
#    which could be converted to string OR
#    enums.
# 
# ToName is a function to convert the param value to a string which is a part of test name.abs
#     e.g.: ToName=lambda v: f"b{v[0]}" for value v[0] of BlendOp generates "test_bt" and "test_bf" for values "true" and "false".
# ToArg is a function to convert the param value to a string for C++ code generation.
# ToDisplay is a function to convert the param value to a string for web view.



Format = Param(
    "Format",
    [DXGIFormat.R8G8B8A8_UINT,  
     DXGIFormat.R16G16B16A16_UINT, 
     DXGIFormat.R32G32B32A32_UINT, 
     DXGIFormat.R10G10B10A2_UINT
     ],
    ToArg=lambda f: f"Format::{f.value.alias}",
)


LogicOp = Param(
    "LogicOP",
    [f for f in LOGIC_OP],
    ToArg=lambda f: f"nvrhi::LogicOp::{f.value.alias}",
)

clear_tests = TestDescriptor(
    # Test description
    SuiteName="RasterPsbBlend",

    # Post filter is not implemented yet.
    # PostFilter=lambda test: test.name.endswith("_f"),

    GenExpr=Format * LogicOp,

    # C++ code generation
    Cpp_IncludeFiles=[
        "TestFramework/RbeBlendOperationTest.hpp",
    ],
    Cpp_TestGeneratorMacro="ADD_LOGIC_OPERATION_TEST",
    Cpp_CaseNamePrefix="rbe_logic_",
)
