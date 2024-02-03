# -*- coding: utf-8 -*-

name = 'gflows'

version = '7.2.6'

description = 'G|Flows, or Greek Flows, provides 15-minute updates for the SPX, NDX and RUT indexes every Monday-Friday from 9:00am-4:30pm ET'

tools = [
]

requires = [
    'pandas-2.1.4',
    'yahooquery-2.3.7',
    'dash-2.14.2',
    'Flask_Caching-2.1.0',
    'cachetools-5.3.2',
    'scipy-1.11.4',
    'dash_bootstrap_components-1.5.0',
    'gunicorn-21.2.0',
    'APScheduler-3.10.4',
    'requests-2.31.0',
    'pandas_market_calendars-4.3.2',
    'dateparser-1.2.0',
    'orjson-3.9.10',
    'python_dotenv-1.0.0',   
]

variants = [['platform-linux', 'arch-x86_64', 'python-3.9', 'importlib_metadata-4.8+']]

# Build command that copies all files in the current directory into the package.
build_command = 'python {root}/rez_build.py'

def commands():
    env.PYTHONPATH.append('{root}/python')
    env.PATH.append('{root}/bin')

timestamp = 1697407444

hashed_variants = True

from_pip = True

pip_name = 'Sphinx (7.2.6)'

is_pure_python = True

format_version = 2
