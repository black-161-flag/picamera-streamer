from setuptools import setup

setup(
    name='picamera-streamer',
    version='0.0.2',
    packages=['picamera-streamer'],
    scripts=['bin/picamera-streamer'],
    description='simple mpg streamer for picamera',
    long_description=open('README.md').read(),
    install_requires=["picamera", "simplejpeg", 'numpy'],
    package_dir={'picamera-streamer': 'bin'},

)
