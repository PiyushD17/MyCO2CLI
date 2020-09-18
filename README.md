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

```
pip3 install setuptools
```

* You might need to install pip3 as well in case the above command does not work.
```
sudo apt install python3-pip
```
## How to use?
* Fork this repository.
* Make sure you create an empty directory and initalize it with **git init** if using **git pull**.

```
mkdir your_dir_name
cd your_dir_name
git init
git pull https://github.com/PiyushD17/MyCO2CLI.git
```

* Or, you can directly download the zip file.

### Installing the tool
* Ensure that you are in the project directory (same directory as of the **setup.py** file).
* Now, you can install the tool from here.

```
sudo python3 setup.py install
```
### Executing commands using the tool
* Now that you have installed the tool, you can simply use it from the Command Line when inside your project directory.
```console
myco2cli --transportation-method medium-diesel-car --distance 15 --unit-of-distance km
Your trip caused 2.6kg of CO2-equivalent.
```

```
myco2cli --distance 1800.5 --transportation-method large-petrol-car

myco2cli --transportation-method train --distance 14500 --unit-of-distance m

myco2cli --transportation-method train --distance 14500 --unit-of-distance m --output kg

myco2cli --unit-of-distance=km --distance 15 --transportation-method=medium-diesel-car
```
* To get more info about the tool:
```
myco2cli --help
```
### Testing the tool
* To test the tool, **cd** into the directory that contains the test script: **test_co2calc.py**.
* Run the tests

```
cd tests

python3 test_co2calc.py
```
