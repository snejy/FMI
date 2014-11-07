describe 'format_string' do
  it 'works for untrimmed strings' do
    expect(format_string('  do YouR   homeWork   NoW    ', 10)).to eq 'DO YOUR HOMEWORK NOW'
  end

  it 'works for placing and padding' do
    expect(format_string('run  FOrest   run!!', 20)).to eq '  RUN FOREST RUN!!  '
  end

  it 'works for placing and padding with uneven width' do
    expect(format_string('run  FOrest   run!!', 21)).to eq '  RUN FOREST RUN!!   '
  end

  it 'works for empty string' do
    expect(format_string(' ', 21)).to eq '                     '
  end

  it 'works for one letter string' do
    expect(format_string(' r', 22)).to eq '          R           '
  end  
end
