# Running & walking distance calculator for Garmin

## Overview

The script calculates the running and walking distances during a running activity recorded with a Garmin device (e.g. Forerunner 255s).

It was born out of the frustration with the Garmin Connect app — which shows only the time spent on runnning/walking/standing, without telling you how far you actually ran and walked. Mostly useful for mountain/trail running probably.

## Requirements
- python >= 3.12

## Usage

1. Export Garmin activity to zip and unpack it (from the desktop's web browser).
2. Upload .fit file e.g. to https://www.fitfileviewer.com/
3. Download `Record` csv using setting `Localized format`.
4. Use the csv to run the script:

With default threshold cadence:
```
python runwalk.py C:/Users/Downloads/20066666_ACTIVITY-record.csv
```

With your specified threshold cadence:
```
python runwalk.py -c 70 C:/Users/Downloads/20066666_ACTIVITY-record.csv
```

