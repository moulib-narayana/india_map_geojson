import json

# Mapping of state names to their codes
state_code_mapping = {
    "Andhra Pradesh": "IN-AP",
    "Arunachal Pradesh": "IN-AR",
    "Assam": "IN-AS",
    "Bihar": "IN-BR",
    "Chhattisgarh": "IN-CT",
    "Goa": "IN-GA",
    "Gujarat": "IN-GJ",
    "Haryana": "IN-HR",
    "Himachal Pradesh": "IN-HP",
    "Jharkhand": "IN-JH",
    "Karnataka": "IN-KA",
    "Kerala": "IN-KL",
    "Madhya Pradesh": "IN-MP",
    "Maharashtra": "IN-MH",
    "Manipur": "IN-MN",
    "Meghalaya": "IN-ML",
    "Mizoram": "IN-MZ",
    "Nagaland": "IN-NL",
    "Odisha": "IN-OR",
    "Punjab": "IN-PB",
    "Rajasthan": "IN-RJ",
    "Sikkim": "IN-SK",
    "Tamil Nadu": "IN-TN",
    "Telangana": "IN-TG",
    "Tripura": "IN-TR",
    "Uttarakhand": "IN-UT",
    "Uttar Pradesh": "IN-UP",
    "West Bengal": "IN-WB",
    "Andaman": "IN-AN",
    "Chandigarh": "IN-CH",
    "Dadra and Nagar Haveli": "IN-DN",
    "Daman and Diu": "IN-DD",
    "Delhi": "IN-DL",
    "Lakshadweep": "IN-LD",
    "Puducherry": "IN-PY",
    "Jammu & Kashmir": "IN-JK"
}

# Path to the geojson file
geojson_file_path = 'map_india.geojson'

# Read the geojson file
with open(geojson_file_path, 'r', encoding='utf-8') as file:
    data = json.load(file)

# Rename the state codes
for feature in data['features']:
    state_name = feature['properties'].get('st_nm')
    print(state_name)
    print(state_name in state_code_mapping)
    if state_name in state_code_mapping:
        feature['properties']['st_code_nm'] = state_code_mapping[state_name]

# Write the updated geojson back to the file
with open(geojson_file_path, 'w', encoding='utf-8') as file:
    json.dump(data, file, ensure_ascii=False, indent=4)