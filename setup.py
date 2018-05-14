from setuptools import setup

def readme():
    with open('README.md') as f:
        return f.read()

with open('requirements.txt') as f:
    dependency_links = []
    install_requires = []
    for line in f.read().splitlines():
        if 'ssh://' in line:
            # make a pip line into setup line
            #pip line   -e git+ssh://git@gitlab.sparefoot.com:10648/analytics/laketrail.git#egg=laketrail
            #setup line git+ssh://git@gitlab.sparefoot.com:10648/analytics/laketrail.git#egg=laketrail-0
            dependency_links.append(line.replace('-e ', '') + '-0')
            install_requires.append(line.split('egg=')[1])
        else:
            install_requires.append(line)


setup(
    name='fake_dep_module',
    py_modules=[''],
    version='0.0.2',
    description='helps test',
    url='ssh://git@gitlab.sparefoot.com:10648/analytics/helpers.git',
    author='Matt Land',
    author_email='mland@sparefoot.com',
    install_requires=install_requires,
    test_suite='nose.collector',
    tests_require=['nose'],
    dependency_links=dependency_links
)
