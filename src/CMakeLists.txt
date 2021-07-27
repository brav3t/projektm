set_property(DIRECTORY ${CMAKE_CURRENT_SOURCE_DIR} PROPERTY VS_STARTUP_PROJECT ${PROJECT_NAME})

add_executable(${PROJECT_NAME} main.cpp)

add_subdirectory(renderer)

target_link_libraries(${PROJECT_NAME} RENDERER)
