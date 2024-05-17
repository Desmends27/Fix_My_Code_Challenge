# Sort integer arguments (ascending)

result = []
ARGV.each do |arg|
  # Skip if not integer
  next if arg !~ /^-?[0-9]+$/

  # Convert to integer
  i_arg = arg.to_i

  # Insert result at the right position
  i = 0
  l = result.size
  while i < l && result[i] < i_arg
    i += 1
  end
  result.insert(i, i_arg)
end

puts result
