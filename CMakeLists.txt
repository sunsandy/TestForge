cmake_minimum_required(VERSION 3.20)

project(TestForgeCppTests)

set(CMAKE_CXX_STANDARD 23)

add_subdirectory(CppTests)

# copy compile_commands.json to root for clangd
add_custom_target(copy_compile_commands
  DEPENDS ${CMAKE_CURRENT_BINARY_DIR}/compile_commands.json)
add_custom_command(
  TARGET copy_compile_commands
  PRE_BUILD
  COMMAND ${CMAKE_COMMAND} -E copy_if_different
    ${CMAKE_CURRENT_BINARY_DIR}/compile_commands.json
    ${CMAKE_CURRENT_SOURCE_DIR}/compile_commands.json
  )