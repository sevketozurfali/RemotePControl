import pulsectl
import json


pulse = pulsectl.Pulse("t")

audio_device_list = pulse.sink_list()
print("Device List : {}",audio_device_list)

device_map = {}
device_list = []

# device_map[audio_device_list]
# print(audio_device_list[0])
# print(audio_device_list[0].volume)
# print(audio_device_list[0].proplist["index"])
# print("hello")
# print(audio_device_list[0].index)
# print(audio_device_list[0].description)

device_map['devices'] = []


for device in pulse.sink_list():

    device_map['devices'].append({
        'index': device.index,
        'name': device.description
    })

with open('data.txt', 'w') as outfile:
    json.dump(device_map, outfile)

    # print(devices.description)
    # print(devices.index ,",", devices.description)
    # print(devices.description)
    # device_list.append(devices.index)
    # device_list.append(devices.description)

# print(device_list)

