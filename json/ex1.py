import json

# Load the JSON file
file_path = "/mnt/data/sample-data (1).json"

with open(file_path, "r") as file:
    data = json.load(file)

# Extract relevant data
interfaces = data["imdata"]
output_lines = []

# Formatting the output
output_lines.append("Interface Status")
output_lines.append("=" * 80)
output_lines.append(
    "{:<50} {:<20} {:<7} {:<6}".format("DN", "Description", "Speed", "MTU")
)
output_lines.append("-" * 80)

# Process each interface entry
for entry in interfaces:
    attributes = entry["l1PhysIf"]["attributes"]
    dn = attributes["dn"]
    descr = attributes["descr"] if attributes["descr"] else ""
    speed = attributes["speed"]
    mtu = attributes["mtu"]
    
    output_lines.append(
        "{:<50} {:<20} {:<7} {:<6}".format(dn, descr, speed, mtu)
    )

# Print the output in formatted style
formatted_output = "\n".join(output_lines)
print(formatted_output)
