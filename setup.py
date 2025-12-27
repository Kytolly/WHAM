import os
from setuptools import setup, find_packages
from setuptools.command.install import install
import subprocess

# 读取 requirements.txt
def parse_requirements(filename):
    with open(filename, 'r') as f:
        return [line.strip() for line in f if line.strip() and not line.startswith('#')]

# 定义安装后的钩子（可选：提示用户安装 DPVO）
class PostInstallCommand(install):
    def run(self):
        install.run(self)
        print("----------------------------------------------------------------")
        print(" NOTICE: WHAM has been installed.")
        print(" Please ensure DPVO is installed separately via:")
        print(" pip install git+https://github.com/Kytolly/DPVO.git")
        print("----------------------------------------------------------------")

setup(
    name='wham',
    version='0.1.0',
    description='WHAM: World-grounded Humans with Accurate Motion',
    author='Kytolly',
    
    # 自动发现 wham 包和 lib 包
    packages=find_packages(include=['wham', 'wham.*', 'lib', 'lib.*']),
    
    # 关键：依赖管理
    install_requires=[
        'numpy<1.24',  # 锁定关键依赖
        'chumpy',
        'smplx',
        'yacs',
        'loguru',
        # 'mmcv-full==1.7.2', # MMCV 建议用户手动安装，避免编译卡死
    ],
    
    # 指定包的数据文件（如果有）
    include_package_data=True,
    
    # 钩子类
    cmdclass={
        'install': PostInstallCommand,
    },
)