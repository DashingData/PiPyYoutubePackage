import os
from pathlib import Path
import logging

# Configure logging to show info messages.
logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")

# Prompt the user for the project name.
project_name = input("Enter project name: ").strip()

# Define the base directory for the project.
project_dir = Path(project_name)
if not project_dir.exists():
    project_dir.mkdir()
    logging.info(f"Created project directory: {project_dir}")
else:
    logging.info(f"Project directory '{project_dir}' already exists. Using existing directory.")

# Prepare a mapping of top-level filenames to placeholder content.
files_to_create = {
    "LICENSE": "Your license text goes here.\n",
    "pyproject.toml": (
        "[build-system]\n"
        "requires = [\"setuptools\", \"wheel\"]\n"
        "build-backend = \"setuptools.build_meta\"\n\n"
        "[project]\n"
        f"name = \"{project_name}\"\n"
        "version = \"0.0.1\"\n"
        "description = \"\"  # TODO: Add project description\n"
        "authors = []        # TODO: Add author info\n"
    ),
    "setup.py": (
        "import setuptools\n\n"
        "# Minimal setup.py for compatibility. Configuration is in setup.cfg.\n"
        "setuptools.setup()\n"
    ),
    "setup.cfg": (
        "[metadata]\n"
        f"name = {project_name}\n"
        "version = 0.0.1\n"
        "description = TODO: Add description\n"
        "license = TODO: Choose a license\n\n"
        "[options]\n"
        "packages = find:\n"
        "package_dir = \n"
        "    = src\n"
        "# Any other options (install_requires, etc.) can be added here.\n"
    ),
    "README.md": "# README\n\nTODO: Write project overview and usage.\n",
    "requirements.txt": "# Project requirements (install dependencies) go here.\n",
    "requirements_dev.txt": "# Development requirements (testing, linting, etc.) go here.\n"
}

# Create top-level files with placeholder content if they don't exist.
for filename, content in files_to_create.items():
    file_path = project_dir / filename
    if not file_path.exists():
        try:
            file_path.write_text(content)
            logging.info(f"Created file: {file_path}")
        except Exception as e:
            logging.error(f"Could not create file {file_path}: {e}")
    else:
        logging.info(f"File {file_path} already exists, skipping.")

# Define directories to create: "src/<project_name>/" and "tests/".
src_dir = project_dir / "src" / project_name
tests_dir = project_dir / "tests"

for d in [src_dir, tests_dir]:
    if not d.exists():
        d.mkdir(parents=True)
        logging.info(f"Created directory: {d}")
    else:
        logging.info(f"Directory {d} already exists, skipping.")

# Define package module files to create inside src/<project_name>/.
package_files = ["__init__.py", "embed.py", "metadata.py"]
for fname in package_files:
    fpath = src_dir / fname
    if not fpath.exists():
        fpath.touch()  # create an empty file
        logging.info(f"Created file: {fpath}")
    else:
        logging.info(f"File {fpath} already exists, skipping.")

# Define test module files to create inside tests/.
test_files = ["__init__.py", "test_embed.py", "test_metadata.py"]
for fname in test_files:
    fpath = tests_dir / fname
    if not fpath.exists():
        fpath.touch()  # create an empty file
        logging.info(f"Created file: {fpath}")
    else:
        logging.info(f"File {fpath} already exists, skipping.")
