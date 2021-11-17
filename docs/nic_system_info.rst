NIC System Information
######################

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

NIC System Attributes
*********************

.. list-table::
   :widths: 25 25 50
   :header-rows: 1

   * - Field
     - Type
     - Description
   * - smc_api_build
     - String
     - Build number of the smc api.
   * - fpga_version
     - String
     - Version of the installed fpga.
   * - app_dip
     - String
     - DIP number of the application.
   * - kernel_version
     - String
     - Version of the installed kernal.
   * - hardware_id
     - String
     - Unique identifier of the NIC hardware.
   * - os_dip
     - String
     - DIP number of the operating system.
   * - os_version
     - String
     - Version of the NIC operating system.
   * - nic_serial_number
     - String
     - Serial number of the NIC.
   * - app_version
     - Dict
     - Application version information.

Read the NIC system information
*******************************

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
        "smc_api_build": "1128",
        "fpga_version": "24",
        "app_dip": "",
        "kernel_version": "3.10.17",
        "hardware_id": "001EC0AF2D9B",
        "os_dip": "2017-00041-08",
        "os_version": "2.08.512",
        "nic_serial_number": "",
        "app_version": "V1R4B111"
    }
   }
