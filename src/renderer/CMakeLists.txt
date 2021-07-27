set(LIB_NAME RENDERER)

set(HEADER_DIR "${PROJECT_SOURCE_DIR}/include/renderer")

add_library(${LIB_NAME} renderer.cpp ${HEADER_DIR}/renderer.hpp)

target_include_directories(${LIB_NAME}
    PUBLIC
        ${PROJECT_SOURCE_DIR}/include/renderer
)

target_link_libraries(${LIB_NAME}
    PRIVATE
        ${CONAN_LIBS}
)
