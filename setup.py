import setuptools

setuptools.setup(
    name="fuel_http_helper",
    version="1.0.0",
    author="bi-jvo",
    author_email="jvo@bi-web.de",
    description="Automatically uploads files to a Trilith FuelHttpServer",
    packages=setuptools.find_packages(),
    include_package_data=True,
    install_requires=["requests"],
    zip_safe=True,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ]
)
