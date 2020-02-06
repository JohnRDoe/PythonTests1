FROM openjdk:slim-buster

ARG VERSION=4.0.1
ARG user=jenkins
ARG group=jenkins
ARG uid=1000
ARG gid=1000

RUN addgroup -g ${gid} ${group}
RUN adduser -h /home/${user} -u ${uid} -G ${group} -D ${user}
LABEL Description="This is a base image, which provides the Jenkins agent executable (slave.jar)" Vendor="Jenkins project" Version="${VERSION}"

ARG AGENT_WORKDIR=/home/${user}/agent

RUN apk add --update --no-cache curl bash git git-lfs openssh-client openssl procps \
  && curl --create-dirs -fsSLo /usr/share/jenkins/agent.jar https://repo.jenkins-ci.org/public/org/jenkins-ci/main/remoting/${VERSION}/remoting-${VERSION}.jar \
  && chmod 755 /usr/share/jenkins \
  && chmod 644 /usr/share/jenkins/agent.jar \
  && ln -sf /usr/share/jenkins/agent.jar /usr/share/jenkins/slave.jar \
  && apk del curl
USER ${user}
ENV AGENT_WORKDIR=${AGENT_WORKDIR}
RUN mkdir /home/${user}/.jenkins && mkdir -p ${AGENT_WORKDIR}

VOLUME /home/${user}/.jenkins
VOLUME ${AGENT_WORKDIR}
WORKDIR /home/${user}

USER root
COPY jenkins-agent /usr/local/bin/jenkins-agent
RUN chmod +x /usr/local/bin/jenkins-agent &&\
    ln -s /usr/local/bin/jenkins-agent /usr/local/bin/jenkins-slave
USER ${user}

STOPSIGNAL SIGKILL
ENV MIRROR https://www-eu.apache.org/dist/jmeter/binaries
ENV JMETER_VERSION 5.2.1
ENV JMETER_HOME /opt/apache-jmeter-${JMETER_VERSION}
ENV JMETER_BIN ${JMETER_HOME}/bin
ENV ALPN_VERSION 8.1.13.v20181017
ENV PATH ${JMETER_BIN}:$PATH
COPY entrypoint.sh /usr/local/bin/
RUN chmod +x /usr/local/bin/entrypoint.sh \
 && apk add --no-cache \
    curl \
    fontconfig \
    net-tools \
    shadow \
    su-exec \
    tcpdump  \
    ttf-dejavu \
 && cd /tmp/ \
 && curl --location --silent --show-error --output apache-jmeter-${JMETER_VERSION}.tgz ${MIRROR}/apache-jmeter-${JMETER_VERSION}.tgz \
 && curl --location --silent --show-error --output apache-jmeter-${JMETER_VERSION}.tgz.sha512 ${MIRROR}/apache-jmeter-${JMETER_VERSION}.tgz.sha512 \
 && sha512sum -c apache-jmeter-${JMETER_VERSION}.tgz.sha512 \
 && mkdir -p /opt/ \
 && tar x -z -f apache-jmeter-${JMETER_VERSION}.tgz -C /opt \
 && rm -R -f apache* \
 && sed -i '/RUN_IN_DOCKER/s/^# //g' ${JMETER_BIN}/jmeter \
 && sed -i '/PrintGCDetails/s/^# /: "${/g' ${JMETER_BIN}/jmeter && sed -i '/PrintGCDetails/s/$/}"/g' ${JMETER_BIN}/jmeter \
 && chmod +x ${JMETER_HOME}/bin/*.sh \
 && jmeter --version \
 && curl --location --silent --show-error --output /opt/alpn-boot-${ALPN_VERSION}.jar https://repo1.maven.org/maven2/org/mortbay/jetty/alpn/alpn-boot/${ALPN_VERSION}/alpn-boot-${ALPN_VERSION}.jar \
 && rm -fr /tmp/*
# Required for HTTP2 plugins
ENV JVM_ARGS -Xbootclasspath/p:/opt/alpn-boot-${ALPN_VERSION}.jar
WORKDIR /jmeter
# ENTRYPOINT ["/usr/local/bin/entrypoint.sh"]
ENTRYPOINT ["jenkins-agent"]