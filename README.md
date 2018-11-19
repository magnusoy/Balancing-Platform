# Balancing platform

This project is in the subject Industrial Management Systems at NTNU and shall provide the basis for the final grade. The project is about making a regulation loop to balance a ball on a platform. As a result of this, the model is based on a Stewart platform with three degrees of freedom (pitch, roll, heave). The platform is moved by three DC servomotors located in each corner of an equal-sided triangle with the center as a trade fair. Furthermore, in order for the engines to lift the platform, a disc is attached to the shaft with an offset from the center. The motion of the three motors is determined by two PID controllers in a PLC, which gives an assertion calculated by errors and parameters. Finally, the assignment is turned into positions of the engines through a position matrix.

The project will be presented as part of the oral exam in the subject. The report is written according to the given technical report templates, and contains images and text from theory, methodology and the results achieved.

### Prerequisites

You will need [Python 3](https://www.python.org/) for using the provided files.
Also you will need to install all the dependencies listed below.

```bash
pip install -r /path/to/requirements.txt

or

pip install opencv-python==3.4.3.18
pip install scipy==1.1.0
pip install numpy==1.15.2
pip install pymodbus==2.1.0
pip install vpython==7.4.7
pip install matplotlib==3.0.0
pip install pygame==1.9.4
```

### Installing and usage

Clone or download project as zip in any directory.
Find correct HSV settings for ball detection with morphological_transform file.
Adjust the sliders until the ball is the only thing white. 
Set the new values in the video_processing file and finish with running main.py

### Example
Each class can be executed on their own for testing purposes.

For single parts:
```bash
python joystick.py
python modbus_communication.py
python video_processing.py
python visualization.py
```
For utility parts:
```bash
python graphs.py
python inverse_kinematics.py
python morphological_transformation.py
```

For whole project:
```bash
python main.py
```
or
```bash
python main.py
python visualization.py
```
if you want to run an 3D visualization model simultaneously.

![Output](https://github.com/magnusoy/Balancing-Platform/blob/master/resources/img/readme1.JPG)


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

[PyGame](https://www.pygame.org/news)

