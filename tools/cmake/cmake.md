# CMAKE

**Table of Contents**
[TOC]

# CMake Presets
The configurePresets and buildPresets in CMakePresets.json serve different purposes within the CMake workflow. Here's a clear breakdown of their roles and how they work together:

## Configure Presets
These define how CMake initializes the build system by configuring the project. This step prepares the environment but does not compile any code.
The Key responsibilities are:
* Set up the CMake cache and project environment.
* Choose the build generator (e.g., Ninja, Unix Makefiles, Visual Studio).
* Define paths (like binaryDir) and toolchains (for cross-compiling).
* Configure CMake variables (e.g., CMAKE_BUILD_TYPE=Debug).
```json
{
    "name": "Debug",
    "generator": "Ninja",
    "binaryDir": "${sourceDir}/build/debug",
    "cacheVariables": {
        "CMAKE_BUILD_TYPE": "Debug"
    }
}
```
## Build Presets
These control how CMake compiles the code after configuration. They rely on a valid configurePreset to know where the build files are located.

The Key Responsibilities:
* Invoke the CMake build command.
* Specify which targets to build (e.g., all, my_app).
* Set the number of parallel jobs to speed up compilation.
```json
{
    "name": "Debug-Build",
    "configurePreset": "Debug",
    "jobs": 8
}
```

## From experience
1. Hidden presets cannot be directly used in build presets