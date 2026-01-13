
Updated on 8/29/2025

Note: https://github.com/thiwaK/open-gis-lk will contain cleaned layers in the future. https://github.com/thiwaK/open-gis-lk/issues/18#issuecomment-3231664404

# 🗺️ Sri Lanka National Spatial Data Infrastructure (NSDI) Layers

This repository provides **scripts and data downloads** from the official [Sri Lanka NSDI Geoportal](https://gisapps.nsdi.gov.lk/server/rest/services/Srilanka/All_Layers/MapServer), which hosts a collection of national GIS datasets.

## What is this about?

The **National Spatial Data Infrastructure (NSDI)** in Sri Lanka is a central platform that provides access to government geospatial data.
This dataset collection includes administrative boundaries, land use, transportation networks, utilities, and more — all in GIS-ready formats.

These layers are useful for:

* Researchers and students studying geography, environment, and urban planning.
* Developers building applications with Sri Lankan geospatial data.
* Government agencies and NGOs working with spatial analysis.
* Anyone curious about mapping Sri Lanka!

## What’s in this repo?

* `download_layers.py` → A Python script to automatically download **all available layers** from the NSDI MapServer in their original formats.
* `Release file` → A compressed archive containing all layers.
* `Layers` → Individual layers.

## Where does the data come from?

All data is sourced directly from:

[Sri Lanka NSDI Geoportal MapServer](https://gisapps.nsdi.gov.lk/server/rest/services/Srilanka/All_Layers/MapServer)

Hosted by the Survey Department of Sri Lanka.

## Example Applications

* Visualizing Sri Lanka’s administrative divisions in **QGIS**.
* Building web maps using **Leaflet** or **MapLibre**.
* Performing geospatial analysis with **Python (GeoPandas, Shapely)**.
