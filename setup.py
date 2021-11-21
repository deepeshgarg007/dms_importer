from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in dms_importer/__init__.py
from dms_importer import __version__ as version

setup(
	name="dms_importer",
	version=version,
	description="Import Invoices from Dealer Management System",
	author="Deepesh",
	author_email="test@example.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
