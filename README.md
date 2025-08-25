# 🗺️ Sri Lanka National Spatial Data Infrastructure (NSDI) Layers

This repository provides **scripts and data downloads** from the official [Sri Lanka NSDI Geoportal](https://gisapps.nsdi.gov.lk/server/rest/services/Srilanka/All_Layers/MapServer), which hosts a collection of national GIS datasets.

## 📖 What is this about?

The **National Spatial Data Infrastructure (NSDI)** in Sri Lanka is a central platform that provides access to government geospatial data.
This dataset collection includes administrative boundaries, land use, transportation networks, utilities, and more — all in GIS-ready formats.

These layers are useful for:

* Researchers and students studying geography, environment, and urban planning.
* Developers building applications with Sri Lankan geospatial data.
* Government agencies and NGOs working with spatial analysis.
* Anyone curious about mapping Sri Lanka!

## 📂 What’s in this repo?

* `download_layers.py` → A Python script to automatically download **all available layers** from the NSDI MapServer in their original formats.
* `Release file` → A compressed archive containing all layers.

## 🔽 Where does the data come from?

All data is sourced directly from:

👉 [Sri Lanka NSDI Geoportal MapServer](https://gisapps.nsdi.gov.lk/server/rest/services/Srilanka/All_Layers/MapServer)

Hosted by the Survey Department of Sri Lanka.

## 📌 Available Layers

The following layers are included in this repository:

| Layer Name |
|------------|
| Agro Metric Stations |
| Hydrometric Station |
| Rainguage Station |
| Home Stay Units |
| Rented Homes |
| Guest Houses |
| Boutique_Villas |
| Fishing Harbor |
| Fish Landing Center |
| Bungalows |
| Heritage Homes |
| Classified Hotels |
| Rented Apartments |
| ATM |
| Banks |
| Shopping Malls |
| Boutique Hotels |
| Hotels |
| Tourist Hotels |
| Hotels Proposed |
| Restaurants |
| Heritage Bungalow |
| Tourist Spots |
| SpotHeights |
| ASC Locations |
| Soil Erosion |
| Hospitals |
| Spill Point |
| Wells |
| Village Anicut |
| Village Tank |
| Sea Ports |
| Minor tank distribution |
| Sluice Point |
| River Mouth Locations |
| Main Service Centers |
| PostOffice |
| Place Name |
| Archeological Sites |
| Educational Institutions |
| Courts |
| Police Stations |
| Place of Worship |
| Building Points |
| Boat Locations |
| Shelters |
| Troop Locations |
| Equipment Placement Centers |
| DEM 1m Point Cloud |
| Helipads |
| Airports |
| Railway Infrastructure |
| Interchanges |
| Helicopter pads |
| Road Transportation Point |
| Hydro UDA 10K |
| Toponym UDA 10K |
| Utility Point UDA 10K |
| Terrain Point UDA 10K |
| Transport Point UDA 10K |
| Other Water Point |
| Water Storage |
| Water Fire Hydrant |
| Water Fittings |
| Water Valve |
| Electrical Substations |
| Water Meter |
| Sewer Manhole |
| Water Station |
| Telecom Structure |
| Sewer Intercepter Manhole |
| Contours |
| Dams |
| Stream |
| Coastal Lines |
| Railway Lines |
| Expressway Network |
| National Road Network |
| Runways |
| Ferry Routes |
| Road Center Line |
| Utility Lline UDA 10K |
| Grid Line UDA 10K |
| AD Boundary Line UDA 10K |
| Transport Line UDA 10K |
| Hydro Line UDA 10K |
| Terrain Line UDA 10K |
| Sewer Lateral Pipeline |
| Sewer Force Main |
| Sewer Gravity Main |
| Water Pipe Line |
| National Parks |
| PA Net 2018 |
| Province Boundary |
| Development Area |
| Divisional Secretariat |
| Economic Zones |
| Country Boundary |
| District Boundary |
| Forest Boundary |
| Grama Niladhari Division |
| Beaches |
| Sensitive Areas |
| Hydro Zones |
| Climate Zones |
| Elevation Regime |
| Disaster Exposure |
| Rainfall |
| Temperature |
| GN ASC Divisions |
| Irrigation Schemes |
| Agro Ecological Zones |
| Crops Suitability Final |
| Soil Groups |
| Landslide |
| Soil Conservation Area |
| Soil |
| Lake |
| Cascades |
| Rivers |
| Reservoirs |
| Lagoon |
| Water Area |
| Canal |
| Pond |
| Ground Water Prospect |
| Water Shed |
| Ground Water |
| Basin |
| Landuse LUPPD 10K |
| Coastal Boundary |
| Agriculture Land |
| LandPlots |
| Landuse |
| Parcel Fabrics |
| SLTDA Parcels |
| ArcheologicalSites Buffer Zone |
| Building Footprint |
| building polygon 10k |
| Beaches 10K |
| Grama Niladhari Division 10K |
| District Boundary 10K |
| Development Area 10K |
| Sensitive Areas 10K |
| Forest Boundary 10K |
| Province Boundary 10K |
| Divisional Secretariat 10K |
| Economic Zones 10K |
| Country Boundary 10K |
| Buildings 3D Colombo |
| Road Right of ways |
| Tile Polygon UDA 10K |
| Building UDA 10K |
| UDA Declared Areas |
| Buildings 3D Colombo |
| Clouds UDA 10K |
| Hydro Polygon UDA 10K |
| Landuse UDA 10K |
| Synoptic Stations |
| Small_irrigation_tanks_poly |
| IDSL_Anicuts |
| IDSL_Reservoirs |


## 🚀 How to use

### 🔹 Option 1: Run locally

1. Clone this repository:

   ```bash
   git clone https://github.com/your-username/srilanka-nsdi-layers.git
   cd srilanka-nsdi-layers
   ```

2. Install dependencies:

   ```bash
   pip install requests
   ```

3. Run the script to download all layers:

   ```bash
   python download_layers.py
   ```

4. A folder named `SriLanka_Layers` will be created with all downloaded files, and a `SriLanka_Layers.zip` archive will also be generated.

* Some formats (like `.pbf`) are binary and require special GIS software (e.g., QGIS, ArcGIS Pro) to read.
* The data is maintained by the Survey Department. Availability and formats may change if the service updates.
* Please check usage rights/licensing with the **Survey Department of Sri Lanka** before using for commercial purposes.

## 🌍 Example Applications

* Visualizing Sri Lanka’s administrative divisions in **QGIS**.
* Building web maps using **Leaflet** or **MapLibre**.
* Performing geospatial analysis with **Python (GeoPandas, Shapely)**.
