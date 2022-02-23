#!/usr/bin/env ruby

str = [
	ARGV[0].scan(/\[(from:.*?)\]/).join().split(":")[1],
	ARGV[0].scan(/\[(to:.*?)\]/).join().split(":")[1],
	ARGV[0].scan(/\[(flags:.*?)\]/).join().split(":",2)[1]
]

puts str.join(",")
