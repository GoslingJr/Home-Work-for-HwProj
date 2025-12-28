cmake_minimum_required(VERSION 3.10)
project(Homework5 LANGUAGES C)

set(CMAKE_C_FLAGS "${CMAKE_C_FLAGS} -Wall -Wextra -pedantic")

set(CMAKE_C_STANDARD 11)
set(CMAKE_C_STANDARD_REQUIRED ON)

add_executable(brackets_balance src/brackets.c)
add_executable(calculator src/calculator.c)
