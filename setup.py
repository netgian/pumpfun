from setuptools import setup, find_packages


setup(
    name='pumpfun',
    version='0.0.1',
    packages=find_packages(),
    install_requires=open('requirements.txt').read().splitlines(),
    license='MIT',
    description='pump.fun frontend API Wrapper for Python',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='Gian Glen',
    author_email='gianlopez.cv@gmail.com',
    project_urls={
        "Source": "https://github.com/netgian/pumpfun",
        "Documentation": "https://frontend-api.pump.fun/api"
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
