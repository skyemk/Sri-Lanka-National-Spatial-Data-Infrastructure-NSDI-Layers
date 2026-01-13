import requests
import os
import shutil

# Base URL of the MapServer
base_url = "https://gisapps.nsdi.gov.lk/server/rest/services/Srilanka/All_Layers/MapServer"

# Output folder
output_folder = "SriLanka_Layers"
os.makedirs(output_folder, exist_ok=True)

# Get service info
service_info = requests.get(f"{base_url}?f=json").json()

for layer in service_info.get('layers', []):
    layer_id = layer['id']
    layer_name = layer['name'].replace(" ", "_").replace("/", "_")  # safe filename

    # Query the layer info
    layer_info = requests.get(f"{base_url}/{layer_id}?f=json").json()
    supported_formats = layer_info.get('supportedQueryFormats', '')

    if not supported_formats:
        print(f"No downloadable formats for {layer_name}, skipping...")
        continue

    formats = [fmt.strip() for fmt in supported_formats.split(",")]

    for fmt in formats:
        fmt_lower = fmt.lower()
        file_ext = fmt_lower if fmt_lower != "geojson" else "geojson"

        # Construct query URL for full download
        query_url = f"{base_url}/{layer_id}/query"
        params = {
            "where": "1=1",      # all features
            "outFields": "*",    # all fields
            "f": fmt_lower
        }

        print(f"Downloading {layer_name} in {fmt} format...")

        response = requests.get(query_url, params=params)

        if response.status_code == 200 and response.text.strip():
            file_path = os.path.join(output_folder, f"{layer_name}.{file_ext}")
            with open(file_path, "w", encoding="utf-8") as f:
                f.write(response.text)
        else:
            print(f"⚠️ Failed to download {layer_name} in {fmt}")

# Zip the folder
zip_filename = "SriLanka_Layers.zip"
shutil.make_archive("SriLanka_Layers", 'zip', output_folder)

print(f"✅ All layers saved to {zip_filename}")
