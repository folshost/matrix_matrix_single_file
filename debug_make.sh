#!/bin/bash
SCRIPTPATH=$( cd $(dirname $0) ; pwd -P )
BUILDPATH=$SCRIPTPATH/debug
rm -rf $BUILDPATH

mkdir $BUILDPATH

cd $BUILDPATH

cmake -DCMAKE_BUILD_TYPE=Debug \
      -DHPX_DIR=/home/mreeser/hpx/hpx_debug_build/lib/cmake/HPX \
      -DCMAKE_INSTALL_PREFIX=$SCRIPTPATH/source \
      $SCRIPTPATH/source

cp $SCRIPTPATH/hpx_sbatch.sbatch $BUILDPATH

make $1
