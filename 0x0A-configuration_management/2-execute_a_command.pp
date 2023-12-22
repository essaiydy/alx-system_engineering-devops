exec { 'killmenow':
  command  => 'pkill -f "killmenow"',
  provider => 'shell',
  onlyif   => 'pgrep -f "killmenow"',
}
