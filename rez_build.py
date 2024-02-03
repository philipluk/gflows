import os
import shutil

if __name__ == '__main__':
    # Copy all files from REZ_BUILD_SOURCE_PATH to REZ_BUILD_INSTALL_PATH
    shutil.rmtree(os.environ['REZ_BUILD_INSTALL_PATH'], ignore_errors=True)
    shutil.copytree(os.environ['REZ_BUILD_SOURCE_PATH'], os.environ['REZ_BUILD_INSTALL_PATH'], dirs_exist_ok=True)
