file(GLOB_RECURSE TEST_SAMPLES CONFIGURE_DEPENDS "*_generated.cpp")

add_executable(CppTestsSamples ${TEST_SAMPLES} main.cpp)

target_include_directories(CppTestsSamples PRIVATE ${CMAKE_CURRENT_SOURCE_DIR}/..)
