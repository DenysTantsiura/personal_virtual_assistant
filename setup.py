from importlib.metadata import entry_points
from setuptools import setup, find_namespace_packages

setup(name='personal_virtual_assistant',
      version='2.2.0.2',
      description='Personal Virtual Assistant',
      url='https://github.com/DenysTantsiura/personal-virtual-assistant.git',
      author='Tantsiura Denys',
      author_email='tdv@tesis.kiev.ua',
      license='MIT',
      packages=find_namespace_packages(),
      include_package_data=True,
      # install_requires=['logging', 'sys', 'shutil'],
      ## install_requires=['type_extensions', 'norma'],
      entry_points={'console_scripts': ['pva = personal_virtual_assistant.start_pva:main']})

"""
The package is installed in the system by the command:
 pip install -e . 
 (or :
python setup.py install
, administrator rights are required!)
"""
