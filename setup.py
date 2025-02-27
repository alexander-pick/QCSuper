#!/usr/bin/python3
#-*- encoding: Utf-8 -*-

from setuptools import setup

setup(name = 'qcsuper',
    version = '2.0.0',
    description = ' QCSuper is a tool communicating with Qualcomm-based phones and modems, allowing to capture raw 2G/3G/4G radio frames, among other things',
    author = 'P1 Security - Marin Moulinier',
    author_email = '',
    entry_points = {
        'console_scripts': [
            'qcsuper = qcsuper.__main__'
        ]
    },
    url = 'https://github.com/P1sec/QCSuper',
    requires = ['pyserial(>=3.5)', 'pyusb(>=1.2.1)', 'crcmod(>=1.7)', 'pycrate(>=0.7.0)'],
    install_requires = [],
    packages = [
        'qcsuper',
        'qcsuper.inputs',
        'qcsuper.protocol',
        'qcsuper.modules',
        'qcsuper.modules.efs_shell_commands'
    ],
    package_dir = {
        'qcsuper': 'src'
    }
)
