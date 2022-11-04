hostname = "sjc12-dt-gw1"

print(hostname)

print("hostname")

hostname = hostname.upper()

print(hostname)

hostname = hostname.lower()

print(hostname)

host_split = hostname.split("-")

print(host_split)

print(dir(host_split))

ip_addr = "10.10.20.5"

subnet_mask = "/32"

print(ip_addr + subnet_mask)

print(ip_addr)

ip_addr = ip_addr + subnet_mask

print(ip_addr)

print(len(ip_addr))

print("The ip address is {}".format(ip_addr))

print("The hostname is {} and the address is {}".format(hostname, ip_addr))

show_run_interface = 'interface Ethernet1/1\n  no switchport\n  description Python Demo\n  ip address 10.10.20.1/24'

print(show_run_interface)

command = "    show ip interface brief "

print(command.strip())
print(command.lstrip())
print(command.rstrip())

# numbers

number_of_sites = 32
new_sites = 4

number_of_sites = number_of_sites + new_sites
print(number_of_sites)

print(dir(number_of_sites))

