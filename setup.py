import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="open3d_ros2_helper",
    version="0.1.0.0",
    author="Farooq Olanrewaju",
    author_email="olanrewajufarooq@yahoo.com",
    description="A helper tool for jointly using open3d and ROS2",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/olanrewajufarooq/open3d-ros2-helper",
    packages=setuptools.find_packages(),
    license="MIT",
    install_requires=[
        "open3d>=0.17.0",
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
