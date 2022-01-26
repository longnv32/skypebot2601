# skypebot

## python 3.9
- Prerequisites
```
sudo apt update 
sudo apt install software-properties-common 
```
- Install Python 3.9 Using Apt-Get
```
sudo add-apt-repository ppa:deadsnakes/ppa 
sudo apt update 
sudo apt install python3.9 
```
- Add Python 3.6 & Python 3.9 to update-alternatives
```
sudo update-alternatives --install /usr/bin/python3 python3 /usr/bin/python3.6 1
sudo update-alternatives --install /usr/bin/python3 python3 /usr/bin/python3.9 2
```
- Update Python 3 for point to Python 3.9
```
sudo update-alternatives --config python3
```
- Test 
```
python3.9 -V 
```
## pip
- install 
```
sudo apt install python3-pip python3.9-distutils
pip3 install -U pip
```
## virtualenv
- install
```
pip3 install --upgrade virtualenv
```
- create folder env
```
python -m virtualenv venv
```
- active folder 
```
source ./venv/bin/activate
```

## Add Python 3.6 & Python 3.9 to update-alternatives

## export file requirments.txt
```
pip freeze > requirements.txt
```

## import file requirments.txt
```
pip install -r requirements.txt
```