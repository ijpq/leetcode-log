# CMAKE generated file: DO NOT EDIT!
# Generated by "Unix Makefiles" Generator, CMake Version 3.17

# Delete rule output on recipe failure.
.DELETE_ON_ERROR:


#=============================================================================
# Special targets provided by cmake.

# Disable implicit rules so canonical targets will work.
.SUFFIXES:


# Disable VCS-based implicit rules.
% : %,v


# Disable VCS-based implicit rules.
% : RCS/%


# Disable VCS-based implicit rules.
% : RCS/%,v


# Disable VCS-based implicit rules.
% : SCCS/s.%


# Disable VCS-based implicit rules.
% : s.%


.SUFFIXES: .hpux_make_needs_suffix_list


# Command-line flag to silence nested $(MAKE).
$(VERBOSE)MAKESILENT = -s

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
CMAKE_COMMAND = /Applications/CLion.app/Contents/bin/cmake/mac/bin/cmake

# The command to remove a file.
RM = /Applications/CLion.app/Contents/bin/cmake/mac/bin/cmake -E rm -f

# Escaping for special characters.
EQUALS = =

# The top-level source directory on which CMake was run.
CMAKE_SOURCE_DIR = /Users/ketang/Desktop/leetcode-log

# The top-level build directory on which CMake was run.
CMAKE_BINARY_DIR = /Users/ketang/Desktop/leetcode-log/cmake-build-debug

# Include any dependencies generated for this target.
include c13_HasPtr/CMakeFiles/HasPtr.dir/depend.make

# Include the progress variables for this target.
include c13_HasPtr/CMakeFiles/HasPtr.dir/progress.make

# Include the compile flags for this target's objects.
include c13_HasPtr/CMakeFiles/HasPtr.dir/flags.make

c13_HasPtr/CMakeFiles/HasPtr.dir/HasPtr.cpp.o: c13_HasPtr/CMakeFiles/HasPtr.dir/flags.make
c13_HasPtr/CMakeFiles/HasPtr.dir/HasPtr.cpp.o: ../c13_HasPtr/HasPtr.cpp
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/Users/ketang/Desktop/leetcode-log/cmake-build-debug/CMakeFiles --progress-num=$(CMAKE_PROGRESS_1) "Building CXX object c13_HasPtr/CMakeFiles/HasPtr.dir/HasPtr.cpp.o"
	cd /Users/ketang/Desktop/leetcode-log/cmake-build-debug/c13_HasPtr && /Applications/Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/bin/c++  $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -o CMakeFiles/HasPtr.dir/HasPtr.cpp.o -c /Users/ketang/Desktop/leetcode-log/c13_HasPtr/HasPtr.cpp

c13_HasPtr/CMakeFiles/HasPtr.dir/HasPtr.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/HasPtr.dir/HasPtr.cpp.i"
	cd /Users/ketang/Desktop/leetcode-log/cmake-build-debug/c13_HasPtr && /Applications/Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E /Users/ketang/Desktop/leetcode-log/c13_HasPtr/HasPtr.cpp > CMakeFiles/HasPtr.dir/HasPtr.cpp.i

c13_HasPtr/CMakeFiles/HasPtr.dir/HasPtr.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/HasPtr.dir/HasPtr.cpp.s"
	cd /Users/ketang/Desktop/leetcode-log/cmake-build-debug/c13_HasPtr && /Applications/Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S /Users/ketang/Desktop/leetcode-log/c13_HasPtr/HasPtr.cpp -o CMakeFiles/HasPtr.dir/HasPtr.cpp.s

# Object files for target HasPtr
HasPtr_OBJECTS = \
"CMakeFiles/HasPtr.dir/HasPtr.cpp.o"

# External object files for target HasPtr
HasPtr_EXTERNAL_OBJECTS =

c13_HasPtr/HasPtr: c13_HasPtr/CMakeFiles/HasPtr.dir/HasPtr.cpp.o
c13_HasPtr/HasPtr: c13_HasPtr/CMakeFiles/HasPtr.dir/build.make
c13_HasPtr/HasPtr: c13_HasPtr/CMakeFiles/HasPtr.dir/link.txt
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --bold --progress-dir=/Users/ketang/Desktop/leetcode-log/cmake-build-debug/CMakeFiles --progress-num=$(CMAKE_PROGRESS_2) "Linking CXX executable HasPtr"
	cd /Users/ketang/Desktop/leetcode-log/cmake-build-debug/c13_HasPtr && $(CMAKE_COMMAND) -E cmake_link_script CMakeFiles/HasPtr.dir/link.txt --verbose=$(VERBOSE)

# Rule to build all files generated by this target.
c13_HasPtr/CMakeFiles/HasPtr.dir/build: c13_HasPtr/HasPtr

.PHONY : c13_HasPtr/CMakeFiles/HasPtr.dir/build

c13_HasPtr/CMakeFiles/HasPtr.dir/clean:
	cd /Users/ketang/Desktop/leetcode-log/cmake-build-debug/c13_HasPtr && $(CMAKE_COMMAND) -P CMakeFiles/HasPtr.dir/cmake_clean.cmake
.PHONY : c13_HasPtr/CMakeFiles/HasPtr.dir/clean

c13_HasPtr/CMakeFiles/HasPtr.dir/depend:
	cd /Users/ketang/Desktop/leetcode-log/cmake-build-debug && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /Users/ketang/Desktop/leetcode-log /Users/ketang/Desktop/leetcode-log/c13_HasPtr /Users/ketang/Desktop/leetcode-log/cmake-build-debug /Users/ketang/Desktop/leetcode-log/cmake-build-debug/c13_HasPtr /Users/ketang/Desktop/leetcode-log/cmake-build-debug/c13_HasPtr/CMakeFiles/HasPtr.dir/DependInfo.cmake --color=$(COLOR)
.PHONY : c13_HasPtr/CMakeFiles/HasPtr.dir/depend
