![Build Status](https://github.com/hrichharms/theia/actions/workflows/integrate.yml/badge.svg)


## Proximity Warning System

The purpose of the code in this repository is to build out the foundation for a system that can be used for a camera-based proximity warning and ride camera system.

## Contents

Project components described bellow each have separate directories in src directory.

### Detector (Python 3)
- able to be run as independent program or imported as python module
- when run as an independent program, the detector monitors either provided video frames or captured camera frames for vehicles and prints warning decisions for each evaluated frame to standard output
- when imported as python module, provides access to:
    - `Detector` class: provides high-level access to a given haar classifier
    - `Monitor` class: provides a threaded implementation of the standalone for integration in larger programs using a given detector object

### Detector (C++)
- independent program which monitors either provided video frames or captured camera frames for vehicles and prints warning decisions for each evaluated frame to standard output

### Upload Client
- client to automatically upload video footage captured by detector component

### Upload Server
- server to receive video data from upload client component
