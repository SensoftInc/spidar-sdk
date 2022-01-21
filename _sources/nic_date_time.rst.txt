*************
Date and Time
*************

This resource allows the client to get or set the current date and time on the NIC. Time is stored
without a timezone offset.

.. list-table::
   :widths: 25 75
   :header-rows: 0

   * - Resource
     - api/nic/date_time
   * - Returns
     - date/time structure
   * - Supported methods
     - * GET: Read the current date and time from the NIC
       * PUT: Set the date and/or time on the NIC

Attributes
==========

.. list-table::
   :widths: 25 25 50
   :header-rows: 1

   * - Field
     - Type
     - Description
   * - date_time
     - string
     - The current date and time formatted as ISO8601 standard.
   * - year
     - integer
     - A four digit year.
   * - month
     - integer
     - A value between one and 12.
   * - day
     - integer
     - A value between one and 31.
   * - hour
     - integer
     - A value between zero and 23.
   * - minute
     - integer
     - A value between zero and 59.
   * - second
     - integer
     - A value between zero and 59.
   * - tz_offset
     - string
     - Timezone offset in the format +/-HHMM.

Read the date and time
======================

Sample request
--------------

.. tabs::
  
   .. code-tab:: python

      response = requests.get("http://192.168.20.221:8080/api/nic/date_time")

   .. code-tab:: console curl

      curl http://192.168.20.221:8080/api/nic/date_time

Sample response data
--------------------

.. code-block:: json

   {
   "data": {
    "date_time": "2021-05-08T03:56:02+0000",
    "hour": 3,
    "month": 5,
    "second": 2,
    "year": 2021,
    "day": 8,
    "minute": 56
   }

Set the date and time
=====================

Sample request
--------------

**Python**

.. code-block:: python

    date_time = json.dumps({"year": 2021, "month": 4, "day": 14, "hour": 20, "minute": 8, "second": 02, "tz_offset": "+0100"})
    response = requests.put("http://192.168.20.221:8080/api/nic/date_time", data={"data": date_time})

Sample response
---------------

.. code-block:: json

   {
   "data": {
    "date_time": "2021-04-14T20:08:02+0000",
    "hour": 20,
    "month": 4,
    "second": 2,
    "year": 2021,
    "day": 14,
    "minute": 08
   }

Errors
======

Value Out of Range
------------------
(Status Code: 0008)

This status code is returned for any of the following reasons:

- The date may not be set earlier than 2017-01-01. A VALUE_OUT_OF_RANGE error will be returned if the year or a combination of year and offset are set less than 2017.
- If any of the fields are out of their normal range, a VALUE_OUT_OF_RANGE error will be returned. For example, if the requested month 15, or hour is 28.

Invalid Parameter Format
------------------------
(Status Code: 0011)

Returned if any of the input parameters have a type mismatch from the expected format.

GPR Already Running
-------------------
(Status Code: 4004)

The date and time cannot be changed while the GPR is acquiring data as it would affect the time stamps on the GPR's
data stream.

