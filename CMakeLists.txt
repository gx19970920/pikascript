cmake_minimum_required(VERSION 3.0.0)
project(pikascript VERSION 0.1.0)

include_directories(src/package/pikascript/pikascript-core)
include_directories(src/package/pikascript/pikascript-api)
include_directories(src/boot/demo01-led)

add_subdirectory(src/package/googletest)
add_subdirectory(src/package/pikascript)
add_subdirectory(src/test)
add_subdirectory(src/boot/demo01-led)
add_subdirectory(src/boot/demo02-add)
add_subdirectory(src/boot/demo03-usart)
add_subdirectory(src/boot/demo04-usarts)
add_subdirectory(src/boot/demo05-sysobject)
add_subdirectory(src/boot/demo06-pikamain)
add_subdirectory(src/boot/banchmark)

