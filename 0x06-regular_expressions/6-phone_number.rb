#!/usr/bin/env ruby
x = ARGV
puts x[0].scan(/^\d{10}$/).join
