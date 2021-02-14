#!/usr/bin/ruby

require 'base64'

File.open(ARGV[0], 'rb') { |f| puts Base64.encode64(f.read) }
