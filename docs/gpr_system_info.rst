******************
System Information
******************

This resource allows the client to get system information including component versions and serial numbers from the GPR.

.. list-table::
   :widths: 25 75
   :header-rows: 0

   * - Resource
     - api/nic/gpr/system_information
   * - Returns
     - system information structure
   * - Supported methods
     - * GET: Read the version and serial number information from the GPR and antennas.

Attributes
==========

.. list-table::
   :widths: 25 25 50
   :header-rows: 1

   * - Field
     - Type
     - Description
   * - unit_ser_num
     - String
     - Serial number of the enclosure
   * - gic_serial_number
     - String
     - Serial number of the GIC board
   * - app_code_version
     - String
     - Version of software running on the device
   * - app_code_dip
     - String
     - DIP number of the software running on the device
   * - type
     - String
     - Identifies a device as RX or TX
   * - window_time_shift_reference_ps
     - String
     - The window time shift value to set to have first break appear at point 1 on the trace.


Read the GPR system information
===============================

Sample request
--------------

.. tabs::

  .. code-tab:: python

    response = requests.get("http://192.168.20.221:8080/api/nic/gpr/system_information")

  .. code-tab:: console curl

    curl http://192.168.20.221:8080/api/nic/gpr/system_information

Sample response data
--------------------

.. code-block:: json

   {
   "data": {
    "gpr": {
      "dev1": {
        "unit_serial_number": "000066660000",
        "type": "TX",
        "app_code_dip": "2004-00229-01",
        "app_code_version": "NA"
      },
      "dev0": {
        "unit_serial_number": "000066660000",
        "type": "RX",
        "app_code_dip": "2004-00226-02",
        "app_code_version": "NA"
      },
      "unit_serial_number": "FFFFFFFFFFFF",
      "app_code_version": "3.039",
      "gic_serial_number": "006794570024",
      "app_code_dip": "2014-00092-05",
      "window_time_shift_reference_ps": -45000
    }
   }

Errors
======

GPR Not Powered
---------------
(Status Code: 4001)

This status code is returned for any of the following reasons:

    - The connected GPR device is not powered on.
    - The specified GPR device is not connected.
    - The GPR is currently in an error state and cannot be read properly.