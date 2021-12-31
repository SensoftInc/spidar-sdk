***
GPR
***

This resource retrieves a list of available resources from the GPR. The GPR is a sub-resource of the NIC. The GPR
resource is limited to retrieving system information such as serial and version numbers, and control of the data
socket over which trace data are sent.

.. list-table::
   :widths: 25 75
   :header-rows: 0

   * - Resource
     - api/nic/gpr
   * - Returns
     - List of resources associated with the GPR.
   * - Supported methods
     - * GET: Retrieve a list of resources

Resources
=========

.. toctree::
   :maxdepth: 1

   gpr_system_info
   gpr_data_socket
   gpr_data_socket_reset


Data Format
===========

The GPR data are sent in trace format, each trace contains a header with information about the trace, and a data portion
with the amplitude information received by the GPR. Data transmitted across the network is broken up to optimize
transfer speeds, and may not always be whole traces. When reading data from the socket, the client must know the
expected size of traces in bytes to ensure all the data is read. The size of a single trace is computed as:

.. code-block::

   trace_size_in_bytes = points_per_trace * bytes_per_point + trace_header_size_in_bytes

where:

.. code-block::

   trace_header_size_in_bytes = 20
   bytes_per_point = 4

Field list
----------

.. list-table::
   :widths: 20 30 60
   :header-rows: 1

   * - Field
     - Type
     - Description
   * - tv_sec
     - integer (4 byte)
     - Integer component of the Linux timespec, in seconds.
   * - tv_nsec
     - integer (4 byte)
     - Fractional component of the Linux timespec, in nanoseconds.
   * - trace_number
     - integer (4 byte)
     - Sequential number assigned to the trace since the last reset.
   * - status
     - integer (2 byte)
     - Bitwise status flags.
   * - header_size
     - unsigned integer (2 byte)
     - Size of the header in bytes.
   * - data
     - array of float (4 byte)
     - Amplitude data presented in mV.

Time stamp
^^^^^^^^^^

The trace time stamp is presented in Linux timespec format, with a seconds and nanoseconds field. The time is measured
from Jan 1 1970 00:00 UTC, and is stored in the NIC-500's real-time clock between boot cycles. The clock can read or
set using the date_time API resource. The trace is stamped at the time of request, and so does not take into account
time take to acquire the trace.

To convert the time stamp to seconds past Jan 1 1970 00:00 UTC: tv_sec + tv_nsec / 1e9

Trace number
^^^^^^^^^^^^

The trace numbering starts at 1, and counts up sequentially for each trace requested. To reset the trace number back
to one, the PUT method must be requested successfully on the API's nic/setup resource. Once a trace has started
collecting it cannot be interrupted. If a new request is made while trace acquisition is happening, the new request
will be 'skipped' the trace number field will appear to have a gap. For instance, if a new trace request is made
while trace 5 is still being acquired, the incoming trace numbers will look like: [1, 2, 4, 4, 5, 7, 8...]. The system
will skip as many traces as necessary while acquisition is going on.

Status
^^^^^^

The status field is not used in SPIDAR SDK.

Stacks
^^^^^^

Indicates the number of stacks, or measurements used to average the trace. The stacks field should match the
point_stacks setting supplied to the :ref:`nic_setup_label` resource.

Header size
^^^^^^^^^^^

The header size is currently fixed at 20 bytes. The consuming application should read this field to determine how
many bytes to skip before reading the data portion of the trace. In future releases of the API, the header size may
change to incorporate new data, and legacy applications can safely skip over these fields if they are not understood.

Data
^^^^

The data portion of the trace contains and array of 4 byte floats representing the received GPR amplitude in mV.
The data points have already been normalized for stacks. The time between points is determined by the
time_sampling_interval_ps in the :ref:`nic_setup_label` resource.
