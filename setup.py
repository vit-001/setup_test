from cx_Freeze import setup, Executable

# Dependencies are automatically detected, but it might need
# fine tuning.
# icon_file = 'resource/icon.png'


buildOptions = dict(
    packages = [],
    excludes = [],
    includes = ["atexit"],
    include_files = ['resource/icon.png'],
    # icon = icon_file
)

import sys
base = 'Win32GUI' if sys.platform=='win32' else None

executables = [
    Executable('s_test.py', base=base)
]

setup(name='s_test',
      version = '1.0',
      description = 'setup test',
      options = dict(build_exe = buildOptions),
      executables = executables)
