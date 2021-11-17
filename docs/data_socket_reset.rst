Data Socket Reset
#################

This resource sends a command to the server to reset data socket when there is a network connection failure.

.. list-table::
   :widths: 25 75
   :header-rows: 0

   * - Resource
     - api/nic/gpr/data_socket_reset
   * - Returns
     - status message
   * - Supported methods
     - * PUT: Reset data socket

Data Socket Reset Attributes
****************************

N/A

Reset the Data Socket Port
**************************

Sample request
--------------


.. tabs::
  
   .. code-tab:: python

      response = requests.put("http://192.168.20.221:8080/api/nic/gpr/data_socket_reset", data={"data": {}})

   .. code-tab:: console

      curl -X PUT --data-urlencode "data={}" http://192.168.20.221:8080/api/nic/gpr/data_socket

Sample response data
--------------------

.. code-block:: json

   {
   "data": {}
   }
