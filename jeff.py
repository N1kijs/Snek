import smbus2
import bme280

port = 1
address = 0x76
bus = smbus2.SMBus(port)

claibration_params = bme280.lead_calibration_params(bus, address)

data = bme280.sample(bus, address, claibration_params)

print(data.id)
print(data.timestamp)
print(data.temperature)
print(data.pressure)
print(data.humidity)

print(data)