
commands = ['interface GigabitEthernet1/1', 'switchport access vlan 50', 'no shut']

print(commands)
print(commands[0])
print(commands[1])
print(print(commands[2]))

print(len(commands))

print(dir(commands))

vlans = [300, 200, 500, 150]
print(vlans.sort())

show_run_interface = 'interface GigabitEthernet1/1\n  no switchport\n  description Python Demo\n  ip address 10.10.20.1/24'

print(show_run_interface)

lines = show_run_interface.splitlines()

print(lines)

ping_results_1 = ["51.200 ms", "29.006 ms"]
ping_results_2 = ["30.300 ms"]

total_ping_results = ping_results_1 + ping_results_2
print(total_ping_results)