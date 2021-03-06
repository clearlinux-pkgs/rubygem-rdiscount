#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : rubygem-rdiscount
Version  : 2.2.0.1
Release  : 9
URL      : https://rubygems.org/downloads/rdiscount-2.2.0.1.gem
Source0  : https://rubygems.org/downloads/rdiscount-2.2.0.1.gem
Summary  : No detailed summary available
Group    : Development/Tools
License  : BSD-3-Clause
Requires: rubygem-rdiscount-bin
Requires: rubygem-rdiscount-lib
BuildRequires : gmp-dev
BuildRequires : ruby
BuildRequires : rubygem-rdoc
BuildRequires : rubygem-test-unit
BuildRequires : xz-dev

%description
Discount Markdown Processor for Ruby
====================================
[![Build Status](https://travis-ci.org/davidfstr/rdiscount.svg?branch=master)](https://travis-ci.org/davidfstr/rdiscount)
[![Build status](https://ci.appveyor.com/api/projects/status/47i0qxrnvjbg724f/branch/master?svg=true)](https://ci.appveyor.com/project/DavidFoster/rdiscount/branch/master)

%package bin
Summary: bin components for the rubygem-rdiscount package.
Group: Binaries

%description bin
bin components for the rubygem-rdiscount package.


%package lib
Summary: lib components for the rubygem-rdiscount package.
Group: Libraries

%description lib
lib components for the rubygem-rdiscount package.


%prep
gem unpack %{SOURCE0}
%setup -q -D -T -n rdiscount-2.2.0.1
gem spec %{SOURCE0} -l --ruby > rubygem-rdiscount.gemspec

%build
gem build rubygem-rdiscount.gemspec

%install
%global gem_dir $(ruby -e'puts Gem.default_dir')
gem install -V \
--local \
--force \
--install-dir .%{gem_dir} \
--bindir .%{_bindir} \
rdiscount-2.2.0.1.gem

mkdir -p %{buildroot}%{gem_dir}
cp -pa .%{gem_dir}/* \
%{buildroot}%{gem_dir}

if [ -d .%{_bindir} ]; then
mkdir -p %{buildroot}%{_bindir}
cp -pa .%{_bindir}/* \
%{buildroot}%{_bindir}/
fi

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost
pushd %{buildroot}%{gem_dir}/gems/rdiscount-2.2.0.1
ruby -v -I.:lib:test test*/*_test.rb
popd


%files
%defattr(-,root,root,-)
/usr/lib64/ruby/gems/2.3.0/cache/rdiscount-2.2.0.1.gem
/usr/lib64/ruby/gems/2.3.0/extensions/x86_64-linux/2.3.0/rdiscount-2.2.0.1/gem.build_complete
/usr/lib64/ruby/gems/2.3.0/extensions/x86_64-linux/2.3.0/rdiscount-2.2.0.1/gem_make.out
/usr/lib64/ruby/gems/2.3.0/extensions/x86_64-linux/2.3.0/rdiscount-2.2.0.1/mkmf.log
/usr/lib64/ruby/gems/2.3.0/gems/rdiscount-2.2.0.1/BUILDING
/usr/lib64/ruby/gems/2.3.0/gems/rdiscount-2.2.0.1/COPYING
/usr/lib64/ruby/gems/2.3.0/gems/rdiscount-2.2.0.1/README.markdown
/usr/lib64/ruby/gems/2.3.0/gems/rdiscount-2.2.0.1/Rakefile
/usr/lib64/ruby/gems/2.3.0/gems/rdiscount-2.2.0.1/bin/rdiscount
/usr/lib64/ruby/gems/2.3.0/gems/rdiscount-2.2.0.1/ext/.RUBYARCHDIR.time
/usr/lib64/ruby/gems/2.3.0/gems/rdiscount-2.2.0.1/ext/Csio.c
/usr/lib64/ruby/gems/2.3.0/gems/rdiscount-2.2.0.1/ext/Csio.o
/usr/lib64/ruby/gems/2.3.0/gems/rdiscount-2.2.0.1/ext/Makefile
/usr/lib64/ruby/gems/2.3.0/gems/rdiscount-2.2.0.1/ext/VERSION
/usr/lib64/ruby/gems/2.3.0/gems/rdiscount-2.2.0.1/ext/amalloc.c
/usr/lib64/ruby/gems/2.3.0/gems/rdiscount-2.2.0.1/ext/amalloc.h
/usr/lib64/ruby/gems/2.3.0/gems/rdiscount-2.2.0.1/ext/amalloc.o
/usr/lib64/ruby/gems/2.3.0/gems/rdiscount-2.2.0.1/ext/basename.c
/usr/lib64/ruby/gems/2.3.0/gems/rdiscount-2.2.0.1/ext/basename.o
/usr/lib64/ruby/gems/2.3.0/gems/rdiscount-2.2.0.1/ext/blocktags
/usr/lib64/ruby/gems/2.3.0/gems/rdiscount-2.2.0.1/ext/config.h
/usr/lib64/ruby/gems/2.3.0/gems/rdiscount-2.2.0.1/ext/css.c
/usr/lib64/ruby/gems/2.3.0/gems/rdiscount-2.2.0.1/ext/css.o
/usr/lib64/ruby/gems/2.3.0/gems/rdiscount-2.2.0.1/ext/cstring.h
/usr/lib64/ruby/gems/2.3.0/gems/rdiscount-2.2.0.1/ext/docheader.c
/usr/lib64/ruby/gems/2.3.0/gems/rdiscount-2.2.0.1/ext/docheader.o
/usr/lib64/ruby/gems/2.3.0/gems/rdiscount-2.2.0.1/ext/dumptree.c
/usr/lib64/ruby/gems/2.3.0/gems/rdiscount-2.2.0.1/ext/dumptree.o
/usr/lib64/ruby/gems/2.3.0/gems/rdiscount-2.2.0.1/ext/emmatch.c
/usr/lib64/ruby/gems/2.3.0/gems/rdiscount-2.2.0.1/ext/emmatch.o
/usr/lib64/ruby/gems/2.3.0/gems/rdiscount-2.2.0.1/ext/extconf.rb
/usr/lib64/ruby/gems/2.3.0/gems/rdiscount-2.2.0.1/ext/flags.c
/usr/lib64/ruby/gems/2.3.0/gems/rdiscount-2.2.0.1/ext/flags.o
/usr/lib64/ruby/gems/2.3.0/gems/rdiscount-2.2.0.1/ext/generate.c
/usr/lib64/ruby/gems/2.3.0/gems/rdiscount-2.2.0.1/ext/generate.o
/usr/lib64/ruby/gems/2.3.0/gems/rdiscount-2.2.0.1/ext/github_flavoured.c
/usr/lib64/ruby/gems/2.3.0/gems/rdiscount-2.2.0.1/ext/github_flavoured.o
/usr/lib64/ruby/gems/2.3.0/gems/rdiscount-2.2.0.1/ext/html5.c
/usr/lib64/ruby/gems/2.3.0/gems/rdiscount-2.2.0.1/ext/html5.o
/usr/lib64/ruby/gems/2.3.0/gems/rdiscount-2.2.0.1/ext/markdown.c
/usr/lib64/ruby/gems/2.3.0/gems/rdiscount-2.2.0.1/ext/markdown.h
/usr/lib64/ruby/gems/2.3.0/gems/rdiscount-2.2.0.1/ext/markdown.o
/usr/lib64/ruby/gems/2.3.0/gems/rdiscount-2.2.0.1/ext/mkdio.c
/usr/lib64/ruby/gems/2.3.0/gems/rdiscount-2.2.0.1/ext/mkdio.h
/usr/lib64/ruby/gems/2.3.0/gems/rdiscount-2.2.0.1/ext/mkdio.o
/usr/lib64/ruby/gems/2.3.0/gems/rdiscount-2.2.0.1/ext/mktags.c
/usr/lib64/ruby/gems/2.3.0/gems/rdiscount-2.2.0.1/ext/mktags.o
/usr/lib64/ruby/gems/2.3.0/gems/rdiscount-2.2.0.1/ext/pgm_options.c
/usr/lib64/ruby/gems/2.3.0/gems/rdiscount-2.2.0.1/ext/pgm_options.h
/usr/lib64/ruby/gems/2.3.0/gems/rdiscount-2.2.0.1/ext/pgm_options.o
/usr/lib64/ruby/gems/2.3.0/gems/rdiscount-2.2.0.1/ext/rdiscount.c
/usr/lib64/ruby/gems/2.3.0/gems/rdiscount-2.2.0.1/ext/rdiscount.o
/usr/lib64/ruby/gems/2.3.0/gems/rdiscount-2.2.0.1/ext/resource.c
/usr/lib64/ruby/gems/2.3.0/gems/rdiscount-2.2.0.1/ext/resource.o
/usr/lib64/ruby/gems/2.3.0/gems/rdiscount-2.2.0.1/ext/ruby-config.h
/usr/lib64/ruby/gems/2.3.0/gems/rdiscount-2.2.0.1/ext/setup.c
/usr/lib64/ruby/gems/2.3.0/gems/rdiscount-2.2.0.1/ext/setup.o
/usr/lib64/ruby/gems/2.3.0/gems/rdiscount-2.2.0.1/ext/tags.c
/usr/lib64/ruby/gems/2.3.0/gems/rdiscount-2.2.0.1/ext/tags.h
/usr/lib64/ruby/gems/2.3.0/gems/rdiscount-2.2.0.1/ext/tags.o
/usr/lib64/ruby/gems/2.3.0/gems/rdiscount-2.2.0.1/ext/toc.c
/usr/lib64/ruby/gems/2.3.0/gems/rdiscount-2.2.0.1/ext/toc.o
/usr/lib64/ruby/gems/2.3.0/gems/rdiscount-2.2.0.1/ext/version.c
/usr/lib64/ruby/gems/2.3.0/gems/rdiscount-2.2.0.1/ext/version.o
/usr/lib64/ruby/gems/2.3.0/gems/rdiscount-2.2.0.1/ext/xml.c
/usr/lib64/ruby/gems/2.3.0/gems/rdiscount-2.2.0.1/ext/xml.o
/usr/lib64/ruby/gems/2.3.0/gems/rdiscount-2.2.0.1/ext/xmlpage.c
/usr/lib64/ruby/gems/2.3.0/gems/rdiscount-2.2.0.1/ext/xmlpage.o
/usr/lib64/ruby/gems/2.3.0/gems/rdiscount-2.2.0.1/lib/markdown.rb
/usr/lib64/ruby/gems/2.3.0/gems/rdiscount-2.2.0.1/lib/rdiscount.rb
/usr/lib64/ruby/gems/2.3.0/gems/rdiscount-2.2.0.1/man/markdown.7
/usr/lib64/ruby/gems/2.3.0/gems/rdiscount-2.2.0.1/man/rdiscount.1
/usr/lib64/ruby/gems/2.3.0/gems/rdiscount-2.2.0.1/man/rdiscount.1.ronn
/usr/lib64/ruby/gems/2.3.0/gems/rdiscount-2.2.0.1/rdiscount.gemspec
/usr/lib64/ruby/gems/2.3.0/gems/rdiscount-2.2.0.1/test/benchmark.rb
/usr/lib64/ruby/gems/2.3.0/gems/rdiscount-2.2.0.1/test/benchmark.txt
/usr/lib64/ruby/gems/2.3.0/gems/rdiscount-2.2.0.1/test/markdown_test.rb
/usr/lib64/ruby/gems/2.3.0/gems/rdiscount-2.2.0.1/test/rdiscount_test.rb
/usr/lib64/ruby/gems/2.3.0/specifications/rdiscount-2.2.0.1.gemspec

%files bin
%defattr(-,root,root,-)
/usr/bin/rdiscount

%files lib
%defattr(-,root,root,-)
/usr/lib64/ruby/gems/2.3.0/extensions/x86_64-linux/2.3.0/rdiscount-2.2.0.1/rdiscount.so
/usr/lib64/ruby/gems/2.3.0/gems/rdiscount-2.2.0.1/ext/rdiscount.so
/usr/lib64/ruby/gems/2.3.0/gems/rdiscount-2.2.0.1/lib/rdiscount.so
