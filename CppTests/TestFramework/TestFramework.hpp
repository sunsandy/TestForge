#include <string>
#include <vector>
#include <cstdint>
#include <functional>
#include <iostream>
enum class BlendOp: uint32_t {
    Add,
    Sub,
    RevSub,
    Min,
    Max,
};

enum class BlendFactor: uint32_t {
    Zero,
    One,
    SrcColor,
    SrcAlpha,
    DstColor,
    DstAlpha,
};

enum class Format: uint32_t {
    RGBA32_FLOAT,
    RGB32_FLOAT,
    R32_FLOAT,
    RGBA16_FLOAT,
    RGB16_FLOAT,
    R16_FLOAT,
    
    RG32_FLOAT,
    RG16_FLOAT,
    
    RGBA16_UNORM,
    RG16_UNORM,
    R16_UNORM,
    RGBA16_SNORM,
    RG16_SNORM,
    R16_SNORM,
    
    SRGBA8_UNORM,
    RGBA8_UNORM,
    RG8_UNORM,
    R8_UNORM,
    RGBA8_SNORM,
    RG8_SNORM,
    R8_SNORM,
    A8_UNORM,
    
    R11G11B10_FLOAT,
    R10G10B10A2_UNORM,
    B5G6R5_UNORM,
    BGRA4_UNORM,
    B5G5R5A1_UNORM
};

struct RenderParams {
    uint32_t width;
    uint32_t height;
};

struct Color {
    float r;
    float g;
    float b;
    float a;
};

namespace GraphicsTestBase {
    enum class Matching {
        GoldenImage,
        NoMatch,
    };
}

inline RenderParams GetRenderParams(uint32_t width, uint32_t height) {
    return {width, height};
}

struct TestDriver {
    TestDriver() = default;

    static TestDriver& Instance() {
        static TestDriver instance;
        return instance;
    }

    void AddTest(std::string name, std::function<void()> func) {
        tests_.push_back(std::make_pair(name, func));
    }

    void Run() {
        for (auto& test : tests_) {
            std::cout << "  Case< " << test.first << " >" << std::endl;
            std::cout << "    ";
            test.second();
        }
    }

    std::vector<std::pair<std::string, std::function<void()>>> tests_;
};

struct TestDriverRegister {
    TestDriverRegister(std::string name, std::function<void()> func) {
        TestDriver::Instance().AddTest(name, func);
    }
};

#define CONCAT(a, b) a ## b

#define FUNC_TEST(test_name, test_func, test_desc) \
    static void test_name ## _ ## test_func (); \
    TestDriverRegister test_name ## _ ## test_func ## _register(#test_func, test_name ## _ ## test_func); \
    void test_name ## _ ## test_func ()
