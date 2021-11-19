![Build Status](https://github.com/hrichharms/theia/actions/workflows/integrate.yml/badge.svg)


## Proximity Warning System

The purpose of this repository is to provide the proof of concept for a camera based proximity warning and ride camera system.

The classifier system included in this project isn't particularly accurate. For a production environment, a more sophisticated solution is advised.

Included Haar Cascade Classifier taken from [here](https://github.com/AdityaPai2398/Vehicle-And-Pedestrian-Detection-Using-Haar-Cascades).

## Components

The source code for each component listed below can be found in separate folders in src.

### Detector (Python 3)
- able to be run as independent program or imported as python module
- when run as an independent program, the detector monitors either provided video frames or captured camera frames (raspberry pi camera module) for vehicles and prints warning decisions for each evaluated frame to standard output
- when imported as python module, provides access to:
    - `Detector` class: provides high-level access to a given haar classifier specialized for simple proximity detection.

### Detector (C++)
- independent executable, which monitors either provided video frames or captured camera frames (raspberry pi camera module) for vehicles and prints warning decisions for each evaluated frame to standard output

### Upload Client
- client to automatically upload video footage captured by detector component
- [steganographic watermarking system](https://github.com/hrichharms/video_frame_stego) can be included here to track videos over social media using web-crawling

### Upload Server
- server to receive video data from upload client component
