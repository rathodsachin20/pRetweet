#!/usr/bin/env ruby

def tojson(in_fname, out_fname)
	out_path = "./out/"
	fr = File.open(in_fname)
	fw = File.open(out_path + out_fname, 'w')

	fw.puts("[")
	count = fr.readlines.size
	puts count
	count -= 1
	fr.close
	fr = File.open(in_fname)

	count.times do
		line = fr.readline + ","
		fw.puts(line)
	end
	line = fr.readline
	fw.puts(line)

	fw.puts("]")

	fr.close
	fw.close
end

dir_path = "./*/"
dirs = Dir.glob(dir_path)
dirs.each do |d|
	dirname = File.basename(d)
        if dirname == "out"
            next
        end
	files = Dir.glob(d+"*.json")
	files.each do |f|
		out_fname = dirname + File.basename(f)
		puts "Formatting " + File.basename(f) + " to "+ out_fname
		tojson(f,out_fname)
	end
end
