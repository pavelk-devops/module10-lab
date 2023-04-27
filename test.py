import testinfra
def test_os_release(host):
    assert host.file("/etc/os-release").contains("alpine")

def test_nginx(host):
  nginx = host.package("nginx")
  assert nginx.is_installed
  assert nginx.version
