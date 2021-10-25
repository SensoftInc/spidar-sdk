# coding=utf-8
import socket
import struct
import json
import requests
import numpy as np

"""
This sample script demonstrates how to collect data from a NIC500.

The script performs the following steps:

1. Get the OEM version information and confirm the NIC-500 is in OEM mode
2. Read system information from the NIC and print it to console.
3. Power on the GPR.
4. Read system information from the GPR and print it to console.
5. Connect to the data socket
6. Set up with GPR  settings for a 1000 MHz system.
    points per trace: 200
    time sampling interval: 100 ps 
    stacks: 4
    period: 1 s
    
    The window time shift is based on the reference value from gpr system information, 
    and the first break is set to appear at point 20. The following formula is used:
    
    window_time_shift_ps = window_time_shift_reference_ps - (20 * time_sampling_interval_ps).
    
    If the unit doesn't have a reference value (aka pulseEKKO PRO) then set window_time_shift to -55000 as default.

7. Start acquisition.
8. Print trace headers and the first 10 points of any trace that arrives.
9. Stop acquisition.
10. Close the data socket.

"""

# NIC500 IP address
IP_ADDRESS = '192.168.20.221'

# Commands to communication with OEM
API_URL = "http://" + IP_ADDRESS + ":8080/api"
NIC_SYSTEM_INFO_CMD = API_URL + "/nic/system_information"
GPR_SYSTEM_INFO_CMD = API_URL + "/nic/gpr/system_information"
DATA_SOCKET_CMD = API_URL + "/nic/gpr/data_socket"
VERSION_CMD = API_URL + "/nic/version"
POWER_CMD = API_URL + "/nic/power"
SETUP_CMD = API_URL + "/nic/setup"
ACQUISITION_CMD = API_URL + "/nic/acquisition"

# GPR settings
POINTS_PER_TRACE = 200
TIME_SAMPLING_INTERVAL_PS = 100
POINT_STACKS = 4
PERIOD_S = 1
FIRST_BREAK_POINT = 20

# Configuration for the following put commands
POWER_ON_CONFIGURATION = {"data": json.dumps({'state': 2})}
START_ACQUISITION_CONFIGURATION = {"data": json.dumps({'state': 1})}
STOP_ACQUISITION_CONFIGURATION = {"data": json.dumps({'state': 0})}

# Trace settings
HEADER_SIZE_BYTES = 20
POINT_SIZE_BYTES = 4


def get_requests(command, command_str_name):
    """
    Perform a get request to retrieve data from a resource.
    @param command: URL for the request command
    @type command: str
    @param command_str_name: Name of the command
    @type command_str_name: str
    @return: response in json format
    @rtype: JSON or None when request failed
    """
    json_response = None
    try:
        response = requests.get(command)
        json_response = json.loads(response.content)
        print("Response from {} command: {}\n".format(command_str_name, json_response["status"]["message"]))
    except ValueError as err:
        print("Unable to decode JSON: {}\n".format(err))
    except KeyError:
        print("Response from {} command: {}\n".format(command_str_name, json_response["success"]))
    return json_response


def put_requests(command, data, command_str_name):
    """
    Perform a put request to change the resource’s data.
    @param command: URL for the request command
    @type command: str
    @param data: Data to send to the command
    @type data: dict
    @param command_str_name: Name of the command
    @type command_str_name: str
    @return: response in json format
    @rtype: JSON or None when request failed
    """
    json_response = None
    try:
        response = requests.put(command, data=data)
        json_response = json.loads(response.content)
        print("Response from {} command: {}\n".format(command_str_name, json_response["status"]["message"]))
    except ValueError as err:
        print("Unable to decode JSON: {}\n".format(err))
    
    if json_response["status"]["status_code"] != 0:
        print("Command failed: {}".format(json_response["status"]["message"]))
        json_response = None

    return json_response


# Use the API command to confirm we are in OEM Mode
api_response = get_requests(API_URL, "API")
if api_response is None or not api_response['data']['name'] == "NIC-500 OEM":
    print("Not in NIC OEM Mode")
    quit()
print("In NIC OEM Mode!")

# Use the NIC system_information command to get the system information
nic_system_information_response = get_requests(NIC_SYSTEM_INFO_CMD, "NIC's System Information")
nic_system_info_response_data = nic_system_information_response['data']
# Print the NIC500 system information
print(("System Information:\nApp DIP: {}\nApp Version: {}\nFPGA Version: {}\nHardware ID: {}\nKernel Version: {}\n"
       "NIC Serial Number: {}\nOS DIP: {}\nOS Version: {}\nSmcApi: {} \n").format(
    nic_system_info_response_data['app_dip'], nic_system_info_response_data['app_version']
    , nic_system_info_response_data['app_dip'], nic_system_info_response_data['fpga_version']
    , nic_system_info_response_data['kernel_version'], nic_system_info_response_data['hardware_id']
    , nic_system_info_response_data['nic_serial_number'], nic_system_info_response_data['os_dip']
    , nic_system_info_response_data['os_version'], nic_system_info_response_data['smc_api_build']))

# Use the NIC Power command to turn on the GPR
power_on_response = put_requests(POWER_CMD, POWER_ON_CONFIGURATION, "Power")
# Confirm the GPR was able to turn on
if power_on_response is None:
    quit()

# Use the GPR System Information command to get system information
gpr_system_json_response = get_requests(GPR_SYSTEM_INFO_CMD, "GPR System Information")
# Confirm we've received a successful response
if gpr_system_json_response is None:
    quit()

# Print out GPR system info
gpr_system_info = gpr_system_json_response['data']['gpr']
print((
    "GPR System Information:\nApp Code DIP: {}\nApp Code Version: {}\nDEV0:\n\tApp Code DIP: {}\n\tType: {}\n\t"
    "Unit Serial Number: {}\nDEV1:\n\tApp Code DIP: {}\n\tType: {}\n\tUnit Serial Number: {}\nGIC Serial Number: {}\n"
    "Unit Serial Number: {}\nWindow Time Shift Reference (ps): {}\n").format(
    gpr_system_info['app_code_dip'], gpr_system_info['app_code_version']
    , gpr_system_info['dev0']['app_code_dip'], gpr_system_info['dev0']['type']
    , gpr_system_info['dev0']['unit_serial_number'], gpr_system_info['dev1']['app_code_dip']
    , gpr_system_info['dev1']['type'], gpr_system_info['dev1']['unit_serial_number']
    , gpr_system_info['gic_serial_number'], gpr_system_info['unit_serial_number']
    , gpr_system_info['window_time_shift_reference_ps']))

# Set the window time shift based on the reference value from GPR system information,
# so that first break appears is at FIRST_BREAK_POINT (#20 in this example). If it doesn't exist use
# the default value.
window_time_shift_ps = -55000
if gpr_system_info['window_time_shift_reference_ps'] is not None:
    window_time_shift_reference_ps = int(gpr_system_info['window_time_shift_reference_ps'])
    window_time_shift_ps = window_time_shift_reference_ps - (FIRST_BREAK_POINT * TIME_SAMPLING_INTERVAL_PS)

# Use the GPR data socket command to get data socket's port
data_socket_json_response = get_requests(DATA_SOCKET_CMD, "GPR Data Socket")
# Get the data socket port
data_socket_port = data_socket_json_response['data']['data_socket']['port']
# Use the port to connect to the data socket
data_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
data_socket.connect((IP_ADDRESS, data_socket_port))

# Create configuration struct for NIC setup command
setup_nic_configuration = {'data': json.dumps(
    {"gpr0": {"parameters": {'points_per_trace': POINTS_PER_TRACE,
                             'window_time_shift_ps': window_time_shift_ps,
                             'point_stacks': POINT_STACKS,
                             'time_sampling_interval_ps': TIME_SAMPLING_INTERVAL_PS
                             }},
     "timer": {"parameters": {"period_s": PERIOD_S}}})}

# Use the NIC Setup command to setup the gpr and timer
setup_nic_json_response = put_requests(SETUP_CMD, setup_nic_configuration, "Setup")
# Confirm we've received a successful response
if setup_nic_json_response is None:
    data_socket.close()
    quit()

# Use the GPR data acquisition command to start data collection
start_acquisition_json_response = put_requests(ACQUISITION_CMD, START_ACQUISITION_CONFIGURATION, "Start Acquisition")
# Confirm we've received a successful response
if start_acquisition_json_response is None:
    data_socket.close()
    quit()

gpr_data = b''
gpr_data_size_bytes = HEADER_SIZE_BYTES + (POINTS_PER_TRACE * POINT_SIZE_BYTES)
num_traces_received = 0
trace_num = 0
# Continue printing traces until we receive 10
while trace_num < 10:
    gpr_data = gpr_data + data_socket.recv(gpr_data_size_bytes)
    # Calculate the number traces received by the socket
    num_traces_received = int(len(gpr_data) / gpr_data_size_bytes)

    for i in range(0, num_traces_received):
        (tv_sec, tv_nsec, trace_num, status, stacks, header_size), s = struct.unpack('<LLLLHH',
                                                                                     gpr_data[0:HEADER_SIZE_BYTES]), \
                                                                       gpr_data[HEADER_SIZE_BYTES:gpr_data_size_bytes]
        gpr_data = gpr_data[gpr_data_size_bytes:]
        print("Trace Header: tv_sec: {} tv_nsec: {} trace_num: {} status: {} stacks: {} header_size: {} ".format(tv_sec,
                                                                                                                 tv_nsec,
                                                                                                                 trace_num,
                                                                                                                 status,
                                                                                                                 stacks,
                                                                                                                 header_size))
        first_ten_trace_points  = (", ".join(map(str, np.frombuffer(s[0:40], dtype=np.float32))))
        print("First ten points (mV): {} \n".format(first_ten_trace_points ))

# Use the GPR data acquisition command to stop data collection
stop_acquisition_json_response = put_requests(ACQUISITION_CMD, STOP_ACQUISITION_CONFIGURATION, "Stop Acquisition")
# Close data socket
data_socket.close()
