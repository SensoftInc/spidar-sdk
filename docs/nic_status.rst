Status
######

This resource gets status information from the NIC including battery voltage and processor temperature.

.. list-table::
   :widths: 25 75
   :header-rows: 0

   * - Resource
     - api/nic/status
   * - Returns
     - NIC status structure
   * - Supported methods
     - * GET: Read current status information such as battery voltage and processor temperature

NIC System Attributes
*********************

.. list-table::
   :widths: 25 25 50
   :header-rows: 1

   * - Field
     - Type
     - Description
   * - processor/temperature_c
     - Float
     - Temperature of the CPU in degrees centigrade
   * - power/input_voltage
     - Float
     - Voltage measured at the input of the NIC-500
   * - memory/bytes_total
     - Float
     - Total amount of RAM available in bytes
   * - memory/bytes_free
     - Float
     - Amount of unused RAM in bytes
   * - memory/bytes_used
     - Float
     - Amount of used RAM in bytes
   * - memory/percent_free
     - Float
     - Amount of RAM free as a percentage of the total available
   * - memory/percent_used
     - Float
     - Amount of RAM used as a percentage of the total available

Read the NIC system information
*******************************

Sample request
--------------

**Python**

.. code-block:: python

    response = requests.get("http://192.168.20.221:8080/api/nic/status")

**curl**

.. code-block:: console

    curl http://192.168.20.221:8080/api/nic/status

Sample response data
--------------------

.. code-block:: json

    {
        "processor": {
            "temperature_c": 32.4
        },
        "power": {
            "input_voltage": 12.2
        },
        "memory": {
            "bytes_free": 503791616,
            "bytes_total": 1052139520,
            "percent_free": 47.9,
            "percent_used": 52.1,
            "bytes_used": 548347904
        }
    }
