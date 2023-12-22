#install flasck

$python_version = '3.8.10'
$pip_package = 'python3-pip'

package { "python${python_version}":
  ensure => $python_version,
}

package { $pip_package:
  ensure => present,
}

package { ['flask==2.1.0', 'werkzeug==2.1.1']:
  ensure   => installed,
  provider => 'pip',
  require  => Package[$pip_package],
}
