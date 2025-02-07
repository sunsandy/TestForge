#include <string>
#include <vector>
#include <iostream>
#include <utility>
#include "TestFramework.hpp"

struct PsbBlend_Test {
    RenderParams renderParams_;
    std::vector<float> vertices_;
    Color clear_color_;
    bool blend_en_;
    Format format_;
    std::string vs_;
    std::string ps_;
    GraphicsTestBase::Matching match_mode_;

    PsbBlend_Test(RenderParams const* renderParams, std::vector<float> const& vertices)
        : renderParams_(*renderParams), vertices_(vertices) {}

    void SetBlendEnable(bool blend_en, BlendOp blend_op, BlendFactor src_factor, BlendFactor dst_factor) {
        blend_en = blend_en;
        blend_op = blend_op;
        src_factor = src_factor;
        dst_factor = dst_factor;
    }
    void SetClearColor(Color const& color) {
        clear_color_ = color;
    }
    void SetRTFormat(Format format) {
        format_ = format;
    }
    void SetVS(std::string const& vs) {
        vs_ = vs;
    }
    void SetPS(std::string const& ps) {
        ps_ = ps;
    }
    void SetMatchMode(GraphicsTestBase::Matching match_mode) {
        match_mode_ = match_mode;
    }
    void Run()
    {
        std::cout << "Run - " 
            << " renderParams_:" << renderParams_.width << "x" << renderParams_.height 
            << " vertices_:" << vertices_.size()
            << " clear_color_:" << clear_color_.r << "," << clear_color_.g << "," << clear_color_.b << "," << clear_color_.a
            << " blend_en_:" << blend_en_ 
            << " format_:" << std::to_underlying(format_) 
            << " vs_:" << vs_ 
            << " ps_:" << ps_ 
            << " match_mode:" << std::to_underlying(match_mode_) 
            << std::endl;
    }
};

void test_blend_format(const std::string& name, bool blend_en, Format format)
{
    RenderParams renderParams = GetRenderParams(32, 32);

    std::vector<float> vertices = {
            0, 0, 0, 1, 0.5f, 0.5f, 0.5f, 1.0f,
            32, 0, 0, 1, 0.5f, 0.5f, 0.5f, 1.0f,
            0, 32, 0, 1, 0.5f, 0.5f, 0.5f, 1.0f,

            0, 0, 0, 1, 0.5f, 0.5f, 0.5f, 1.0f, 
            0, 32, 0, 1, 0.5f, 0.5f, 0.5f, 1.0f, 
            32, 32, 0, 1, 0.5f, 0.5f, 0.5f, 1.0f, 
    };

    Color clear_color = {0, 0, 0, 0};

    PsbBlend_Test test(&renderParams, vertices);
    test.SetBlendEnable(blend_en, BlendOp::Add, BlendFactor::SrcColor, BlendFactor::DstColor);
    test.SetClearColor(clear_color);
    test.SetRTFormat(format);
    test.SetVS("main_vs");
    test.SetPS("main_ps_pass");
    test.SetMatchMode(GraphicsTestBase::Matching::GoldenImage);
    test.Run();
}

#define ADD_BLEND_FORMAT_TEST(name, blend_en, format) FUNC_TEST(RasterPsbBlend, name, \
    "1 draw, draw 2 overlapped triangles with specific color,set different rt formats and blending is on") \
{ \
    test_blend_format(#name, (blend_en), (format)); \
}
