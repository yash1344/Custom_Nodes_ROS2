cmake_minimum_required(VERSION 3.8)
project(custom_interface)

if(CMAKE_COMPILER_IS_GNUCXX OR CMAKE_CXX_COMPILER_ID MATCHES "Clang")
  add_compile_options(-Wall -Wextra -Wpedantic)
endif()

# find dependencies
find_package(ament_cmake REQUIRED)
# uncomment the following section in order to fill in
# further dependencies manually.
# find_package(<dependency> REQUIRED)

# ================================================================
# This pulls in the IDL (Interface Definition Language) code generation tools.
# rosidl_default_generators is basically a meta-package that bundles the common code generators (rosidl_generator_c, rosidl_generator_cpp, rosidl_typesupport_*).
# Without this, your .srv or .msg files won’t get turned into C++ or Python headers.
# REQUIRED means CMake will error out if it doesn’t find it.
find_package(rosidl_default_generators REQUIRED)


# This is the magic that takes your .srv file and generates source code.
# It uses the IDL compilers under the hood to spit out headers like add_two_ints__struct.hpp, add_two_ints__functions.c, etc.
# srv/AddTwoInts.srv is relative to your msg/ or srv/ folder inside the package.
# ${PROJECT_NAME} means the generated interfaces belong to your package.
rosidl_generate_interfaces(${PROJECT_NAME}
  srv/AddTwoInts.srv
)
# ================================================================

if(BUILD_TESTING)
  find_package(ament_lint_auto REQUIRED)
  # the following line skips the linter which checks for copyrights
  # comment the line when a copyright and license is added to all source files
  set(ament_cmake_copyright_FOUND TRUE)
  # the following line skips cpplint (only works in a git repo)
  # comment the line when this package is in a git repo and when
  # a copyright and license is added to all source files
  set(ament_cmake_cpplint_FOUND TRUE)
  ament_lint_auto_find_test_dependencies()
endif()

ament_package()
