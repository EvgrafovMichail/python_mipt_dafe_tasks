cmake_minimum_required(VERSION 3.20)

project(Fifteen-Game LANGUAGES CXX)

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)
set(CMAKE_CXX_EXTENSIONS OFF)

add_compile_options(-Wall -Wextra)

# РУЧНОЕ УКАЗАНИЕ ПУТЕЙ FLTK (вместо find_package)
set(FLTK_INCLUDE_DIR "C:/FLTK/include")
set(FLTK_LIBRARY_DIR "C:/FLTK/lib")

# Проверка что пути существуют
if(NOT EXISTS "${FLTK_INCLUDE_DIR}/FL/Fl.H")
    message(FATAL_ERROR "FLTK not found at ${FLTK_INCLUDE_DIR}")
else()
    message(STATUS "FLTK manually set: ${FLTK_INCLUDE_DIR}")
endif()

set(TARGET "Fifteen_game")

add_executable(
    ${TARGET}
    src/main.cpp
    src/Graph_lib/Graph.cpp
    src/Graph_lib/GUI.cpp
    src/Graph_lib/Window.cpp
    src/Graph_lib/ext/graph.cpp
    src/GameGUI/cell.cpp
    src/GameGUI/fifteen_board.cpp
)

target_include_directories(${TARGET} PRIVATE
    ${CMAKE_SOURCE_DIR}/src
    ${CMAKE_SOURCE_DIR}/src/GameGUI
    ${CMAKE_SOURCE_DIR}/src/Graph_lib
    ${FLTK_INCLUDE_DIR}  # Добавляем FLTK вручную
)

target_link_directories(${TARGET} PRIVATE ${FLTK_LIBRARY_DIR})

target_link_libraries(${TARGET} PRIVATE
    fltk
    fltk_images
    fltk_forms
    fltk_gl
    fltkjpeg
    fltkpng
    fltkz
)

# Системные библиотеки Windows
if(WIN32)
    target_link_libraries(${TARGET} PRIVATE 
        gdi32 comctl32 ws2_32 ole32 uuid)
endif()

add_custom_target(CopyResources ALL
    COMMAND ${CMAKE_COMMAND} -E copy_directory
    ${PROJECT_SOURCE_DIR}/resources
    ${CMAKE_BINARY_DIR}/resources
    COMMENT "Copying resources into runtime output directory"
)

add_dependencies(${TARGET} CopyResources)