# Balancing platform

Short description

### Prerequisites

You will need [Python 3](https://www.python.org/) for using the provided files.
Also you will need to install all the dependencies listed below.

```bash
pip install -r /path/to/requirements.txt

or

pip install opencv-python
pip install numpy
pip install pymodbus
pip install vpython
pip install matplotlib
pip install simple-pid
```

### Installing

Clone or download project as zip in any directory.
Find correct HSV settings for ball detection with morphological_transform file.
Adjust the sliders until the ball is the only thing white. 
Set the new values in the video_processing file and finish with running main.py

### Example
```bash
python main.py
```
![Output]()
![Output]()
![Output]()


## Built With

* [Python](https://www.python.org/) - Python

## Contributing

If you want to contribute or find anything wrong, please create a Pull request, or issue adressing the change, or issue.


## Author

* **Magnus Øye** - [magnusoy](https://github.com/magnusoy)


## License

This project is licensed under the MIT License - see the [LICENSE.md](https://github.com/magnusoy/Arduino-with-Python/blob/master/LICENSE) file for details


## Libraries

[OpenCV](https://docs.opencv.org/3.4.1/index.html)

[Numpy](http://www.numpy.org/)

[Vpython](http://vpython.org/)

[Matplotlib](https://matplotlib.org/index.html)

[PyModbus](https://pymodbus.readthedocs.io/en/latest/)
