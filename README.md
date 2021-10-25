# spidar-sdk


## Requirements 

* Python2.7 or Python3.8 install and added to your path. For more details on how to add python to your path use the following [link](https://datascience.com.co/how-to-install-python-2-7-and-3-6-in-windows-10-add-python-path-281e7eae62a). 
* NIC-500 with OEM.  
* Git must be included on your system. Follow this link to download [Git](https://git-scm.com/downloads). 

## Setup 

Commands works for python 2.7 or 3.8. If you have both you need to modify the name of the python.exe and specify the python version (i.e. python3) when running python commands. Refer to this [link](https://datascience.com.co/how-to-install-python-2-7-and-3-6-in-windows-10-add-python-path-281e7eae62a) for more details on how to update the name of the python executable. 

1. Open Command Prompt from the Start Menu. 
   
2. Install a python virtual environment 

    ```python -m  pip install virtualenv```

3. Create python environment. We are calling it nic-oem-python${VERSION}.  

    For python2 use this command:

    ```python -m virtualenv nic-oem-python2```

    For python3 use this command: 

    ```python -m venv nic-oem-python3```

4. Navigate to your python environment. From the command above it should state the path where the environment was installed.

    For example, I got the following output.  

    ```creator CPython3Windows(dest=C:\Users\ygnanamuttu\nic-oem, clear=False, no_vcs_ignore=False, global=False)```

    Replace PATH_TO_ENV to the path of your environment (for me it was C:\Users\ygnanamuttu\nic-oem). 

    ```cd ${PATH_TO_ENV}```

5. Activate the environment.
   
    ```Scripts\activate```  

6. Navigate back to home, create a workspace, and clone your repo. If you have a workspace clone it there. 

    Replace ${USERNAME} with your computer name.  If you get stuck use the command ```dir```. It'll tell you where you are and what files you can navigate into to using the ```cd``` command. 

    ``` cd C:\Users\${USERNAME} ```

    ``` mkdir workspace ```

    ``` cd workspace```

    ```git clone git@github.com:SensoftInc/smc_server.git```

7. Navigate into the sample scrip directory 

    ```cd smc_server\sample_scripts```

8. Install the requirements to run the software. Replace ${VERSION} with the specific version you are using.

    ```python -m pip install -r requirements_python${VERSION}.txt```

9. When you are finish with your environment deactivate it

    ```deactivate```
 

## Usage 

To run the collection script use the following command. 

```python collect_data_from_nic500_oem.py```


To run the scoping script use the following command. 

```python scope_nic500_oem.py```

Each script will output what commands it ran. For more details on what the script does refer to the python file.