from setuptools import setup, find_packages

setup(
    name="weather_pipeline",  
    version="0.1.0",  
    description="A weather data processing pipeline using OpenWeather API",  
    long_description=open('README.md').read(),  
    long_description_content_type="text/markdown",  
    url="https://github.com/pablomaceda3/weather_pipeline",  
    author="Pablo Maceda",  
    author_email="pablomaceda3@gmail.com",  
    license="MIT",  
    packages=find_packages(),  
    install_requires=[  
        "requests>=2.0.0",  
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",  
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',  
    entry_points={  
        'console_scripts': [
            'weather-pipeline=weather_pipeline.run_pipeline:main',  
        ],
    },
)
