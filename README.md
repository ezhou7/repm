Research Package Manager
=========

This package is a small package manager to help more easily setup
and manage your research projects.

Right now, this is not even alpha version, but it is able to setup a new research
package in no time.

To get started, make sure you have Python 3.7 installed.

N.B. If you're wondering why the shorthand looks so weird (`repm` instead of `rpm`),
it's because `rpm` has already been taken.

## Installation
Clone this repo, and run `python ./bin/install` to install this CLI.

## New feature: Upload
To upload a dataset, run `repm upload -a <your-dataset-name>`.

Ex. for uploading a dataset:
```bash
cd ~/PycharmProjects/repm_tutorial
repm upload -a repm_tutorial_dataset
```

## Project Creation
To initialize a new project, run `repm --init <your-project-name (optional)>`.

Ex. (if you're a fan of PyCharm):
```bash
# Option 1
cd ~/PycharmProjects/
repm --init repm_tutorial

# Option 2
cd ~/PycharmProjects/
mkdir repm_tutorial
cd repm_tutorial
repm --init
```

## Download
To download a dataset, run `repm download -a <your-dataset-name>`.

Ex. for downloading a dataset:
```bash
cd ~/PycharmProjects/repm_tutorial
repm download -a repm_tutorial_dataset
# Downloads into the data/ folder within the project.
```

## Authorization
Downloading datasets can't work if you can't upload anything.
Authorization is meant to support uploading your own datasets.

To create an account, run `repm --signup`.

To login, run `repm --login`.

To logout, run `repm --logout`.

## Next up
- Dataset permissions
- Dataset listing
