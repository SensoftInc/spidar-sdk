##########
SPIDAR SDK
##########

********
Overview
********

SPIDAR SDK is a system which allows users to control data acquisition, and retrieve data from a NIC-500 based system
in real time using an Application Programming Interface (API). The API is accessed by simple HTTP endpoints,
employing GET and PUT methods to retrieve and set data.

Trace data from the GPR data is pushed across a separate, long-lasting network socket which the client connects to and
listens for incoming data.

Control of the system is achieved by accessing resources primarily on the nic device, representing the NIC-500 hardware.
A gpr device representing the GPR hardware attached to the NIC-500 can provide information about the hardware as well
as creating and resetting the data socket.

Sample scripts written in Python are available from the `GitHub`_ repository.

Please reference the SPIDAR Operations Manual for details on how to physically connect and configure the NIC-500 SPIDAR 
system and for instructions on how to activate the SDK mode.

.. _Github: https://github.com/sensoftinc/spidar-sdk

********************
Activation Agreement
********************

.. toctree::
   :maxdepth: 1

   terms_and_conditions

************************************
Overview SPIDAR SDK API Terminology 
************************************

.. toctree::
   :maxdepth: 1

   glossary

*************************************
Devices controlled by SPIDAR SDK API
*************************************

.. toctree::
   :maxdepth: 1

   nic
   gpr

