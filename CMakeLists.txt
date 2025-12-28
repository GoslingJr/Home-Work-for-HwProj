cmake_minimum_required(VERSION 3.10)
project(MorePrograms)

set(CMAKE_C_STANDARD 11)
set(CMAKE_C_FLAGS "${CMAKE_C_FLAGS} -Wall -Wextra -pedantic")

add_executable(Zero src/Zero.c)
add_executable(S1inS2 src/S1inS2.c)
add_executable(Balance src/Balance.c)
