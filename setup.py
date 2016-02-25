from setuptools import setup

import re
import subprocess

def git_version():
    '''Versions from git labels according to PEP-0440'''
    label = subprocess.check_output(["git", "describe", "--tags"]).rstrip()
    r = '^((?:v\d+(?:\.\d)+))(a|b|rc|dev)?(?:-(\d+)-g(.+))?$'
    try:
        (m,t,n,h) = re.match(r,label).groups()

        if t and not n:
            n = '0'

        if n:
            if not t:
                suffix = '.post%s+%s' % (n,h)
            elif t == 'dev':
                suffix = '.dev%s+%s' % (n,h)
            else:
                suffix = '%s%s+%s' % (t,n,h)
                
            return m + suffix
        else:
            return m 
    
    except :
        raise Exception("Invalid version: %s, please enjoy regexp: %s" % (label, r))

setup(
    name='ptest',
    packages=['ptest'],
    url='http://www.equa.se',
    author='Kenny Johansson',
    author_email='kenny@equa.se',
    maintainer='Kenny Johansson',
    version = git_version(),
)

# Whee!

# Fixing stuff

# Branched


# Dev
