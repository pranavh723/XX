from setuptools import setup, find_packages

setup(
    name="t1x2y1",
    version="1.0.0",
    packages=find_packages(),
    install_requires=[
        "python-telegram-bot==20.3",
        "python-dotenv",
        "sqlalchemy",
        "psycopg2-binary",
        "python-dateutil",
        "requests",
        "ujson",
        "flask",
        "flask-cors",
        "flask-sqlalchemy"
    ],
    entry_points={
        'console_scripts': [
            't1x2y1=t1x2y1.main:main',
        ],
    },
)