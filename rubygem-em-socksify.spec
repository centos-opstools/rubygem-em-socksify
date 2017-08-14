%global gem_name em-socksify

Name: rubygem-%{gem_name}
Version: XXX
Release: 1%{?dist}
Summary: Transparent proxy support for any EventMachine protocol
Group: Development/Languages
License: MIT
URL: https://github.com/igrigorik/em-socksify
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
Source1: MIT-LICENSE
BuildRequires: ruby(release)
BuildRequires: rubygems-devel

Requires: rubygem(eventmachine)

BuildArch: noarch

%if 0%{?rhel} > 0
Provides: rubygem(%{gem_name}) = %{version}
%endif


%description
Transparent proxy support for any EventMachine protocol

%package doc
Summary: Documentation for %{name}
Group: Documentation
Requires: %{name} = %{version}-%{release}
BuildArch: noarch

%description doc
Documentation for %{name}

%prep
gem unpack %{SOURCE0}
%if 0%{?dlrn} > 0
%setup -q -D -T -n  %{dlrn_nvr}
%else
%setup -q -D -T -n  %{gem_name}-%{version}
%endif
gem spec %{SOURCE0} -l --ruby > %{gem_name}.gemspec


%build
gem build %{gem_name}.gemspec
%gem_install


%install
mkdir -p %{buildroot}%{gem_dir}
cp -pa .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/
cp -p %{SOURCE1} %{buildroot}/%{gem_instdir}/

#Spec suite only includes 2 tests that require external connections,
#commented out since this isn't possible on build server
#%%check
#pushd ./%%{gem_instdir}
#rspec -Ilib spec
#popd

%files
%dir %{gem_instdir}
%exclude %{gem_cache}
%exclude %{gem_instdir}/.gitignore
%{gem_spec}
%doc %{gem_instdir}/MIT-LICENSE
%{gem_libdir}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/README.md
%{gem_instdir}/spec
%{gem_instdir}/Gemfile
%{gem_instdir}/Rakefile
%{gem_instdir}/em-socksify.gemspec

%changelog
