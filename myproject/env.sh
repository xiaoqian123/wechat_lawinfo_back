PROJ_DIR=`pwd`
VENV=${PROJ_DIR}/.env
PROJ_NAME=wxdraco

if [ ! -e ${VENV} ];then
    virtualenv --never-download --prompt "(${PROJ_NAME})" ${VENV} -p $(type -p python2.7)
fi

source ${VENV}/bin/activate 

export PYTHONPATH=${PROJ_DIR}:${PROJ_DIR}/modules

export PROJ_NAME
export PROJ_DIR

export FLASKR_SETTINGS=/tmp/myproject/myapp/setting.py

