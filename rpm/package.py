import os
from pathlib import Path


class Setup:
    def __init__(self, package_name):
        self._package_name = package_name
        self._imports = [Import("setuptools", sub_imports=["setup", "find_packages"])]

    def __str__(self):
        resources_path = str(Path(__file__).resolve().parents[1].absolute())
        setup_template_path = os.path.abspath(resources_path + "/resources/setup_template.py")
        with open(setup_template_path, "r") as fin:
            setup_template = fin.read()
            return setup_template.format(self._package_name)


class Import:
    def __init__(self, package: str, sub_imports: list = (), shorthand: str = ""):
        self._package = package.strip()
        self._sub_imports = sub_imports
        self._shorthand = shorthand.strip()

    def __str__(self):
        if self._package != "" and self._package is not None:
            if len(self._sub_imports) == 0 and (self._shorthand is None or self._shorthand == ""):
                return "import {}".format(self._package)
            elif len(self._sub_imports) != 0 and (self._shorthand is None or self._shorthand == ""):
                return "from {} import {}".format(self._package, ", ".join(self._sub_imports))
            elif len(self._sub_imports) == 0 and (self._shorthand is not None or self._shorthand != ""):
                return "import {} as {}".format(self._package, self._shorthand)
            else:
                return "from {} import {}".format(self._package, ", ".join(self._sub_imports))
