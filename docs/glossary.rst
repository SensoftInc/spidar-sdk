********
Glossary
********

Resource
========

An object with type, data, relationships to other resources and set of methods to operate on it. For example,
in the endpoint "api/nic/system_information", "nic" is a resource which represents NIC-500 device, and
"system_information" is a resource which can respond with serial number and version information from it.

Request
=======

An action performed on a resource. SPIDAR SDK supports GET and PUT type requests. GET requests are used to retrieve
data from a resource. PUT request are used to change the resource's data. Not all resources support both types
of requests, please see the resource documentation for more information.


Response
========

Each request to SPIDAR SDK's API will generate a standard response. Each response is represented as a JSON dictionary
structure with "status", "message", "data" and "success" fields. The following example is a response of
nic/power resource:

.. code-block:: json

    {
      "status": {
        "status_code": 0,
        "message": "The command executed successfully",
        "type": "SUCCESS",
        "source": "nic/power",
        "title": "Success"
      },
      "message": "The command executed successfully",
      "data": {
        "state": 1
      },
      "success": true
    }

"status" field is a dictionary structure which describes the execution state of the resource, "message" is a human
readable string of status description, "data" is a dictionary structure returned by the resource as the execution
result, and "success" is a boolean success indicator of the execution status.


Status
------

An API status structure will be returned in every response from requests to SPIDAR SDK. This structure contains
information that describes the result of a request sent to a resource. This includes whether or not the request was
completed successfully and any errors that occurred while executing the request and information to help diagnose the
error, etc.

Attributes
^^^^^^^^^^

.. list-table::
   :widths: 20 25 100
   :header-rows: 1

   * - Key
     - Data type
     - Description
   * - status_code
     - integer
     - An integer representing the status returned. A status code of 0 represents success. Each status code will
       represent a standard status that can be returned. The documentation for each resource explains the expected
       error codes.
   * - message
     - string
     - A human readable description of the status returned. This message will contain additional information about the
       status.
   * - type
     - string
     - One of the following status types will be returned:

       * SUCCESS: Indicates that the command was executed successfully.
       * WARNING: Indicates the request completed but this specific use of the resource is not recommended.
       * ERROR: Indicates that a problem has occurred during the command execution and that it failed to complete
         successfully.
       * FATAL: Indicates that something has caused a system level issue / crash and that normal operation of the
         system may not continue without some action taken to restore it. Typically this will mean that something must
         be rebooted, either a device or the entire system.

   * - source
     - string
     - URI of resource that generated this status.
   * - title
     - string
     - Short descriptor of the status returned.

Sample SUCCESS status
^^^^^^^^^^^^^^^^^^^^^

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

Sample ERROR status
^^^^^^^^^^^^^^^^^^^

.. code-block:: json

    {
        "status": {
            "status_code": 9,
            "message": "The requested command is not supported",
            "type": "ERROR",
            "source": "nic/unknown_resource",
            "title": "CommandNotSupported"
        }
    }

Uniform Resource Identifier (URI)
=================================

Name of physical or logical resource accessible through the API.

Uniform Resource Locator (URL)
==============================

Address of a URI including the protocol identifier. For example, "http://192.168.20.221:8080/api/nic" is the
URL, "nic" is the URI.