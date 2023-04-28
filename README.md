## Introduction

Bing Maps is releasing open building footprints around the world. We have detected **1.03B** buildings from Bing Maps imagery between 2014 and 2023 including Maxar, Airbus, and IGN France imagery. The data is freely available for download and use under ODbL. This dataset complements our [other releases](#will-there-be-more-data-coming-for-other-geographies). 

## Updates
* 2023-04-28 - Improved near duplicate and overlapping data detection and removal. 
* 2023-03-13 - Added **41MM** new buildings in Japan derived from Maxar Imagery (FP rate 0.8%). Added **79M** building height estimates for North America structures. 
* 2022-11-16 - Added **40M** new and updated buildings across 46 geographies derived from Bing imagery including Maxar, IGN-France, and AirBus between 2015 and 2022. The largest updates are for Pakistan (16M), Turkey (13M), Afghanistan (3M), and Saudi Arabia (2.5M). Added [make-gis-friendly.py](scripts/make-gis-friendly.py) demonstrating how to convert files
into a GIS tool (e.g., QGIS, ArcGIS) friendly format. 
* 2022-10-12 - Added **147M** new buildings for North America based on Vexcel and Maxar imagery between 2017 and 2022. This data is a refresh of [US](https://github.com/microsoft/USBuildingFootprints). Updated data format from country-partitioned zip
 files to country-[l9 quad key](https://learn.microsoft.com/en-us/bingmaps/articles/bing-maps-tile-system#tile-coordinates-and-quadkeys) gzipped partitioned files. Each file extension is .csv.gz but the contents are geojsonl. False positive rate for this dataset is ~1% based on a 4k structure sample. Link table was moved
 to a [dataset-links.csv](https://minedbuildings.blob.core.windows.net/global-buildings/dataset-links.csv)
* 2022-07-08 - Added **78M** buildings in Western EU Countries from Maxar imagery between 2014 and 2021 bringing the total structure count to **856M**. Added link to download buildings coverage. 
* 2022-07-05 - The complete building footprints dataset is available on [Microsoft's Planetary Computer](https://planetarycomputer.microsoft.com/dataset/ms-buildings)


![sample footprints](images/footprints-sample.png)

### Regions included 

![building regions](images/country-overview.png)

You can download the layer above as GeoJSON [here](https://minedbuildings.blob.core.windows.net/global-buildings/buildings-coverage.geojson).

## License
This data is licensed by Microsoft under the [Open Data Commons Open Database License (ODbL)](https://opendatacommons.org/licenses/odbl/).


## FAQ
### What does the data include?
999M building footprint polygon geometries located around the world in line delimited GeoJSON format. Due to the way we process the data, file extensions are `.csv.gz` see [make-gis-friendly.py](scripts/make-gis-friendly.py) for an example of how to decompress and change file extension.

As of October 2022, we moved the location table to [dataset-links.csv](https://minedbuildings.blob.core.windows.net/global-buildings/dataset-links.csv) since it's over 19k records with country-quadkey partitioning.

### What is the GeoJSON format?
GeoJSON is a format for encoding a variety of geographic data structures. 
For intensive documentation and tutorials, refer to this [blog](http://geojson.org/).

### Why is the data being released?
Microsoft has a continued interest in supporting a thriving OpenStreetMap ecosystem.

### Should we import the data into OpenStreetMap?
Maybe. Never overwrite the hard work of other contributors or blindly import data into OSM without first checking the local quality. While our metrics show that this data meets or exceeds the quality of hand-drawn building footprints, the data does vary in quality from place to place, between rural and urban, mountains and plains, and so on. Inspect quality locally and discuss an import plan with the community. Always follow the [OSM import community guidelines](https://wiki.openstreetmap.org/wiki/Import/Guidelines).

### Will the data be used or made available in the larger OpenStreetMap ecosystem?
Yes. The [HOT Tasking Manager](https://tasks.hotosm.org) has integrated Facebook [RapiD](https://mapwith.ai/rapid#background=Bing&disable_features=boundaries&map=2.00/0.0/0.0) where the data has been made available. 

### How did we create the data?
The building extraction is done in two stages:
1.	Semantic Segmentation – Recognizing building pixels on an aerial image using deep neural networks (DNNs)
2.	Polygonization – Converting building pixel detections into polygons

#### Stage1: Semantic Segmentation
![segmenation diagram](images/segmentation.jpg)

#### Stage 2: Polygonization
![polygonization diagram](images/polygonization.jpg)

### How do we estimate building height?
We trained a neural network to estimate height above ground using imagery paired with height measurements, and then we take the 
average height within a building polygon. Structures without height estimates are populated with a -1. 

### Were there any modeling improvements used for this release? 
We did not apply any modeling improvements for this release. Instead, we focused on scaling our approach to increase coverage, and trained models regionally.  

### Evaluation set metrics
The evaluation metrics are computed on a set of building polygon labels for each region. Note, we only have verification results for 
Mexico buildings since we did not train a model for the country. 

Building match metrics on the evaluation set:

| Region          | Precision   | Recall   |
|:----------------:|:------------:|:---------:|
| Africa          | 94.4%       | 70.9%    |
| Caribbean      | 92.2%       | 76.8%    |
| Central Asia    | 97.17%      | 79.47%   |
| Europe          | 94.3%       | 85.9%    |
| Middle East     | 95.7%       | 85.4%    |
| South America   | 95.4%       | 78.0%    |
| South Asia      | 94.8%       | 76.7%    |




We track the following metrics to measure the quality of matched building polygons in the evaluation set:
1. Intersection over Union – This is a standard metric measuring the overlap quality against the labels
2. Dominant angle rotation error – This measures the polygon rotation deviation

| Region          | IoU    |   Rotation error [deg] |
|:----------------:|:-------:|:-----------------------:|
| Africa          | 64.5%  |                   5.67 |
| Caribbean      | 64.0%  |                   6.64 |
| Central Asia    | 68.2%  |                   6.91 |
| Europe          | 65.1%  |                  10.28 |
| Middle East     | 65.1%  |                   9.3  |
| South America   | 66.7%  |                   6.34 |
| South Asia      | 63.1%  |                   6.25 |



### False positive ratio in the corpus

False positives are estimated per country from randomly sampled building polygon predictions.

| Region | Buildings Sampled | False Positive Rate | Run Date |
| :--: | :--: | :--: | :--: |
| Africa | 5,000 | 1.1% | Early 2022 | 
| Caribbean | 3,000 | 1.8% | Early 2022 |
| Central Asia | 3,000 | 2.2% | Early 2022 |
| Europe | 5,000 | 1.4% | Early 2022 |
| Mexico | 2,000 | 0.1% | Early 2022 |
| Middle East | 7,000 | 1.8% | Early 2022 |
| South America | 5,000 | 1.7% | Early 2022 |
| South Asia | 7,000 | 1.4% | Early 2022 | 
| North America  | 4,000 | 1% | Oct 2022 |
| Europe Maxar | 5,000 | 1.4% | July 2022 |


### What is the vintage of this data?
Vintage of extracted building footprints depends on the vintage of the underlying imagery. The underlying imagery is from Bing Maps including Maxar and Airbus between 2014 and 2021.

### How good is the data?
Our metrics show that in the vast majority of cases the quality is at least as good as hand digitized buildings in OpenStreetMap. It is not perfect, particularly in dense urban areas but it provides good recall in rural areas.

### What is the coordinate reference system?
EPSG: 4326

### Will there be more data coming for other geographies?
Maybe. This is a work in progress. Also, check out our other building releases!
* [US](https://github.com/microsoft/USBuildingFootprints)
* [Australia](https://github.com/microsoft/AustraliaBuildingFootprints)
* [Canada](https://github.com/microsoft/CanadianBuildingFootprints)
* [Uganda and Tanzania](https://github.com/microsoft/Uganda-Tanzania-Building-Footprints)
* [South America](https://github.com/microsoft/SouthAmericaBuildingFootprints)
* [Kenya and Nigeria](https://github.com/microsoft/KenyaNigeriaBuildingFootprints)
* [Indonesia, Malaysia, and the Philippines](https://github.com/microsoft/IdMyPhBuildingFootprints)

### Why are some locations missing?
We excluded imagery from processing if tiles were dated before 2014 or there was a low-probability of detection. Detection probability is loosely defined here as proximity to roads and population centers. This filtering and tile exclusion results in squares of missing data. 

### How can I read large files?
Some files are very large but they are stored in line-delimited format so one could use parallel processing tools (e.g., [Spark](https://spark.apache.org/), [Dask](https://docs.dask.org/en/stable/dataframe.html)) or create a memory 
efficient script to segment into smaller pieces. See `scripts/read-large-files.py` for a Python example. 

## Need roads?
Check out our [ML Road Detections](https://github.com/microsoft/RoadDetections) project page!

<br>

## Contributing

This project welcomes contributions and suggestions.  Most contributions require you to agree to a
Contributor License Agreement (CLA) declaring that you have the right to, and actually do, grant us
the rights to use your contribution. For details, visit https://cla.microsoft.com.

When you submit a pull request, a CLA-bot will automatically determine whether you need to provide
a CLA and decorate the PR appropriately (e.g., label, comment). Simply follow the instructions
provided by the bot. You will only need to do this once across all repos using our CLA.

This project has adopted the [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/).
For more information see the [Code of Conduct FAQ](https://opensource.microsoft.com/codeofconduct/faq/) or
contact [opencode@microsoft.com](mailto:opencode@microsoft.com) with any additional questions or comments.

## Legal Notices

Microsoft, Windows, Microsoft Azure and/or other Microsoft products and services referenced in the documentation
may be either trademarks or registered trademarks of Microsoft in the United States and/or other countries.
The licenses for this project do not grant you rights to use any Microsoft names, logos, or trademarks.
Microsoft's general trademark guidelines can be found [here](http://go.microsoft.com/fwlink/?LinkID=254653).

Privacy information can be found [here](https://privacy.microsoft.com/en-us/).

Microsoft and any contributors reserve all others rights, whether under their respective copyrights, patents,
or trademarks, whether by implication, estoppel or otherwise.
