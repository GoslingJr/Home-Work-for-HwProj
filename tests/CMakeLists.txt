enable_testing()

add_executable(test_hello test_hello.c)
add_test(NAME test_hello COMMAND test_hello)
