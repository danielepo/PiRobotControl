FROM python
LABEL maintainer="dnl.pozzobon@gmail.com"

RUN cd ~
RUN mkdir -p projects/quick_tutorial
RUN cd projects/quick_tutorial

RUN export VENV=~/projects/quick_tutorial/env
RUN python3 -m venv ~/projects/quick_tutorial/env
RUN cd ~/projects/quick_tutorial/env/bin
RUN pip install --upgrade pip setuptools
RUN pip install "pyramid==1.10.4" waitress

RUN pip install pyramid_chameleon

RUN cd projects/quick_tutorial
COPY . /src
WORKDIR /src

EXPOSE 6543

ENTRYPOINT [ "python","./app.py" ]