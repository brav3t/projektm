cd ..
rmdir ./build /q /s
conan install . --build=missing 
cd build
cmake .. -G "Visual Studio 17 2022" -DCMAKE_TOOLCHAIN_FILE=generators\conan_toolchain.cmake
::cmake --build . --config Release
