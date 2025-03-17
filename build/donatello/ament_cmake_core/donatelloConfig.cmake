# generated from ament/cmake/core/templates/nameConfig.cmake.in

# prevent multiple inclusion
if(_donatello_CONFIG_INCLUDED)
  # ensure to keep the found flag the same
  if(NOT DEFINED donatello_FOUND)
    # explicitly set it to FALSE, otherwise CMake will set it to TRUE
    set(donatello_FOUND FALSE)
  elseif(NOT donatello_FOUND)
    # use separate condition to avoid uninitialized variable warning
    set(donatello_FOUND FALSE)
  endif()
  return()
endif()
set(_donatello_CONFIG_INCLUDED TRUE)

# output package information
if(NOT donatello_FIND_QUIETLY)
  message(STATUS "Found donatello: 0.0.0 (${donatello_DIR})")
endif()

# warn when using a deprecated package
if(NOT "" STREQUAL "")
  set(_msg "Package 'donatello' is deprecated")
  # append custom deprecation text if available
  if(NOT "" STREQUAL "TRUE")
    set(_msg "${_msg} ()")
  endif()
  # optionally quiet the deprecation message
  if(NOT ${donatello_DEPRECATED_QUIET})
    message(DEPRECATION "${_msg}")
  endif()
endif()

# flag package as ament-based to distinguish it after being find_package()-ed
set(donatello_FOUND_AMENT_PACKAGE TRUE)

# include all config extra files
set(_extras "")
foreach(_extra ${_extras})
  include("${donatello_DIR}/${_extra}")
endforeach()
