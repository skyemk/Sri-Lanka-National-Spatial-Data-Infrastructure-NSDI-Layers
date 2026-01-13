Updated on 8/29/2025

Note: open-gis-lk
 will contain cleaned layers in the future. See this comment
.

🗺️ Sri Lanka National Spatial Data Infrastructure (NSDI) Layers

This repository provides scripts and data downloads from the official Sri Lanka NSDI Geoportal
, which hosts a collection of national GIS datasets.

What is this about?

The National Spatial Data Infrastructure (NSDI) in Sri Lanka is a central platform that provides access to government geospatial data.
This dataset collection includes administrative boundaries, land use, transportation networks, utilities, and more — all in GIS-ready formats.

These layers are useful for:

Researchers and students studying geography, environment, and urban planning.

Developers building applications with Sri Lankan geospatial data.

Government agencies and NGOs working with spatial analysis.

Anyone curious about mapping Sri Lanka!

What’s in this repo?

download_layers.py → A Python script to automatically download all available layers from the NSDI MapServer in their original formats.

Release file → A compressed archive containing all layers.

Layers/ → Individual layers.

Where does the data come from?

All data is sourced directly from:

Sri Lanka NSDI Geoportal MapServer

Hosted by the Survey Department of Sri Lanka.

Inspect Available Layers
import requests

base_url = "https://gisapps.nsdi.gov.lk/server/rest/services/Srilanka/All_Layers/MapServer"

# Get service info
service_info = requests.get(f"{base_url}?f=json").json()
layers = service_info.get("layers", [])

print(f"Total layers: {len(layers)}\n")

for layer in layers:
    print(layer["name"])

Download Selected Layers
import requests
import os

# Base MapServer URL
base_url = "https://gisapps.nsdi.gov.lk/server/rest/services/Srilanka/All_Layers/MapServer"

# Layers you want (must match MapServer names)
TARGET_LAYERS = [
    "Grama Niladhari Division 10K",
    "UDA Declared Areas",
    "Province Boundary 10K",
    "District Boundary 10K",
    "Grama Niladhari Division",
    "Divisional Secretariat"
]

# Output folder
output_folder = "Selected_Layers"
os.makedirs(output_folder, exist_ok=True)

# Get service info
service_info = requests.get(f"{base_url}?f=json").json()

matched = 0

for layer in service_info.get("layers", []):
    layer_id = layer["id"]
    layer_name = layer["name"]

    if layer_name not in TARGET_LAYERS:
        continue

    matched += 1
    safe_name = layer_name.replace(" ", "_").replace("/", "_")
    print(f"📥 Found: {layer_name}")

    # Get layer info
    layer_info = requests.get(f"{base_url}/{layer_id}?f=json").json()
    formats = layer_info.get("supportedQueryFormats", "").lower()

    # Prefer GeoJSON → JSON → fallback
    if "geojson" in formats:
        out_format = "geojson"
    elif "json" in formats:
        out_format = "json"
    else:
        print(f"⚠️ No usable format for {layer_name}, skipping")
        continue

    query_url = f"{base_url}/{layer_id}/query"
    params = {
        "where": "1=1",
        "outFields": "*",
        "f": out_format
    }

    response = requests.get(query_url, params=params)

    if response.status_code == 200 and response.text.strip():
        path = os.path.join(output_folder, f"{safe_name}.{out_format}")
        with open(path, "w", encoding="utf-8") as f:
            f.write(response.text)
        print(f"✅ Saved {safe_name}.{out_format}")
    else:
        print(f"❌ Failed to download {layer_name}")

print(f"\n✨ Downloaded {matched} matching layers into '{output_folder}'")

Example Applications

Visualizing Sri Lanka’s administrative divisions in QGIS.

Building web maps using Leaflet or MapLibre.

Performing geospatial analysis with Python (GeoPandas, Shapely).
