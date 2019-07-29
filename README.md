# Research Package Manager

This package is a small package manager to help more easily setup
and manage your research projects.

Right now, this is not even alpha version, but it is able to setup a new research
package in no time.

To get started, make sure you have python 3.x installed along with the appropriate pip version.
Clone this repo, and run `pip install .` to install this CLI.
To initialize a new project, run `repm --init <your-project-name (optional)>`.

Ex. (if you're a fan of PyCharm):
```bash
cd ~/PycharmProjects/
repm --init repm_tutorial
ls -la ./repm_tutorial
# Or open the workspace with whichever IDE to see the workspace structure
```

To download a dataset, run `repm download -a <your-dataset-name>`.

Ex. for downloading a dataset (continuing from the example above):
```bash
cd ~/PycharmProjects/repm_tutorial
repm download -a repm_tutorial_dataset
# Downloads into the data/ folder within the project.
```

New feature: authorization.
Downloading datasets can't work if you can't upload anything.
Authorization is meant to support uploading your own datasets.

To create an account, run `repm --signup`.
To login, run `repm --login`.
To logout, run `repm --logout`.

That's about it for now, but more will be coming soon.

N.B. If you're wondering why the shorthand looks so weird (`repm` instead of `rpm`),
it's because `rpm` has already been taken.
