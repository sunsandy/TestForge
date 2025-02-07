cmake_minimum_required(VERSION 3.20)

project(BlendFormatTest)

set(CMAKE_CXX_STANDARD 23)

add_executable(BlendFormatTest blend.cpp main.cpp)

target_include_directories(BlendFormatTest PRIVATE ${CMAKE_SOURCE_DIR}/TestFramework)
