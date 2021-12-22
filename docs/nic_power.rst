*****
Power
*****

This resource allows the client to get or set the power state of devices connected to the NIC. When the NIC is booted,
connected devices such as the GPR will remain off until requested to turn on. Once the GPR is turned on, it cannot be
turned off except by powering down the NIC.

.. list-table::
   :widths: 25 75
   :header-rows: 0

   * - Resource
     - api/nic/power
   * - Returns
     - power state structure
   * - Supported methods
     - * GET: Read the power state of all connected devices.
       * PUT: Set the power state of all devices including the NIC.

Attributes
==========

.. list-table::
   :widths: 20 20 10 50
   :header-rows: 1

   * - Field
     - Type
     - Option
     - Description
   * - state
     - Integer
     - 0
     - All devices including NIC turned off.
   * -
     -
     - 1
     - NIC is on but all connected devices are off.
   * -
     -
     - 2
     - NIC and all connected devices are turned on.

Read the power state
====================

Sample request
--------------

.. tabs::

  .. code-tab:: python

    response = requests.get("http://192.168.20.221:8080/api/nic/power")

  .. code-tab:: console curl

    curl http://192.168.20.221:8080/api/nic/power

Sample response data
--------------------

.. code-block:: json

   {
   "data": {
    "state": 1
   }

Turn on all connected devices
=============================

Sample request
--------------

**Python**

.. code-block:: python

    power_state = json.dumps({"state": 2})
    response = requests.put("http://192.168.20.221:8080/api/nic/power", data={"data": power_state})

Sample response
---------------

.. code-block:: json

   {
   "data": {
    "state": 2
    }
   }

Errors
======

Value Out Of Range
------------------
(Status Code: 0008)

This error is returned when the input state is not an accepted value

GPR Not Powered
---------------
(Status Code: 4001)

This status code is returned for any of the following reasons:

- The connected GPR device is not powered on.
- The specified GPR device is not connected.

GPR Type Not Supported
----------------------
(Status Code: 4013)

GPR Type Not Supported is returned when the connected GPR device is not supported in SPIDAR SDK mode

GPR No Receiver Detected
------------------------
(Status Code: 4016)

This error is returned when there is no receiver detected on a GPR device

GPR Multiple Receivers Detected
-------------------------------
(Status Code: 4017)

This error is returned when more than one receiver is detected on a single GPR device

GPR Frequency Mismatch
----------------------
(Status Code: 4018)

A Frequency Mismatch occurs when the center frequency of the Rx or Tx on the GPR device is not supported by the other

Warnings
========

No Transmitted Detected
-----------------------
(Status Code: 919)

This warning is returned when there is no transmitter detected on the GPR device. The device can still be used to
collect data but will only be listening to background noise