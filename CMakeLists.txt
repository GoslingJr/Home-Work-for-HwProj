cmake_minimum_required(VERSION 3.10)
project(SortedList)

set(CMAKE_C_STANDARD 11)
set(CMAKE_C_FLAGS "${CMAKE_C_FLAGS} -Wall -Wextra -pedantic")

add_executable(Spisok src/Spisok.c)

add_executable(test_sorted_list tests/test_sorted_list.c src/Spisok.c)

enable_testing()
add_test(NAME SortedListTests COMMAND test_sorted_list --test)
