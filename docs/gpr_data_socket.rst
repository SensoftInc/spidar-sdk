.. _data_socket_label:

***********
Data Socket
***********

This resource retrieves the port number to connect for data streaming.

.. list-table::
   :widths: 25 75
   :header-rows: 0

   * - Resource
     - api/nic/gpr/data_socket
   * - Returns
     - data socket port number
   * - Supported methods
     - * GET: Read the data socket port number

Attributes
==========

.. list-table::
   :widths: 25 25 50
   :header-rows: 1

   * - Field
     - Type
     - Description
   * - port
     - integer
     - Port identifier for data socket.

Read the Data Socket Port
=========================

Sample request
--------------

.. tabs::
  
   .. code-tab:: python

      response = requests.get("http://192.168.20.221:8080/api/nic/gpr/data_socket")

   .. code-tab:: console curl

      curl http://192.168.20.221:8080/api/nic/gpr/data_socket

Sample response data
--------------------

.. code-block:: json

   {
   "data": {
    "data_socket": {
     "port": 60039
     }
    }
   }


Errors
======

Command Not Supported
---------------------
(Status Code: 0009)

This error is returned when the server is unable to setup the data socket.

Device Failed to Initialized
----------------------------
(Status Code: 1006)

This error is returned when the server is unable to communicate with the data socket.