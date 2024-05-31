
# CurrencyRecognizationApp

Currency Recognization App Made Using TKINTER. It allows users to use their own model for different currencies and detect them either by browsing or capturing using camera.
It currently only supports Indian and Nepali currencies. The newer models can be added in the models folder and the code can be updated accordingly for ```predict.py``` and ```gui.py``` which should be fairly simple.

## Installation

## TKinter must be installed on your system. Install using the following command

### For Linux Users
```bash
  sudo apt-get install python3-tk
```

### Windows users can simply run the python installer, which will automatically installs TKInter.

Install the requirements using pip.

```bash
  pip install -r requirements.txt
```
OR

```bash
  python -m pip install -r requirements.txt
```
Then run the gui.py in the main folder

## Roadmap
- ~~Web app using flask~~
- ~~Android app for mobile access~~
- ~~Adding the training code~~
- ~~Docker image~~ unable to add camera features in container

## Dataset Used
- [@IndianCurrencyDataset](https://www.kaggle.com/datasets/uashutoshk/indian-currrency-dataset)
- [@NepaliCurrencyDataset](https://www.kaggle.com/datasets/uashutoshk/nepali-currency-dataset)

## Contributors
- [@Ashutosh Khanal Upadhyay](https://github.com/asup20cs)
- [@Omprakash Rana](https://github.com/Omprakash7171)
- [@Nitesh Shah](https://github.com/NiteshShah1999)

## License
[GNU General Public License v3.0](https://choosealicense.com/licenses/gpl-3.0/)

[![GPLv3 License](https://img.shields.io/badge/License-GPL%20v3-yellow.svg)](https://opensource.org/licenses/)
