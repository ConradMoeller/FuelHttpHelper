import setuptools

with open('requirements.txt') as f:
    required = f.read().splitlines()

setuptools.setup(
    name="fuel_http_helper",
    version="1.0.2",
    author="bi-jvo",
    author_email="jvo@bi-web.de",
    description="Automatically uploads files to a Trilith FuelHttpServer",
    packages=setuptools.find_packages(),
    include_package_data=True,
    install_requires=required,
    zip_safe=True,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ]
)
