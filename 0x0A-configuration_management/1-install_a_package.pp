#Installing a package (Puppet Lint)
package { 'puppet-lint':
  ensure   => '2.1.1',
  provider => 'gem',
}
