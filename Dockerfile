FROM centos
RUN yum -y update
RUN yum install -y vim
RUN echo "hello docker"