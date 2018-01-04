PYTHON=`which python`
NAME=`python setup.py --name`
VERSION=`python setup.py --version`
SDIST=dist/$(NAME)-$(VERSION).tar.gz
VENV=/tmp/venv

install:
	$(PYTHON) setup.py install

init:
	pip install -r requirements.txt --use-mirrors
	
clean:
	$(PYTHON) setup.py clean
	rm -rf build/ MANIFEST dist build caffe_cnn_train.egg-info deb_dist
	find . -name '*.pyc' -delete

