# Specify build type for flashing

This script is designed to be flexible, allowing users to specify different build types while ensuring that the necessary firmware file exists before attempting to flash it.

## improvement point
The hard-coded path to commander-cli might need adjustment based on where the tool is installed on different systems. Using an environment variable or passing the path as a parameter would make the script even more adaptable.

```sh
#!/bin/bash

# Default build type
DEFAULT_BUILD_TYPE="DEVELOPMENT-DEBUG"

# Valid build types
VALID_BUILD_TYPES=("DEVELOPMENT-DEBUG" "DEVELOPMENT-RELEASE" "PRODUCTION-RELEASE" "PRODUCTION-DEBUG")

# Assign the input parameter to a variable, use the default if none is provided
BUILD_TYPE=${1:-$DEFAULT_BUILD_TYPE}

# Function to check if the build type is valid
function is_valid_build_type {
  local type=$1
  for valid_type in "${VALID_BUILD_TYPES[@]}"; do
    if [[ "$valid_type" == "$type" ]]; then
      return 0
    fi
  done
  return 1
}

# Validate the build type
if ! is_valid_build_type "$BUILD_TYPE"; then
  echo "Error: Invalid build type '$BUILD_TYPE'"
  echo "Valid build types are: ${VALID_BUILD_TYPES[*]}"
  exit 1
fi

# Get the directory of the script
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

# Base path to the build files
BASE_PATH="${SCRIPT_DIR}/../application/build"

# Construct the full path based on the build type
FULL_PATH="${BASE_PATH}/${BUILD_TYPE}/firmware.hex"

# Check if the .hex file exists
if [ ! -f "$FULL_PATH" ]; then
  echo "Error: Firmware file not found at '$FULL_PATH'"
  exit 1
fi

cd ~/SimplicityCommander-Linux/commander-cli
# here use your path of the hex file
./commander-cli flash  "$FULL_PATH"
```

## step by step

1. Shebang Line: This line indicates that the script should be executed using the Bash shell. It ensures the script runs in a compatible environment with Bash-specific features.
```sh 
#!/bin/bash
```

2. Default Build Type: This variable sets a default build type (DEVELOPMENT-DEBUG) that will be used if the user does not provide a build type as an input parameter.

```sh
# Default build type
DEFAULT_BUILD_TYPE="DEVELOPMENT-DEBUG"
```

3.Valid Build Types: This array defines the acceptable build types. The script uses this list to validate user input and ensure that only recognized build types are processed.
```sh
# Valid build types
VALID_BUILD_TYPES=("DEVELOPMENT-DEBUG" "DEVELOPMENT-RELEASE" "PRODUCTION-RELEASE" "PRODUCTION-DEBUG")
```

4. Assign Input Parameter: This line assigns the first input argument ($1) to the BUILD_TYPE variable. If no argument is provided, it defaults to DEFAULT_BUILD_TYPE. The syntax ${1:-$DEFAULT_BUILD_TYPE} means "use $1 if provided; otherwise, use $DEFAULT_BUILD_TYPE."
```sh
# Assign the input parameter to a variable, use the default if none is provided
BUILD_TYPE=${1:-$DEFAULT_BUILD_TYPE}
```
5. Validation Function: This function, is_valid_build_type, checks if the provided BUILD_TYPE is within the VALID_BUILD_TYPES array.
    - local type=$1: Declares a local variable type with the value of the first argument.
    - The for loop iterates over each item in the VALID_BUILD_TYPES array.
    - If the BUILD_TYPE matches any valid type, the function returns 0, indicating success.
    - If no match is found after looping, it returns 1, indicating failure.

    ```sh
    # Function to check if the build type is valid
    function is_valid_build_type {
    local type=$1
    for valid_type in "${VALID_BUILD_TYPES[@]}"; do
        if [[ "$valid_type" == "$type" ]]; then
        return 0
        fi
    done
    return 1
    }
    ```
6. Build Type Validation: This section uses the is_valid_build_type function to check if the BUILD_TYPE is valid.
If the function returns 1 (indicating the build type is invalid), the script prints an error message listing the valid build types and exits with exit 1, indicating an error.

```sh
# Validate the build type
if ! is_valid_build_type "$BUILD_TYPE"; then
  echo "Error: Invalid build type '$BUILD_TYPE'"
  echo "Valid build types are: ${VALID_BUILD_TYPES[*]}"
  exit 1
fi
```

7. Script Directory: This line sets SCRIPT_DIR to the directory where the script itself is located.
    - dirname "${BASH_SOURCE[0]}": Extracts the directory path of the script.
    - cd ... && pwd: Changes to that directory and prints the current path. This ensures that SCRIPT_DIR contains the absolute path to the script's location.

```sh
# Get the directory of the script
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
```

8. Base Path: This sets the base path for the build files relative to the script's directory. It assumes the build files are located in a sibling directory to the script's directory (going up one level with .. and then into application/build).
```sh
# Base path to the build files
BASE_PATH="${SCRIPT_DIR}/../application/build"
```
9. Construct Full Path: This constructs the full path to the .hex file by combining the BASE_PATH, the BUILD_TYPE, and the filename firmware.hex. This path points to the specific firmware file to be flashed.
```sh
# Construct the full path based on the build type
FULL_PATH="${BASE_PATH}/${BUILD_TYPE}/firmware.hex"
```

10. File Existence Check: This checks if the .hex file exists at the constructed FULL_PATH.
    - -f: Checks if the file exists and is a regular file.
    - If the file does not exist, it prints an error message and exits.
```sh
# Check if the .hex file exists
if [ ! -f "$FULL_PATH" ]; then
  echo "Error: Firmware file not found at '$FULL_PATH'"
  exit 1
fi
```

11. Change Directory and Flash Firmware:
    - cd ~/SimplicityCommander-Linux/commander-cli: Changes the directory to where the commander-cli tool is located.
    - ./commander-cli flash "$FULL_PATH": Executes the commander-cli command to flash the firmware using the specified .hex file.
```sh
cd ~/SimplicityCommander-Linux/commander-cli
# here use your path of the hex file
./commander-cli flash  "$FULL_PATH"
```