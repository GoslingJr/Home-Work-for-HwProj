enable_testing()

add_executable(test_brackets test_brackets.c)
add_test(NAME test_brackets COMMAND test_brackets)

add_executable(test_calculator test_calculator.c)
add_test(NAME test_calculator COMMAND test_calculator)
