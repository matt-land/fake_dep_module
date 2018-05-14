from setuptools import setup

# with open('requirements.txt') as f:
#     dependency_links = []
#     install_requires = []
#     for line in f.read().splitlines():
#         if 'ssh://' in line:
#             # make a pip line into setup line
#             dependency_links.append(line.replace('-e ', '') + '-0')
#             install_requires.append(line.split('egg=')[1])
#         else:
#             install_requires.append(line)

# pip line
# -e git@github.com:matt-land/fake_subdep_module.git#egg=fakesubdepmodule
# setup dependency_links list
# git@github.com:matt-land/fake_subdep_module.git#egg=fakesubdepmodule-0
# setup install_requires line
# fakesubdepmodule-0

setup(
    name='fakedepmodule',
    py_modules=[''],
    version='0.0.0',
    description='helps test',
    url='git@github.com:matt-land/fake_dep_module.git',
    author='No One',
    author_email='noone@nowhere.com',
    install_requires=[
        'fakesubdepmodule-0'
    ],
    dependency_links=[
        'git@github.com:matt-land/fake_subdep_module.git#egg=fakesubdepmodule-0'
    ]
)
