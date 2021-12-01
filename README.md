# spidar-sdk


## Requirements 

* Python2.7 or Python3.8 install and added to your path. For more details on how to add python to your path use the following [link](https://datascience.com.co/how-to-install-python-2-7-and-3-6-in-windows-10-add-python-path-281e7eae62a). 
* NIC-500 with SDK.  
* Git must be included on your system. Follow this link to download [Git](https://git-scm.com/downloads). When installing Git make sure it's installed on your Windows Command Prompt. 

## Setup 

Commands works for python 2.7 or 3.8. If you have both you need to modify the name of the python.exe and specify the python version (i.e. python3) when running python commands. Refer to this [link](https://datascience.com.co/how-to-install-python-2-7-and-3-6-in-windows-10-add-python-path-281e7eae62a) for more details on how to update the name of the python executable.

1. Open Command Prompt from the Start Menu. 
   
2. Install a python virtual environment 

    ```python -m  pip install virtualenv```

3. Create python environment. We are calling it nic-sdk-python${VERSION}.  

    For python2 use this command:

    ```python -m virtualenv nic-sdk-python2```

    For python3 use this command: 

    ```python -m venv nic-sdk-python3```

4. Navigate to your python environment. From the command above it should state the path where the environment was installed.

    For example, I got the following output.  

    ```creator CPython3Windows(dest=C:\Users\${USERNAME}\nic-sdk, clear=False, no_vcs_ignore=False, global=False)```

    Replace PATH_TO_ENV to the path of your environment (for me it was C:\Users\${USERNAME}\nic-sdk). 

    ```cd ${PATH_TO_ENV}```

5. Activate the environment.
   
    ```Scripts\activate```  

6. Navigate back to home, create a workspace, and clone your repo. If you have a workspace clone it there. 

    Replace ${USERNAME} with your computer name.  If you get stuck use the command ```dir```. It'll tell you where you are and what files you can navigate into to using the ```cd``` command. 

    ``` cd C:\Users\${USERNAME} ```

    ``` mkdir workspace ```

    ``` cd workspace```

    ```git clone git@github.com:SensoftInc/spidar-sdk.git```

7. Navigate into the sample scrip directory 

    ```cd smc_server\sample_scripts```

8. Install the requirements to run the software. Replace ${VERSION} with the specific version you are using.

    ```python -m pip install -r requirements_python${VERSION}.txt```

9. When you are finish with your environment deactivate it

    ```deactivate```
 

## Usage 

Example scripts of ruunning SPIDAR SDK are available in the [example](example/) subfolder.

### Collection

This sample script demonstrates how to collect data from a NIC500.

To run the [collection](example/collect_data_from_nic500_sdk.py) script navigate into the example directory and use the following command. 

```python collect_data_from_nic500_sdk.py```

### Data Socket Reset 

This sample script demonstrates how to run reset data socket command during collection. An example use case of this command is when Ethernet cable disconnects from the NIC500 and Computer.  

To run the [reset data socket](example/reset_data_socket_during_collection_sdk.py) script navigate into the example directory and use the following command. 

```python reset_data_socket_during_collection_sdk.py```

Each script will output what commands it ran. For more details on what the script does refer to the python file.

## Copyright and License

```
Copyright 2021 Sensors and Software Inc. All rights reserved.

TODO: Add Software License 
```