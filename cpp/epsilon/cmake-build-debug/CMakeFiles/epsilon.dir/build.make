# CMAKE generated file: DO NOT EDIT!
# Generated by "Unix Makefiles" Generator, CMake Version 3.15

# Delete rule output on recipe failure.
.DELETE_ON_ERROR:


#=============================================================================
# Special targets provided by cmake.

# Disable implicit rules so canonical targets will work.
.SUFFIXES:


# Remove some rules from gmake that .SUFFIXES does not remove.
SUFFIXES =

.SUFFIXES: .hpux_make_needs_suffix_list


# Suppress display of executed commands.
$(VERBOSE).SILENT:


# A target that is always out of date.
cmake_force:

.PHONY : cmake_force

#=============================================================================
# Set environment variables for the build.

# The shell in which to execute make rules.
SHELL = /bin/sh

# The CMake executable.
CMAKE_COMMAND = /cygdrive/c/Users/user/.CLion2019.3/system/cygwin_cmake/bin/cmake.exe

# The command to remove a file.
RM = /cygdrive/c/Users/user/.CLion2019.3/system/cygwin_cmake/bin/cmake.exe -E remove -f

# Escaping for special characters.
EQUALS = =

# The top-level source directory on which CMake was run.
CMAKE_SOURCE_DIR = /cygdrive/c/Users/user/Desktop/cpp/epsilon

# The top-level build directory on which CMake was run.
CMAKE_BINARY_DIR = /cygdrive/c/Users/user/Desktop/cpp/epsilon/cmake-build-debug

# Include any dependencies generated for this target.
include CMakeFiles/epsilon.dir/depend.make

# Include the progress variables for this target.
include CMakeFiles/epsilon.dir/progress.make

# Include the compile flags for this target's objects.
include CMakeFiles/epsilon.dir/flags.make

CMakeFiles/epsilon.dir/main.cpp.o: CMakeFiles/epsilon.dir/flags.make
CMakeFiles/epsilon.dir/main.cpp.o: ../main.cpp
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/cygdrive/c/Users/user/Desktop/cpp/epsilon/cmake-build-debug/CMakeFiles --progress-num=$(CMAKE_PROGRESS_1) "Building CXX object CMakeFiles/epsilon.dir/main.cpp.o"
	/usr/bin/c++.exe  $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -o CMakeFiles/epsilon.dir/main.cpp.o -c /cygdrive/c/Users/user/Desktop/cpp/epsilon/main.cpp

CMakeFiles/epsilon.dir/main.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/epsilon.dir/main.cpp.i"
	/usr/bin/c++.exe $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E /cygdrive/c/Users/user/Desktop/cpp/epsilon/main.cpp > CMakeFiles/epsilon.dir/main.cpp.i

CMakeFiles/epsilon.dir/main.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/epsilon.dir/main.cpp.s"
	/usr/bin/c++.exe $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S /cygdrive/c/Users/user/Desktop/cpp/epsilon/main.cpp -o CMakeFiles/epsilon.dir/main.cpp.s

CMakeFiles/epsilon.dir/days.cpp.o: CMakeFiles/epsilon.dir/flags.make
CMakeFiles/epsilon.dir/days.cpp.o: ../days.cpp
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/cygdrive/c/Users/user/Desktop/cpp/epsilon/cmake-build-debug/CMakeFiles --progress-num=$(CMAKE_PROGRESS_2) "Building CXX object CMakeFiles/epsilon.dir/days.cpp.o"
	/usr/bin/c++.exe  $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -o CMakeFiles/epsilon.dir/days.cpp.o -c /cygdrive/c/Users/user/Desktop/cpp/epsilon/days.cpp

CMakeFiles/epsilon.dir/days.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/epsilon.dir/days.cpp.i"
	/usr/bin/c++.exe $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E /cygdrive/c/Users/user/Desktop/cpp/epsilon/days.cpp > CMakeFiles/epsilon.dir/days.cpp.i

CMakeFiles/epsilon.dir/days.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/epsilon.dir/days.cpp.s"
	/usr/bin/c++.exe $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S /cygdrive/c/Users/user/Desktop/cpp/epsilon/days.cpp -o CMakeFiles/epsilon.dir/days.cpp.s

# Object files for target epsilon
epsilon_OBJECTS = \
"CMakeFiles/epsilon.dir/main.cpp.o" \
"CMakeFiles/epsilon.dir/days.cpp.o"

# External object files for target epsilon
epsilon_EXTERNAL_OBJECTS =

epsilon.exe: CMakeFiles/epsilon.dir/main.cpp.o
epsilon.exe: CMakeFiles/epsilon.dir/days.cpp.o
epsilon.exe: CMakeFiles/epsilon.dir/build.make
epsilon.exe: CMakeFiles/epsilon.dir/link.txt
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --bold --progress-dir=/cygdrive/c/Users/user/Desktop/cpp/epsilon/cmake-build-debug/CMakeFiles --progress-num=$(CMAKE_PROGRESS_3) "Linking CXX executable epsilon.exe"
	$(CMAKE_COMMAND) -E cmake_link_script CMakeFiles/epsilon.dir/link.txt --verbose=$(VERBOSE)

# Rule to build all files generated by this target.
CMakeFiles/epsilon.dir/build: epsilon.exe

.PHONY : CMakeFiles/epsilon.dir/build

CMakeFiles/epsilon.dir/clean:
	$(CMAKE_COMMAND) -P CMakeFiles/epsilon.dir/cmake_clean.cmake
.PHONY : CMakeFiles/epsilon.dir/clean

CMakeFiles/epsilon.dir/depend:
	cd /cygdrive/c/Users/user/Desktop/cpp/epsilon/cmake-build-debug && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /cygdrive/c/Users/user/Desktop/cpp/epsilon /cygdrive/c/Users/user/Desktop/cpp/epsilon /cygdrive/c/Users/user/Desktop/cpp/epsilon/cmake-build-debug /cygdrive/c/Users/user/Desktop/cpp/epsilon/cmake-build-debug /cygdrive/c/Users/user/Desktop/cpp/epsilon/cmake-build-debug/CMakeFiles/epsilon.dir/DependInfo.cmake --color=$(COLOR)
.PHONY : CMakeFiles/epsilon.dir/depend

