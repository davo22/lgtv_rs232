from setuptools import find_packages, setup
setup(
    name='lgtv_rs232',
    packages=find_packages(include=['lgtv_rs232']),
    version='0.1.0',
    description='LG TV RS-232 client.',
    author='Dawid Rashid',
    license='MIT',
    install_requires=['pyserial'],
    include_package_data=True,
)
