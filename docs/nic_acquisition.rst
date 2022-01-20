***********
Acquisition
***********

This resource allows the client to get or set the acquisition state devices connected to the NIC.

.. list-table::
   :widths: 25 75
   :header-rows: 0

   * - Resource
     - api/nic/acquisition
   * - Returns
     - acquisition state structure
   * - Supported methods
     - * GET: Read the acquisition state.
       * PUT: Set the acquisition state.

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
     - integer
     - 0
     - Stop data acquisition and reset the trace numbering.
   * -
     -
     - 1
     - Start data acquisition.
   * - 
     -
     - 2
     - Pause data acquisition, does not reset trace number. Start acquisition again to resume.

  
Read the acquisition state
==========================

Sample request
--------------

.. tabs::

  .. code-tab:: python

      response = requests.get("http://192.168.20.221:8080/api/nic/acquisition")

  .. code-tab:: console curl

      curl http://192.168.20.221:8080/api/nic/acquisition

Sample response data
--------------------

.. code-block:: json

   {
   "data": {
    "state": 0
   }

Start data acquisition
======================

Sample request
--------------

**Python**

.. code-block:: python

    acq_state = json.dumps({"state": 1})
    response = requests.put("http://192.168.20.221:8080/api/nic/acquisition", data={"data": acq_state})

Sample response
---------------

.. code-block:: json

   {
   "data": {
    "state": 1
   }

Errors
======

Invalid Parameter Format
------------------------
(Status Code: 0011)

Returned if any of the input parameters have a type mismatch from the expected format.

GPR Not Powered
---------------
(Status Code: 4001)

The connected GPR device is not powered on.

GPR Not Running
---------------
(Status Code: 4003)

Returned when the connected GPR device is not running and a stop or pause state is input.

GPR Already Running
-------------------
(Status Code: 4004)

Returned when the connected GPR device is already running and a start state is input.

GPR Not Initialized
-------------------
(Status Code: 4005)

Returned when a start state is input, but the connected GPR device has not been initialized with the setup command first.
