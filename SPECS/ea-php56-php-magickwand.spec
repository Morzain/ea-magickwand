%global scl_version ea-php56
%global ext_prefix opt/cpanel/%{scl_version}/root
%global ext_dir usr/%{_lib}/php/modules
%global conf_dir etc/php.d

Name:           %{scl_version}-php-magickwand
Version:        1.0.9
Summary:        magickwand extension for %{scl_version} 
%define         release_prefix 1
Release:        %{release_prefix}%{?dist}
License:        MIT 
Group:          Programming/Languages
URL:            https://www.magickwand.org/
Source:         http://www.magickwand.org/download/php/MagickWandForPHP-%{version}-2.tar.gz
Source1:        magickwand.ini

BuildRequires: %{scl_version} %{scl_version}-php-cli lw-ImageMagick 

%description
MagickWand is a native php extension to create 
and modify images using the ImageMagick MagickWand API.

%prep
%setup -n MagickWandForPHP-%{version}


%build
scl enable %{scl_version} phpize
scl enable %{scl_version} ./configure
make


%install
make install INSTALL_ROOT=%{buildroot}
install -m 755 -d %{buildroot}/%{ext_prefix}/%{conf_dir}
install -m 644 %{SOURCE1} %{buildroot}/%{ext_prefix}/%{conf_dir}/

%clean
%{__rm} -rf %{buildroot}

%files
/%{ext_prefix}/%{ext_dir}/magickwand.so
%config /%{ext_prefix}/%{conf_dir}/magickwand.ini


%changelog
* Wed Aug 16 2017 Michael Wineland
- Initial spec file creation.
