******************
System Information
******************

This resource allows the client to get system information including component versions and serial numbers from the NIC.

.. list-table::
   :widths: 25 75
   :header-rows: 0

   * - Resource
     - api/nic/system_information
   * - Returns
     - system information structure
   * - Supported methods
     - * GET: Read the version and serial number information from the NIC

Attributes
==========

.. list-table::
   :widths: 25 25 50
   :header-rows: 1

   * - Field
     - Type
     - Description
   * - smc_api_build
     - string
     - Build number of the smc api.
   * - fpga_version
     - string
     - Version of the installed fpga.
   * - app_dip
     - string
     - DIP number of the application.
   * - kernel_version
     - string
     - Version of the installed kernel.
   * - hardware_id
     - string
     - Unique identifier of the NIC hardware.
   * - os_dip
     - string
     - DIP number of the operating system.
   * - os_version
     - string
     - Version of the NIC operating system.
   * - nic_serial_number
     - string
     - Serial number of the NIC.
   * - app_version
     - Dict
     - Application version information.

Read the NIC system information
===============================

Sample request
--------------

.. tabs::

  .. code-tab:: python

    response = requests.get("http://192.168.20.221:8080/api/nic/system_information")

  .. code-tab:: console curl

    curl http://192.168.20.221:8080/api/nic/system_information

Sample response data
--------------------
.. code-block:: json

   {
    "data": {
        "smc_api_build": "1829",
        "fpga_version": "29",
        "app_dip": "2018-00023-03",
        "kernel_version": "3.10.17",
        "hardware_id": "001EC0AF2D9B",
        "os_dip": "2017-00041-08",
        "os_version": "2.11.622",
        "nic_serial_number": "123456789012",
        "app_version": "V1R4B1223"
    }
   }
