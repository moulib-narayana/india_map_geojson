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
    "Maharastra": "IN-MH",
    "Manipur": "IN-MN",
    "Meghalaya": "IN-ML",
    "Mizoram": "IN-MZ",
    "Nagaland": "IN-NL",
    "Orissa": "IN-OR",
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
    "Pondicherry": "IN-PY",
    "Jammu & Kashmir": "IN-JK"
}

state_code_mapping_new = {
    "Andhra Pradesh": 1,
    "Arunachal Pradesh": 31,
    "Assam": 4,
    "Bihar": 5,
    "Chhattisgarh": 6,
    "Goa": 21,
    "Gujarat": 7,
    "Haryana": 8,
    "Himachal Pradesh": 9,
    "Jharkhand": 11,
    "Karnataka": 20,
    "Kerala": 22,
    "Madhya Pradesh": 12,
    "Maharastra": 13,
    "Manipur": 24,
    "Meghalaya": 25,
    "Mizoram": 26,
    "Nagaland": 27,
    "Orissa": 14,
    "Punjab": 15,
    "Rajasthan": 3,
    "Sikkim": 29,
    "Tamil Nadu": 16,
    "Telangana": 35,
    "Tripura": 30,
    "Uttarakhand": 18,
    "Uttar Pradesh": 17,
    "West Bengal": 19,
    "Andaman": 33,
    "Chandigarh": 32,
    "Dadra and Nagar Haveli": 36,
    "Daman and Diu": 37,
    "Delhi": 2,
    "Lakshadweep": 23,
    "Pondicherry": 28,
    "Jammu & Kashmir": 10,
    "Ladakh": 38,
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

    # Replace the state codes with new mapping
    for feature in data['features']:
        state_name = feature['properties'].get('st_nm')
        print(state_name)
        print(state_name in state_code_mapping_new)
        if state_name in state_code_mapping_new:
            feature['properties']['state_code'] = state_code_mapping_new[state_name]

    # Write the updated geojson back to the file
    with open(geojson_file_path, 'w', encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False, indent=4)
