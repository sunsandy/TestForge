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

BlendOp = Param("BlendOp", ["true", "false"])




BlendEn = Param(
    "BlendEn",
    [""],
    ToArg=lambda f: f"true",
)

Format0 = Param(
    "Format",
    [DXGIFormat.R8_UNORM, 
     DXGIFormat.R8G8_UNORM, 
     DXGIFormat.R8G8B8A8_UNORM, 
     DXGIFormat.R16_FLOAT, 
     DXGIFormat.R16G16_FLOAT, 
     DXGIFormat.R16G16B16A16_FLOAT, 
     DXGIFormat.R32_FLOAT, 
     DXGIFormat.R32G32_FLOAT, 
     DXGIFormat.R32G32B32A32_FLOAT, 
     DXGIFormat.R11G11B10_FLOAT, 
     DXGIFormat.R10G10B10A2_UNORM,
     ],
    ToArg=lambda f: f"Format::{f.value.alias}",
)


UserParams = Param("UserParams", ["rt0_1010102unorm_rt1_8888unorm,", 
                                  "rt0_1010102unorm_rt1_8888srgb",
                                  "rt0_1010102unorm_rt1_111110float",
                                  "rt0_88888unorm_rt1_1616float_rt2_1010102unorm_rt3_8888srgb",
                                  "rt0_88888unorm_rt1_32323232float_rt2_1010102unorm_rt3_1010102float",
                                  "rt0_88888srgb_rt1_1010102_rt2_1010102unorm_rt3_111110float",
                                  "rt0_1010102unorm_rt1_8888srgb"
                                  ],
                                  ToArg=lambda f: f"FormatList",)


clear_tests = TestDescriptor(
    # Test description
    SuiteName="RasterPsbBlend",

    # Post filter is not implemented yet.
    # PostFilter=lambda test: test.name.endswith("_f"),

    GenExpr=UserParams,

    # C++ code generation
    Cpp_IncludeFiles=[
        "TestFramework/RbeBlendFormatTest.hpp",
    ],
    Cpp_TestGeneratorMacro="ADD_BLEND_FORMAT_TEST",
    Cpp_CaseNamePrefix="rbe_mrt_",
)
