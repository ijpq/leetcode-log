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
CMAKE_COMMAND = /home/ketang/.local/share/JetBrains/Toolbox/apps/CLion/ch-0/202.8194.17/bin/cmake/linux/bin/cmake

# The command to remove a file.
RM = /home/ketang/.local/share/JetBrains/Toolbox/apps/CLion/ch-0/202.8194.17/bin/cmake/linux/bin/cmake -E rm -f

# Escaping for special characters.
EQUALS = =

# The top-level source directory on which CMake was run.
CMAKE_SOURCE_DIR = /home/ketang/leetcode-log

# The top-level build directory on which CMake was run.
CMAKE_BINARY_DIR = /home/ketang/leetcode-log/cmake-build-debug

# Include any dependencies generated for this target.
include c13_String/CMakeFiles/string.dir/depend.make

# Include the progress variables for this target.
include c13_String/CMakeFiles/string.dir/progress.make

# Include the compile flags for this target's objects.
include c13_String/CMakeFiles/string.dir/flags.make

c13_String/CMakeFiles/string.dir/String.cpp.o: c13_String/CMakeFiles/string.dir/flags.make
c13_String/CMakeFiles/string.dir/String.cpp.o: ../c13_String/String.cpp
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/home/ketang/leetcode-log/cmake-build-debug/CMakeFiles --progress-num=$(CMAKE_PROGRESS_1) "Building CXX object c13_String/CMakeFiles/string.dir/String.cpp.o"
	cd /home/ketang/leetcode-log/cmake-build-debug/c13_String && /usr/bin/c++  $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -o CMakeFiles/string.dir/String.cpp.o -c /home/ketang/leetcode-log/c13_String/String.cpp

c13_String/CMakeFiles/string.dir/String.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/string.dir/String.cpp.i"
	cd /home/ketang/leetcode-log/cmake-build-debug/c13_String && /usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E /home/ketang/leetcode-log/c13_String/String.cpp > CMakeFiles/string.dir/String.cpp.i

c13_String/CMakeFiles/string.dir/String.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/string.dir/String.cpp.s"
	cd /home/ketang/leetcode-log/cmake-build-debug/c13_String && /usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S /home/ketang/leetcode-log/c13_String/String.cpp -o CMakeFiles/string.dir/String.cpp.s

# Object files for target string
string_OBJECTS = \
"CMakeFiles/string.dir/String.cpp.o"

# External object files for target string
string_EXTERNAL_OBJECTS =

c13_String/string: c13_String/CMakeFiles/string.dir/String.cpp.o
c13_String/string: c13_String/CMakeFiles/string.dir/build.make
c13_String/string: c13_String/CMakeFiles/string.dir/link.txt
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --bold --progress-dir=/home/ketang/leetcode-log/cmake-build-debug/CMakeFiles --progress-num=$(CMAKE_PROGRESS_2) "Linking CXX executable string"
	cd /home/ketang/leetcode-log/cmake-build-debug/c13_String && $(CMAKE_COMMAND) -E cmake_link_script CMakeFiles/string.dir/link.txt --verbose=$(VERBOSE)

# Rule to build all files generated by this target.
c13_String/CMakeFiles/string.dir/build: c13_String/string

.PHONY : c13_String/CMakeFiles/string.dir/build

c13_String/CMakeFiles/string.dir/clean:
	cd /home/ketang/leetcode-log/cmake-build-debug/c13_String && $(CMAKE_COMMAND) -P CMakeFiles/string.dir/cmake_clean.cmake
.PHONY : c13_String/CMakeFiles/string.dir/clean

c13_String/CMakeFiles/string.dir/depend:
	cd /home/ketang/leetcode-log/cmake-build-debug && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /home/ketang/leetcode-log /home/ketang/leetcode-log/c13_String /home/ketang/leetcode-log/cmake-build-debug /home/ketang/leetcode-log/cmake-build-debug/c13_String /home/ketang/leetcode-log/cmake-build-debug/c13_String/CMakeFiles/string.dir/DependInfo.cmake --color=$(COLOR)
.PHONY : c13_String/CMakeFiles/string.dir/depend

