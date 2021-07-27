from conan import ConanFile
from conan.tools.cmake import cmake_layout

class VoxelConan(ConanFile):
    settings = "os", "compiler", "build_type", "arch"
    generators = "CMakeToolchain", "CMakeDeps"
 
    def requirements(self):
        self.requires("glad/0.1.36")
        self.requires("glfw/3.3.8")
        self.requires("glm/cci.20230113")

    def layout(self):
        cmake_layout(self)
