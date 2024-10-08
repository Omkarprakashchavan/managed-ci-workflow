#!/usr/bin/env bash

# chdir to the directory in which this script resides
cd $(dirname $0)
# the above allows the user to invoke this script from any directory

sig_int() {
    echo 'Interrupted... Good bye!'
    # restore original file
    mv /tmp/conf.py.$$ conf.py
    exit 0
}
trap sig_int SIGINT

# backup
cp -p conf.py /tmp/conf.py.$$

# if the dependencies in the requirements.txt have already been installed
# on your host/env, and you don't want to use Docker, then set the
# env var NO_DOCKER to a non-empty value to skip building the Docker image.
if [ -z "$NO_DOCKER" ]; then
    # add --no-cache to disable docker cache and pull all packages from scratch
    # make html
    #
    docker build -f Dockerfile -t design-content ..
fi

pushd ..  # logic in the workflow expects current dir to be one dir up, 
          # so must go one level up
# the logic in the workflow file is used to get the highest version
# number, which will be updated in the conf.py file
wf=.github/workflows/gh-pages.yaml
bash <(awk '/#-# start/,/#-# end/' $wf)
popd
sleep 5

# clean up the last run
rm -rf _build/html/*
mkdir -p _build

cmd="sphinx-multiversion .. _build/html/versions -c . -D version="
if [ -z "$NO_DOCKER" ]; then
    # enter container terminal
    docker run -v `pwd`/_build:/design/docs-creation/_build \
               -v `pwd`/_static:/design/docs-creation/_static \
               design-content \
               bash -c "cd docs-creation; $cmd"
else
    $cmd
fi

# copy file generated by sphinx-multiversion
cp -p _static/index.html _build/html

# point out where we dumped the output
echo ''
echo Site built in `pwd`/_build

# restore original file
mv /tmp/conf.py.$$ conf.py

