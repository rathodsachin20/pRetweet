#!/usr/bin/env ruby
fr = File.open('00.json')
fw = File.open('final.json', 'w')

fw.puts("[")
count = fr.readlines.size
puts count
count -= 1
fr.close
fr = File.open('00.json')

count.times do
	line = fr.readline + ","
	fw.puts(line)
end
line = fr.readline
fw.puts(line)
#IO.foreach('00.json') do |line|
#	fw.puts(line + ",")
#end

fw.puts("]")
fr.close
fw.close