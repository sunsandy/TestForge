from pforge.params.DXGIFormats import DXGIFormat
from pforge.params.BlendParams import SPNUM
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
    [f for f in SPNUM],
    ToArg=lambda f: f"SPNUM::{f.name}",
)

# PRECISION = Param(
#     "PRECISION",
#     ["fp16", "fp32", "unorm8", "fp1110"]
# )

Format = Param(
    "Format",
    [DXGIFormat.R8G8B8A8_UNORM, 
     DXGIFormat.R8G8B8A8_SNORM, 
     DXGIFormat.R16G16B16A16_FLOAT, 
     DXGIFormat.R16G16B16A16_UNORM, 
     DXGIFormat.R16G16B16A16_SNORM, 
     DXGIFormat.R32G32B32A32_FLOAT, 
     DXGIFormat.R11G11B10_FLOAT, 
     DXGIFormat.R10G10B10A2_UNORM,
     ],
    ToArg=lambda f: f"Format::{f.value.alias}",
)


##UserParams = Param("UserParams", ["rnd_fp16", "rnd_fp11"])

clear_tests = TestDescriptor(
    # Test description
    SuiteName="RasterPsbBlend",

    # Post filter is not implemented yet.
    # PostFilter=lambda test: test.name.endswith("_f"),

    GenExpr=SP_NUM * Format,

    # C++ code generation
    Cpp_IncludeFiles=[
        "TestFramework/RbeBlendOperationTest.hpp",
    ],
    Cpp_TestGeneratorMacro="ADD_SPN_WO_TEST",
    Cpp_CaseNamePrefix="rbe_snum_wo",
)
