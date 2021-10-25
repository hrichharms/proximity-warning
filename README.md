## Components

Project components described bellow each have separate directories in src directory.

### Detector (Python 3)
- able to be run as independent program or imported as python module

### Detector (C++)
- independent program

### Upload Client
- client to automatically upload video footage captured by detector component

### Upload Server
- server to receive video data from upload client component

## Performance Goals
- performance to be measured on raspberry pi zero with the use of downloaded camera data
- performance with physical camera module to be estimated based upon average fps
- 25 fps
- 90% accuracy