import json

alkaline = 2
analog_thermometer = 2
bloodset = 1
bolts = 18
bulbs = 14
capacitors = 12
car_battery = 4
circuit_board = 8
coffee = 3
cpu_fan = 50
duct_tape = 6
edrill = 6
flash_drive = 3
gas_analyzer = 3
gold_chain = 6
gun_lube = 1
hand_drill = 1
hard_drive = 4
helix = 8
hose = 26
intelligence = 4
lcd = 2
ledx = 1
lion = 2
military_cable = 4
motor = 9
multitool = 1
nails = 4
nixxor = 8
phase_relay = 16
pliers = 4
power_cord = 13
pressure_gauge = 6
psu = 15
roler = 3
saline = 8
signal_transmitter = 2
screw_nut = 12
screws = 20
skull_ring = 2
shus = 5
silicone_tubing = 14
sodium = 3
spark_plug = 5
tool_set = 6
ssd = 1
vpx = 2
wd40 = 4
wires = 47
wrench = 4
xenomorph = 3

dollars = 13000
euros = 165000
roubles = 13467000

with open('levels.json') as json_file:
    state = json.load(json_file)

if state["air_filtering_unit"] >= 1:
    dollars -= 10000


if state["bitcoin_farm"] >= 1:
    cpu_fan -= 10
    psu -= 5
    power_cord -= 5
    edrill -= 1

if state["bitcoin_farm"] >= 2:
    cpu_fan -= 15
    psu -= 5
    circuit_board -= 5
    phase_relay -= 2

if state["bitcoin_farm"] >= 3:
    cpu_fan -= 25
    silicone_tubing -= 10
    motor -= 1
    pressure_gauge -= 2


if state["booze_generator"] >= 1:
    silicone_tubing -= 4
    analog_thermometer -= 2
    pressure_gauge -= 2
    hose -= 5


if state["generator"] >= 1:
    roubles -= 100000

if state["generator"] >= 2:
    phase_relay -= 5
    motor -= 1
    wires -= 15

if state["generator"] >= 3:
    phase_relay -= 6
    motor -= 2
    spark_plug -= 5
    psu -= 5


if state["heating"] >= 1:
    roubles -= 25000

if state["heating"] >= 2:
    roubles -= 50000

if state["heating"] >= 3:
    helix -= 8
    wires -= 8


if state["illumination"] >= 1:
    roubles -= 10000

if state["illumination"] >= 2:
    bulbs -= 14
    wires -= 5

if state["illumination"] >= 3:
    roubles -= 50000
    capacitors -= 7


if state["intelligence_center"] >= 1:
    intelligence -= 1

if state["intelligence_center"] >= 2:
    intelligence -= 3
    flash_drive -= 3
    power_cord -= 4
    hard_drive -= 4

if state["intelligence_center"] >= 3:
    signal_transmitter -= 2
    vpx -= 2
    gas_analyzer -= 3
    military_cable -= 4


if state["lavatory"] >= 1:
    roubles -= 2000

if state["lavatory"] >= 2:
    hose -= 3
    screws -= 5
    edrill -= 1

if state["lavatory"] >= 3:
    hose -= 6
    pressure_gauge -= 2
    tool_set -= 1
    xenomorph -= 3


if state["library"] >= 1:
    roubles -= 400000


if state["medstation"] >= 1:
    roubles -= 25000

if state["medstation"] >= 2:
    roubles -= 50000
    bloodset -= 1
    saline -= 3

if state["medstation"] >= 3:
    roubles -= 150000
    saline -= 5
    ledx -= 1


if state["nutrition_unit"] >= 1:
    roubles -= 25000
    phase_relay -= 2

if state["nutrition_unit"] >= 2:
    wrench -= 4
    hose -= 2
    alkaline -= 2
    phase_relay -= 1

if state["nutrition_unit"] >= 3:
    coffee -= 3
    sodium -= 3
    roubles -= 125000


if state["rest_space"] >= 1:
    roubles -= 10000

if state["rest_space"] >= 2:
    roubles -= 35000

if state["rest_space"] >= 3:
    power_cord -= 4
    capacitors -= 5
    wires -= 7
    dollars -= 3000


if state["scav_case"] >= 1:
    lion -= 2
    skull_ring -= 2
    gold_chain -= 6
    roler -= 3

if state["security"] >= 1:
    roubles -= 20000

if state["security"] >= 2:
    roubles -= 45000

if state["security"] >= 3:
    lcd -= 2
    wires -= 4
    nixxor -= 8
    ssd -= 1


if state["shooting_range"] >= 1:
    nails -= 4
    screw_nut -= 5
    bolts -= 5
    duct_tape -= 3


if state["solar_power"] >= 1:
    euros -= 15000


if state["stash"] >= 2:
    roubles -= 3500000
    hand_drill -= 1
    screws -= 7
    wd40 -= 4

if state["stash"] >= 3:
    roubles -= 8500000
    edrill -= 2
    screws -= 8

if state["stash"] >= 4:
    euros -= 150000


if state["vents"] >= 1:
    roubles -= 25000

if state["vents"] >= 2:
    motor -= 1
    car_battery -= 1

if state["vents"] >= 3:
    motor -= 2
    car_battery -= 3
    wires -= 8
    circuit_board -= 3


if state["water_collector"] >= 1:
    hose -= 4
    bolts -= 5
    screw_nut -= 5
    duct_tape -= 3

if state["water_collector"] >= 2:
    hose -= 6
    motor -= 2
    tool_set -= 2

if state["water_collector"] >= 3:
    roubles -= 125000
    pliers -= 2
    shus -= 5


if state["workbench"] >= 1:
    screw_nut -= 2
    bolts -= 2
    multitool -= 1

if state["workbench"] >= 2:
    tool_set -= 3
    edrill -= 2
    bolts -= 6

if state["workbench"] >= 3:
    roubles -= 195000
    pliers -= 2
    gun_lube -= 1

loots = {
    'alkaline': alkaline,
    'Analog Thermometer': analog_thermometer,
    'Bloodset': bloodset,
    'Bolts': bolts,
    'Bulbs': bulbs,
    'Capacitors': capacitors,
    'Car Battery': car_battery,
    'Circuit Board': circuit_board,
    'Coffee': coffee,
    'CPU Fan': cpu_fan,
    'Duct Tape': duct_tape,
    'Electric Drill': edrill,
    'Secure Flash Drive': flash_drive,
    'Gas Analyzer': gas_analyzer,
    'Gold Chain': gold_chain,
    'Gun Lube': gun_lube,
    'Hand Drill': hand_drill,
    'Hard Drive': hard_drive,
    'Helix': helix,
    'Corrugated Hose': hose,
    'Intelligence Folder': intelligence,
    'LCD': lcd,
    'LEDx': ledx,
    'Bronze Lion': lion,
    'Military Cable': military_cable,
    'Electric Motor': motor,
    'Multitool': multitool,
    'Box of Nails': nails,
    'Nixxor': nixxor,
    'Phase Control Relay': phase_relay,
    'Elite Pliers': pliers,
    'Power Cord': power_cord,
    'Pressure Gauge': pressure_gauge,
    'PSU': psu,
    'Roler': roler,
    'NaCi': saline,
    'Signal Transmitter': signal_transmitter,
    'Screw Nut': screw_nut,
    'Screws': screws,
    'Skull Ring': skull_ring,
    'Shustrillo Sealing Foam': shus,
    'Silicone Tubing': silicone_tubing,
    'Sodium': sodium,
    'Spark Plug': spark_plug,
    'Tool Set': tool_set,
    'SSD': ssd,
    'VPX': vpx,
    'WD-40': wd40,
    'Wires': wires,
    'Wrench': wrench,
    'Xenomorph': xenomorph,
    'Dollars': dollars,
    'Euros': euros,
    'Roubles': roubles
    }

print("You need the following items:")
for key, value in loots.items():
    if value == 0:
        continue
    else:
        print(key, '->', value)