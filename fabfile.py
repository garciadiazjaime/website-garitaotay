from fabric.api import local

def deploy():
  local('docker build -t garciadiazjaime/website-garitaotay .')
  local('docker push garciadiazjaime/website-garitaotay')
  local('echo "docker pull garciadiazjaime/website-garitaotay"')
