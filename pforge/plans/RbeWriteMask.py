from pforge.params.DXGIFormats import DXGIFormat
from pforge.params.BlendParams import BlendOp
from pforge.params.BlendParams import WMASK
from pforge.TestExpr import Cross, Param, TestDescriptor, Union

# Param values should be a list of objects:
#    which could be converted to string OR
#    enums.
# 
# ToName is a function to convert the param value to a string which is a part of test name.abs
#     e.g.: ToName=lambda v: f"b{v[0]}" for value v[0] of BlendOp generates "test_bt" and "test_bf" for values "true" and "false".
# ToArg is a function to convert the param value to a string for C++ code generation.
# ToDisplay is a function to convert the param value to a string for web view.


# ChMsk = Param(
#     "BlendEn",
#     ["r", "rg", "rgb"],
#     ToArg=lambda f: f"{f}",
# )


WMsk = Param(
    "WriteMask",
    [f for f in WMASK],
    ToArg=lambda f: f"{f.value.alias}",
)


Format = Param(
    "Format",
    [DXGIFormat.R8G8B8A8_UNORM, 
     DXGIFormat.R8G8_UNORM, 
     DXGIFormat.R16G16B16A16_FLOAT, 
     DXGIFormat.R16_FLOAT, 
     DXGIFormat.R32G32B32A32_FLOAT, 
     DXGIFormat.R32_FLOAT, 
     DXGIFormat.R11G11B10_FLOAT, 
     DXGIFormat.R10G10B10A2_UNORM,
     DXGIFormat.B5G6R5_UNORM,
     DXGIFormat.B5G5R5A1_UNORM,
     DXGIFormat.B4G4R4A4_UNORM,
     ],
    ToArg=lambda f: f"Format::{f.value.alias}",
)

clear_tests = TestDescriptor(
    # Test description
    SuiteName="RasterPsbBlend",

    # Post filter is not implemented yet.
    # PostFilter=lambda test: test.name.endswith("_f"),

    GenExpr=WMsk * Format,

    # C++ code generation
    Cpp_IncludeFiles=[
        "TestFramework/RbeBlendOperationTest.hpp",
    ],
    Cpp_TestGeneratorMacro="ADD_CHANNEL_MASK_TEST",
    Cpp_CaseNamePrefix="rbe_rtwmask_",
)
