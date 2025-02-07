#include "TestFramework/BlendFormatTest.hpp"

ADD_BLEND_FORMAT_TEST(rbe_blend_r32g32b32a32_float, true, Format::RGBA32_FLOAT)
ADD_BLEND_FORMAT_TEST(rbe_blend_r32g32_float, true, Format::RG32_FLOAT)
ADD_BLEND_FORMAT_TEST(rbe_blend_r32_float, true, Format::R32_FLOAT)

ADD_BLEND_FORMAT_TEST(rbe_blend_r16g16b16a16_float, true, Format::RGBA16_FLOAT)
ADD_BLEND_FORMAT_TEST(rbe_blend_r16g16_float, true, Format::RG16_FLOAT)
ADD_BLEND_FORMAT_TEST(rbe_blend_r16_float, true, Format::R16_FLOAT)

ADD_BLEND_FORMAT_TEST(rbe_blend_r16g16b16a16_unorm, true, Format::RGBA16_UNORM)
ADD_BLEND_FORMAT_TEST(rbe_blend_r16g16_unorm, true, Format::RG16_UNORM)
ADD_BLEND_FORMAT_TEST(rbe_blend_r16_unorm, true, Format::R16_UNORM)

ADD_BLEND_FORMAT_TEST(rbe_blend_r16g16b16a16_snorm, true, Format::RGBA16_SNORM)
ADD_BLEND_FORMAT_TEST(rbe_blend_r16g16_snorm, true, Format::RG16_SNORM)
ADD_BLEND_FORMAT_TEST(rbe_blend_r16_snorm, true, Format::R16_SNORM)

ADD_BLEND_FORMAT_TEST(rbe_blend_r8g8b8a8_unorm_srgb, true, Format::SRGBA8_UNORM)

ADD_BLEND_FORMAT_TEST(rbe_blend_r8g8b8a8_unorm, true, Format::RGBA8_UNORM)
ADD_BLEND_FORMAT_TEST(rbe_blend_r8g8_unorm, true, Format::RG8_UNORM)
ADD_BLEND_FORMAT_TEST(rbe_blend_r8_unorm, true, Format::R8_UNORM)

ADD_BLEND_FORMAT_TEST(rbe_blend_r8g8b8a8_snorm, true, Format::RGBA8_SNORM)
ADD_BLEND_FORMAT_TEST(rbe_blend_r8g8_snorm, true, Format::RG8_SNORM)
ADD_BLEND_FORMAT_TEST(rbe_blend_r8_snorm, true, Format::R8_SNORM)

ADD_BLEND_FORMAT_TEST(rbe_blend_a8_unorm, true, Format::A8_UNORM)

ADD_BLEND_FORMAT_TEST(rbe_blend_r11g11b10_float, true, Format::R11G11B10_FLOAT)
ADD_BLEND_FORMAT_TEST(rbe_blend_r10g10b10a2_unorm, true, Format::R10G10B10A2_UNORM)
ADD_BLEND_FORMAT_TEST(rbe_blend_b5g6r5_unorm, true, Format::B5G6R5_UNORM)
ADD_BLEND_FORMAT_TEST(rbe_blend_b4g4r4a4_unorm, true, Format::BGRA4_UNORM)
ADD_BLEND_FORMAT_TEST(rbe_blend_b5g5r5a1_unorm, true, Format::B5G5R5A1_UNORM)

