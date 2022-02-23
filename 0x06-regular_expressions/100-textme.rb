#!/usr/bin/env ruby
regexs = /from:(.*?)\]\s\[to:(.*?)\]\s\[flags:(.*?)\]/
x = ARGV
# Print the match result
puts x[0].scan(regexs).join(", ")
