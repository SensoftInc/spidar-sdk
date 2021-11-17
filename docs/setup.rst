Setup
#####

This resource allows the client to get or set the configuration of devices connected to the NIC.

.. list-table::
   :widths: 25 75
   :header-rows: 0

   * - Resource
     - api/nic/setup
   * - Returns
     - gpr and timer parameter structure
   * - Supported methods
     - * GET: Read the parameter structure from all connected devices.
       * PUT: Set the parameter structure for any or all connected devices.

Date/Time Attributes
********************

.. list-table::
   :widths: 25 25 50
   :header-rows: 1

   * - Field
     - Type
     - Description
   * - timer
     - Timer parameter structure
     -
   * - period_s
     - Float
     - Interval between trigger events when the GPR trigger mode is set to "Free".
   * - gpr
     - GPR parameter structure
     -
   * - points_per_trace
     - Integer
     - Number of sample points to collect per trace.
   * - time_sampling_interval_ps
     - Integer
     - The time interval between sample points on a trace.
   * - frequency_MHz
     - Float
     - The centre frequency of the GPR transmitting and receiving antenna.
   * - point_stacks
     - Integer
     - Point stacks are collected at the receiver. Must be a power of 2, between 1 and 32768.
   * - trigger_mode
     - String
     - Method used for triggering GPR trace acquisition. Must be "Free" or "Pulse".
   * - window_time_shift_ps
     - Integer
     - Offset used to position the receiver's recording window within range of the transmitter pulse. For monostatic GPRs, the window time shift reference is the calibrated value necessary to place first break at point 1 on the trace.

Read the setup
**************

Sample request
--------------

.. code-block:: python

    response = requests.get("http://192.168.20.221:8080/api/nic/setup")

.. code-block:: console

    curl http://192.168.20.221:8080/api/nic/setup

Sample response data
--------------------

.. code-block:: json

    {
        "data": {
        "timer": {
            "parameters": {
                "period_s": 1
            }
        },
        "gpr0": {
            "parameters": {
                "time_sampling_interval_ps": 100,
                "frequency_MHz": 1000,
                "point_stacks": 4,
                "trigger_mode": "Free",
                "window_time_shift_ps": -37000,
                "points_per_trace": 200
            }
        }
    }

Change the setup
****************

Sample request
--------------

**Python**

.. code-block:: python

    configuration = json.dumps({"gpr": {"parameters": {"points_per_trace": 200, "point_stacks": 32}}, "timer": {"parameters": {"period_s": 0.1}}})
    response = requests.put("http://192.168.20.221:8080/api/smc/setup", data={"data": configuration})

.. code-block:: console

    curl -X PUT --data-urlencode "data={\"gpr\": {\"point_stacks\": 2048}}" http://192.168.20.221:8080/api/smc/setup

Sample response
---------------

.. code-block:: json

    {
        "data": {
        "timer": {
            "parameters": {
              "period_s": 0.1
            }
        },
        "gpr": {
            "parameters": {
                "time_sampling_interval_ps": 100,
                "frequency_MHz": 1000,
                "point_stacks": 32,
                "trigger_mode": "Free",
                "window_time_shift_ps": -37000,
                "points_per_trace": 200
            }
        }
    }


GPR Parameter Ranges
*********************

.. list-table::
   :widths: 45 20 20 20 100
   :header-rows: 1

   * - Parameter
     - Default
     - Min
     - Max
     - Resolution
   * - points_per_trace
     - 100
     - 70
     - 30000
     - 1
   * - time_sampling_interval_ps
     - 100
     - 50
     - 6400
     - 50
   * - point_stacks
     - 1
     - 1
     - 32768
     - One of [1, 2, 4, 6, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384, 32768]
   * - window_time_shift_ps
     - -48000
     - -50000000
     - 50000000
     - 5
   * - trigger_mode
     - "Free"
     - n/a
     - n/a
     - One of ["Free", "Pulse", 0, 3]
   * - period_s
     - 1
     - 0.00125
     - 60
     - any


Errors
******

Value out of range
------------------
(Status Code: 0008)

This status code is returned for any of the following reasons:

    - One or more parameters are out of the defined range.
    - An input parameter is outside the allowed range of values.
    - The input combination of points_per_trace and time_sampling_interval_ps result in a time_window outside the allowed range.

Invalid Input Parameter Format
------------------------------
(Status Code: 0011)

This status code is returned for any of the following reasons:

    - When the input parameter is not in a JSON readable format.
    - When either the input timer or the gpr doesn't contain a "parameters" key.

GPR Not Powered
---------------
(Status Code: 4001)

The connected GPR device is not powered on

GPR Already Running
-------------------
(Status Code: 4004)

The connected GPR device is currently acquiring data and must be stopped before running setup

Warnings
********

Unrecognized Input
------------------
(Status Code: 912)

This warning is returned if any of the input parameters were unrecognized and as a result did not apply any changes to the system

Modified Input
--------------
(Status Code: 913)

This warning is returned when an input value is not in the proper resolution. The input value will be rounded to the closest valid value and accepted

