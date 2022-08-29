import setuptools

import simple_sendgrid

setuptools.setup(
    name='simple-sendgrid',
    version=simple_sendgrid.__version__,
    description='SendGrid simple async client based on httpx',
    packages=['simple-sendgrid'],
    install_requires=[
        "httpx>=0.21",
    ],
    author_email='saltytimofey@gmail.com',
)
