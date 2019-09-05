cmake_minimum_required(VERSION 2.8.4 FATAL_ERROR)

project(matrix_matrix_single_file CXX)

	set(CMAKE_MODULE_PATH ${CMAKE_MODULE_PATH}
			${HPX_ROOT}/SHARE/cmake-${CMAKE_MAJOR_VERSION}.${CMAKE_MINOR_VERSION}/Modules)

	find_package(HPX)
include_directories(${HPX_INCLUDE_DIR})
link_directories(${HPX_LIBRARY_DIR})

	add_hpx_executable(matrix_matrix_single_file
			ESSENTIAL

			SOURCES main.cpp

			COMPONENT_DEPENDENCIES iostreams)
