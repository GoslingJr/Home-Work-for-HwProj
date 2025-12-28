cmake_minimum_required(VERSION 3.10)
project(LinkedListPrograms)

set(CMAKE_C_STANDARD 11)
set(CMAKE_C_FLAGS "${CMAKE_C_FLAGS} -Wall -Wextra -pedantic")

add_executable(Iuda src/Iuda.c)
add_executable(Spisok src/Spisok.c)
