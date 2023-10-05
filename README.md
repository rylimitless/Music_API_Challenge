# Music_API_Challenge

Ignoring ffi-1.16.3 because its extensions are not built. Try: gem pristine ffi --version 1.16.3
/Users/stonetech/.gem/ruby/3.2.2/gems/activesupport-7.1.0/lib/active_support/core_ext/array/conversions.rb:108:in `<class:Array>': undefined method `deprecator' for ActiveSupport:Module (NoMethodError)

  deprecate to_default_s: :to_s, deprecator: ActiveSupport.deprecator
                                                          ^^^^^^^^^^^
Did you mean?  deprecate_constant
	from /Users/stonetech/.gem/ruby/3.2.2/gems/activesupport-7.1.0/lib/active_support/core_ext/array/conversions.rb:8:in `<top (required)>'
	from <internal:/usr/local/Cellar/ruby/3.2.2_1/lib/ruby/3.2.0/rubygems/core_ext/kernel_require.rb>:85:in `require'
	from <internal:/usr/local/Cellar/ruby/3.2.2_1/lib/ruby/3.2.0/rubygems/core_ext/kernel_require.rb>:85:in `require'
	from /usr/local/Cellar/cocoapods/1.13.0/libexec/gems/cocoapods-1.13.0/lib/cocoapods.rb:9:in `<top (required)>'
	from <internal:/usr/local/Cellar/ruby/3.2.2_1/lib/ruby/3.2.0/rubygems/core_ext/kernel_require.rb>:85:in `require'
	from <internal:/usr/local/Cellar/ruby/3.2.2_1/lib/ruby/3.2.0/rubygems/core_ext/kernel_require.rb>:85:in `require'
	from /usr/local/Cellar/cocoapods/1.13.0/libexec/gems/cocoapods-1.13.0/bin/pod:36:in `<top (required)>'
	from /usr/local/Cellar/cocoapods/1.13.0/libexec/bin/pod:25:in `load'
	from /usr/local/Cellar/cocoapods/1.13.0/libexec/bin/pod:25:in `<main>'

## Requirements
python:3.7+
fastapi:latest
sqlite:latest
uvicorn:latest

Runs on http:localhost:8000
documentation http:localhost:8000/docs
