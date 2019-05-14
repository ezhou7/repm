# Research Package Manager

This package is a small package manager to help more easily setup
and manage your research projects.

Right now, this is not even alpha version, but it is able to setup a new research
package in no time.

To get started, run `repm <your personal workspace path> <your package name>`.

Ex. (if you're a fan of PyCharm):
```bash
cd ~/PycharmProjects/
mkdir repm_tutorial
cd repm_tutorial
repm --init
# or you can write...
repm --init ~/PycharmProjects/repm_tutorial
```

That's about it for now, but more will be coming soon.

N.B. If you're wondering why the shorthand looks so weird (`repm` instead of `rpm`),
it's because `rpm` has already been taken.
