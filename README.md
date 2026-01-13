# 🗺️ Sri Lanka National Spatial Data Infrastructure (NSDI) Layers

> **Last Updated:** August 29, 2025  
> **Note:** `open-gis-lk` will contain cleaned layers in the future. See [this comment](link-to-comment) for details.

This repository provides automation scripts and data downloads from the official **Sri Lanka NSDI Geoportal**, the central hub for national GIS datasets hosted by the Survey Department of Sri Lanka.

## 🚀 Overview
The National Spatial Data Infrastructure (NSDI) in Sri Lanka provides access to government-verified geospatial data. This collection includes critical layers such as administrative boundaries, land use, and transportation networks.

### Use Cases:
* **Research:** Geography, environmental science, and urban planning.
* **Development:** Building apps requiring localized Sri Lankan geospatial data.
* **Analysis:** Spatial analysis for government agencies and NGOs.

---

## 📁 Repository Structure
* `download_layers.py`: Python script to fetch all available layers in their original formats.
* **Release file**: Compressed archive containing the complete dataset.
* `Layers/`: Directory containing individual GIS layers.

---

## 🛠️ Usage

### 1. Inspect Available Layers
Use this script to list all layers currently hosted on the NSDI MapServer.

```python
import requests

base_url = "[https://gisapps.nsdi.gov.lk/server/rest/services/Srilanka/All_Layers/MapServer](https://gisapps.nsdi.gov.lk/server/rest/services/Srilanka/All_Layers/MapServer)"

# Get service info
service_info = requests.get(f"{base_url}?f=json").json()
layers = service_info.get("layers", [])

print(f"Total layers: {len(layers)}\n")

for layer in layers:
    print(layer["name"])
