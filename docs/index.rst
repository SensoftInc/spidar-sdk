###
OEM
###

OEM mode is activated by passing a -O flag as command line argument to the main file. The main differences in OEM mode
compared to the standard SPIDAR mode are:

* The software will not automatically probe (power on) the GPR on startup, but instead waits for the client request to do so.

* A limited command set is presented which is handled by the OEMSMControllerInterface instead of routing api commands directly to the underlying controllers.

.. toctree::

   overview
   glossary
   nic
   gpr