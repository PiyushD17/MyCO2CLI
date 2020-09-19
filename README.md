# CO2-Tool

# About
This is a CLI Tool that returns the amount of CO2-equivalent that will be caused when traveling a given distance using a given transportation method.

CO2e per passenger per km is available for the following Transportation methods:
* Small cars:
  * small-diesel-car : 142g
  * small-petrol-car : 154g
  * small-plugin-hybrid-car : 73g
  * small-electric-car : 50g
* Medium cars:
  * medium-diesel-car : 171g
  * medium-petrol-car : 192g
  * medium-plugin-hybrid-car : 110g
  * medium-electric-car : 58g
* Large cars:
  * large-diesel-car : 209g
  * large-petrol-car : 282g
  * large-plugin-hybrid-car : 126g
  * large-electric-car : 73g
* bus : 27g
* train : 6g

## Requirements
* This tool needs Python 3.5 or higher.
* This tool will also need the **python setuptools** library to be installed.
* Install the library using the following command

```console
pip3 install setuptools
```

* You might need to install pip3 as well in case the above command does not work.
```console
sudo apt install python3-pip
```
## How to use?
* Fork the following repository: https://github.com/PiyushD17/MyCO2CLI.git.
* Make sure you create an empty directory and initalize it with **git init** if using **git pull**.

```console
mkdir cli
cd cli
git init
git pull https://github.com/PiyushD17/MyCO2CLI.git
```

* Or, you can directly download the zip file.

### Installing the tool
* Ensure that you are in the project directory (same directory as of the **setup.py** file).
* Now, you can install the tool from here.

```console
foo@bar:~/cli$ sudo python3 setup.py install
```
### Executing commands using the tool
* Now that you have installed the tool, you can simply use it from the Command Line when inside your project directory.

```console
foo@bar:~/cli$ myco2cli --transportation-method medium-diesel-car --distance 15 --unit-of-distance km
Your trip caused 2.6kg of CO2-equivalent.
```

```console
foo@bar:~/cli$ myco2cli --distance 1800.5 --transportation-method large-petrol-car
Your trip caused 507.7kg of CO2-equivalent.
```

```console
foo@bar:~/cli$ myco2cli --transportation-method train --distance 14500 --unit-of-distance m
Your trip caused 87g of CO2-equivalent.
```

```console
foo@bar:~/cli$ myco2cli --transportation-method train --distance 14500 --unit-of-distance m --output kg
Your trip caused 0.1kg of CO2-equivalent.
```

```console
foo@bar:~/cli$ myco2cli --unit-of-distance=km --distance 15 --transportation-method=medium-diesel-car
Your trip caused 2.6kg of CO2-equivalent.
```
* To get more info about the tool:
```console
myco2cli --help
```
### Testing the tool
* To test the tool, **cd** into the directory that contains the test script: **test_co2calc.py**.
* Run the tests

```console
foo@bar:~/cli$ cd tests
foo@bar:~/cli/tests $python3 test_co2calc.py
```
