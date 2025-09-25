#!/bin/bash

# CMSSW Environment Setup Script
# This script sets up the CMSSW_11_2_0 environment

echo "Setting up CMSSW_11_2_0 environment..."

# Source the CMSSW environment scripts
source /cvmfs/cms.cern.ch/cmsset_default.sh

# Save current directory
CURRENT_DIR=$(pwd)

# CMSSW path
CMSSW_PATH="/cvmfs/cms.cern.ch/slc7_amd64_gcc700/cms/cmssw/CMSSW_11_2_0"

# Check if CMSSW exists
if [ ! -d "$CMSSW_PATH" ]; then
    echo "Error: CMSSW_11_2_0 not found at $CMSSW_PATH"
    echo "Please check if CVMFS is properly mounted and accessible."
    return 1
fi

# Go to CMSSW area and run cmsenv
cd "$CMSSW_PATH"
eval `scramv1 runtime -sh`

# Return to original directory
cd "$CURRENT_DIR"

# Add current directory to PATH for convenience
export PATH="$(pwd):$PATH"

echo "CMSSW environment successfully set up!"
echo "CMSSW_BASE: $CMSSW_BASE"
echo "CMSSW_VERSION: $CMSSW_VERSION"
echo "SCRAM_ARCH: $SCRAM_ARCH"

echo "Setup complete. You can now use this directory for your analysis."
