FROM dalloriam/python-dlib
RUN echo ' deb https://mirrors.tuna.tsinghua.edu.cn/debian/ jessie main contrib non-free \n \
deb https://mirrors.tuna.tsinghua.edu.cn/debian/ jessie-updates main contrib non-free \n \
deb https://mirrors.tuna.tsinghua.edu.cn/debian/ jessie-backports main contrib non-free \n \
deb https://mirrors.tuna.tsinghua.edu.cn/debian-security jessie/updates main contrib non-free'>/etc/apt/sources.list
RUN apt update  || true
#RUN apt install  gfortran ca-certificates libpng-dev libfreetype6-dev
COPY xlw_project /xlw_project
WORKDIR xlw_project

RUN pip3 install -r /xlw_project/m_flask/requirements.txt -i https://mirrors.tuna.tsinghua.edu.cn/pypi/web/simple/
RUN chmod 777 /xlw_project/start.sh
EXPOSE 80
ENTRYPOINT ["bash"]
