device_dict = {
    "name" : "sjc-dt-gw1",
    "ip_addr" : "10.20.30.40",
    "role" : "gateway"
}

print(device_dict)

print(device_dict["name"])
print(device_dict["ip_addr"])
print(device_dict["ip_address"])
print(device_dict.get("name"))
print(device_dict.get("ip_address"))

print(dir(device_dict))
print(device_dict.keys())
print(device_dict.values())

location = {
    "country" : "Mexico",
    "city" : "Cancun"
}

loc_update = {
    "region" : "LATAM"
}

#updates original dict, overwrites if same keys
print(location.update(loc_update))

print(location)

loc_update = {
    "city" : "Mexico City"
}

print(location.update(loc_update))

print(location)