##########
SPIDAR SDK
##########

********
Overview
********

SPIDAR SDK is a system which allows users to control data acquisition, and retrieve data from a NIC-500 based system
in real time using an Application Programming Interface (API). The API is accessed by simple HTTP endpoints,
employing GET and PUT methods to retrieve and set data.

Trace data from the GPR data is pushed across a separate, long-lasting network socket which the client connects to.


.. toctree::
   :maxdepth: 1

   glossary
   nic
   gpr