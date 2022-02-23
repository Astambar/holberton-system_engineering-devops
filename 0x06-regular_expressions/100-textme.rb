#!/usr/bin/env ruby
regexs = /from:(.*?)\]\s\[to:(.*?)\]\s\[flags:(.*?)\]/
x = ARGV
# Print the match result
puts str.scan(regexs).join(",")
