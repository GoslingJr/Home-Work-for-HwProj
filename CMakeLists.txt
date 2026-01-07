cmake_minimum_required(VERSION 3.10)
project(SortApp)

set(CMAKE_C_STANDARD 11)

add_executable(sort_app main.c sort.s)

if(UNIX)
    set(CMAKE_ASM_FLAGS "${CMAKE_ASM_FLAGS} -f elf64")
    if(APPLE)
        message(STATUS "Building for macOS")
        set(CMAKE_ASM_FLAGS "${CMAKE_ASM_FLAGS} -f macho64")
    else()
        message(STATUS "Building for Linux")
    endif()
endif()

if(WIN32)
    message(STATUS "Building for Windows")
    set(CMAKE_ASM_FLAGS "${CMAKE_ASM_FLAGS} -f win64")
    
    if(MSVC)
        enable_language(ASM_MASM)
        set_source_files_properties(sort.s PROPERTIES LANGUAGE ASM_MASM)
    endif()
endif()
