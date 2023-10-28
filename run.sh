#!/bin/bash

# Define the required Python packages
required_packages=("vidmaker" "pygame" "matplotlib")

# Check if Python 3 is installed
if command -v python3 &>/dev/null; then
	echo "Python 3 is installed."
else
	echo "Python 3 is not installed. Please install Python 3 before running this script."
	exit 1
fi

# Function to check if a Python package is installed
check_package() {
	package_name=$1
	if python3 -c "import $package_name" &>/dev/null; then
		echo "The required package '$package_name' is installed."
	else
		echo "The required package '$package_name' is not installed. Please install it before running this script."
		exit 1
	fi
}

# Check for each required package
for package in "${required_packages[@]}"; do
	check_package "$package"
done

# If all required packages are installed, run the main.py script
python3 src/main.py
