Glossary
########

Uniform Resource Identifier (URI)
=================================

Name of physical or logical resource accessible through the API.

Uniform Resource Locator (URL)
==============================

Address of a URI including the protocol identifier. For example, "http://192.168.20.221:8080/api/nic" is the
URL, "nic" is the URI.

Resource
========

An object with type, data, relationships to other resources and set of methods to operate on it. For example,
in the endpoint "api/nic/system_information", "nic" is a resource which represents SmartController device, and
"system_information" is a resource which can access serial number and version information from it.

Request
=======

An action performed on a resource. SPIDAR-OEM supports GET and PUT type requests. GET requests are used to retrieve
data from a resource. PUT request are used to change the resource's data.

Response
========

Standard response returned by the SPIDAR-OEM server. It is in JSON dictionary structure with "status", "message",
"data" and "success" fields. The following example is a response of system_information resource:

.. code-block:: json

    {
        "status": {
            "status_code": 0,
            "message": "The command executed successfully",
            "type": "SUCCESS",
            "source": "nic/system_information",
            "title": "Success"
        },
        "message": "The command executed successfully",
        "data": {
            "smc_api_build": "1783",
            "fpga_version": "24",
            "app_dip": "",
            "kernel_version": "3.10.17",
            "hardware_id": "000000000000",
            "os_dip": "2017-00041-10",
            "os_version": "2.10.583",
            "nic_serial_number": "0000-0000-0000",
            "app_version": "V1R4B111"
        },
        "success": true
    }

"status" field is a dictionary structure which describes the execution state of the resource, "message" is a human
readable string of status description, "data" is a dictionary structure returned by the resource as the execution
result, and "success" is a boolean success indicator of the execution status.


API Status
***********

An API_STATUS structure will be returned in every response from requests to SPIDAR-OEM This structure contains information
that describes the result of a request sent to a resource. This includes whether or not the request was completed successfully,
any errors that occurred while executing the request and information to help diagnose the error, etc.

API Status Attributes
----------------------

.. list-table::
   :widths: 20 25 100
   :header-rows: 1

   * - Field
     - data type
     - Description
   * - status_code
     - int
     - An integer representing the status returned. A status code of 0 represents success. Each status code will represent a standard status that can be returned
   * - message
     - string
     - A human readable description of the status returned. This message will contain additional information about the status
   * - type
     - string
     - One of the following status types will be returned:

       * SUCCESS: An API_STATUS of type SUCCESS is used to indicated that the command was executed successfully.
       * WARNING: An API_STATUS of type WARNING is used to tell the user that the command completed but this specific use of the command is not recommended.
       * ERROR: An API_STATUS of type ERROR is used to indicate that an error has occurred during the command execution and that it failed to complete successfully.
       * FATAL: An API_STATUS of type FATAL is used to indicate that something has caused a system level issue / crash and that normal operation of the system may not continue without some action taken to restore it. Typically, this will mean that something must be rebooted, either a device or the entire system.

   * - source
     - string
     - URI of resource that generated this status
   * - title
     - string
     - Short descriptor of the status returned



Sample SUCCESS Status
---------------------

.. code-block:: json

    {
        "status": {
            "status_code": 0,
            "message": "The command executed successfully",
            "type": "SUCCESS",
            "source": "nic/system_information",
            "title": "Success"
        }
    }

Sample ERROR Status
-------------------

.. code-block:: json

    {
        "status": {
            "status_code": 9,
            "message": "The requested command is not supported",
            "type": "ERROR",
            "source": "nic/bad_command",
            "title": "CommandNotSupported"
        }
    }