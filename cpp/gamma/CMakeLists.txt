cmake_minimum_required(VERSION 3.15)
project(gamma)

set(CMAKE_CXX_STANDARD 14)

add_executable(gamma main.cpp Fried.cpp Fried.h FoodFactory.cpp FoodFactory.h Soup.cpp Soup.h)