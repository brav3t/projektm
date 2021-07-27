set(LIB_NAME RENDERER)
set(HEADER_DIR "${PROJECT_SOURCE_DIR}/include/renderer")

find_package(glad REQUIRED)
find_package(glfw3 REQUIRED)
find_package(glm REQUIRED)

add_library(${LIB_NAME} STATIC renderer.cpp ${HEADER_DIR}/renderer.h)

target_include_directories(${LIB_NAME} PUBLIC ${HEADER_DIR})

target_link_libraries(${LIB_NAME}
    glad::glad
    glfw
    glm::glm
)
