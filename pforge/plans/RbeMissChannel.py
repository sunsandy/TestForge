from pforge.params.DXGIFormats import DXGIFormat
from pforge.params.BlendParams import BlendOp
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
    ["R8G8_UNORM", "R8G8B8A8_UNORM", "R16G16_FLOAT", "R16G16B16A16_FLOAT", "R32G32_FLOAT", "R32G32B32A32_FLOAT"]
)

PS_O = Param(
    "PS_O",
    ["oxyzw", "oxyz", "oxy"]
)

MissChannel = Param(
    "ColorType",
    ["srca", "dsta", "srcb"]
)

UserParams = Param("UserParams", 
                   ["dsta_oxyzw_r8g8_unorm", 
                    "dsta_oxyzw_r16g16_float",
                    "dsta_oxyzw_r32g32_float", 
                    "srca_oxyz_r8g8b8a8_unorm",        
                    "srca_oxyz_r16g16b16a16_float",        
                    "srca_oxyz_r32g32b16a16_float",        
                    "srcb_oxyz_r8g8b8a8_unorm",        
                    "srcb_oxyz_r16g16b16a16_float",    
                    "srcb_oxyz_r32g32b16a16_float"],
    ToArg=lambda f: f"RG8_UNORM",)

clear_tests = TestDescriptor(
    # Test description
    SuiteName="RasterPsbBlend",

    # Post filter is not implemented yet.
    # PostFilter=lambda test: test.name.endswith("_f"),

    GenExpr=UserParams,

    #GenExpr=PS_O * Format,

    # C++ code generation
    Cpp_IncludeFiles=[
        "TestFramework/RbeBlendOperationTest.hpp",
    ],
    Cpp_TestGeneratorMacro="ADD_BLEND_MISS_CHANNEL_TEST",
    Cpp_CaseNamePrefix="rbe_miss_ch_",
)
