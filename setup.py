import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="open3d_ros2_helper",
    version="0.0.0.1",
    author="Farooq Olanrewaju",
    author_email="olanrewajufarooq@yahoo.com",
    description="A helper tool for jointly using open3d and ROS",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/olanrewajufarooq/open3d-ros2-helper",
    packages=setuptools.find_packages(),
    license="MIT",
    classifiers=[
        "Programming Language :: Python :: 3.10",
        "Operating System :: OS Independent",
    ],
)
