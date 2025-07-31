from pforge.params.DXGIFormats import DXGIFormat
from pforge.params.BlendParams import DUALSRC
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
# Format = Param(
#     "Format",
#     [f for f in DXGIFormat if f.value.blendable==True],
#     ToArg=lambda f: f"Format::{f.name}",
# )

MissO1 = Param(
    "MissO1",
    [""],
    ToArg=lambda f: f"true",
)

UserParams = Param("UserParams", ["o1_miss_src1color", "o1_miss_invsrc1color"])

Format = Param(
    "Format",
    [DXGIFormat.R8G8B8A8_UNORM, DXGIFormat.R16G16B16A16_FLOAT, DXGIFormat.R32G32B32A32_FLOAT],
    ToArg=lambda f: f"Format::{f.value.alias}",
)


DualSrcOp = Param(
    "DualSrcOp",
    [f for f in DUALSRC],
    ToArg=lambda f: f"BlendFactor::{f.value.alias}",
)

clear_tests = TestDescriptor(
    # Test description
    SuiteName="RasterPsbBlend",

    # Post filter is not implemented yet.
    # PostFilter=lambda test: test.name.endswith("_f"),

    GenExpr=DualSrcOp * Format + UserParams,

    # C++ code generation
    Cpp_IncludeFiles=[
        "TestFramework/RbeBlendOperationTest.hpp",
    ],
    Cpp_TestGeneratorMacro="ADD_BLEND_DUAL_SRC_TEST",
    Cpp_CaseNamePrefix="rbe_dualsrc_",
)
