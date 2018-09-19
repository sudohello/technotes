
## Steps to Run OpenSfM - PCD Generation

* https://github.com/mapillary/OpenSfM

An example dataset is available at data/berlin.

* Put some images in data/DATASET_NAME/images/
* Put config.yaml in data/DATASET_NAME/config.yaml
* Go to the root of the project and run:
```bash
cd $HOME/softwares/OpenSfM
DATASET_NAME="data/gaze"
bin/opensfm_run_all data/DATASET_NAME
bin/opensfm_run_all data/gaze/13/44/15
```
* Start an http server from the root with:
```bash
python -m SimpleHTTPServer
```
* Browse:
```bash
http://localhost:8000/viewer/reconstruction.html#file=/data/gaze/13/44/15/reconstruction.meshed.json
http://localhost:8000/viewer/reconstruction.html#file=/data/DATASET_NAME/reconstruction.meshed.json
```