# CMake 最低版本号要求
cmake_minimum_required (VERSION 2.8)

# 项目信息
project (hasptr)

# 查找当前目录下的所有源文件
# 并将名称保存到 DIR_SRCS 变量
aux_source_directory(/Users/ketang/Desktop/leetcode-log/c13_HasPtr DIR_SRCS)
INCLUDE_DIRECTORIES(HasPtr.h)
# 指定生成目标
add_executable(HasPtr ${DIR_SRCS})

set (CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -std=c++11 -fsanitize=address")