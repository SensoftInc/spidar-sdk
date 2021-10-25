Acquisition
###########

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

Acquisition State Attributes
****************************

.. list-table::
   :widths: 25 25 50
   :header-rows: 1

   * - Field
     - Type
     - Description
   * - state
     - Integer
     - 0, 1, 2 state requested for the NIC that are corresponding to stop, running and paused.

Read the acquisition state
**************************

Sample request
--------------

.. code-block:: python

    response = requests.get("http://192.168.20.221:8080/api/nic/acquisition")

.. code-block:: console

    curl http://192.168.20.221:8080/api/nic/acquisition

Sample response data
--------------------

.. code-block:: json

   {
   "data": {
    "state": 0
   }

Start data acquisition
**********************

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
******

GPR Not Powered
---------------
(Status Code: 4001)

The connected GPR device is not powered on

GPR Not Running
---------------
(Status Code: 4003)

Returned when the connected GPR device is not running and a stop or pause state is input

GPR Already Running
---------------
(Status Code: 4004)

Returned when the connected GPR device is already running and a start state is input

GPR Not Initialized
---------------
(Status Code: 4005)

Returned when a start state is input, but the connected GPR device has not been initialized with the setup command first

Invalid Parameter Format
------------------------
(Status Code: 0011)

An INVALID_PARAMETER_FORMAT error is returned if any of the input parameters have a type mismatch from the expected format

Warnings
********

No transmitter detected
-----------------------

No transmitter was detected on power up.