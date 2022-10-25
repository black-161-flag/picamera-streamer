from setuptools import setup

setup(
    name='picamera-streamer',
    version='0.0.1',
    packages=['picamera-streamer'],
    scripts=['bin/picamera-streamer'],
    description='simple mpg streamer for picamera',
    long_description=open('README.md').read(),
    install_requires=["picamera", "simplejpeg", 'numpy <= 1.23.4'],
    package_dir={'picamera-streamer': 'bin'},

)
