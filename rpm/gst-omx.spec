Name:           gstreamer0.10-omx
Summary:        GStreamer OpenMAX IL wrappers
Version:        0.0.0
Release:        1
Group:          Applications/Multimedia
License:        LGPL v2.1+
URL:            http://gstreamer.net/
Source0:        gstreamer0.10-omx-%{version}.tar.gz
BuildRequires:  pkgconfig(gstreamer-0.10)
BuildRequires:  pkgconfig(gstreamer-plugins-base-0.10)
BuildRequires:  libhybris-devel

%description
GStreamer OpenMAX IL wrappers

%prep
%setup -q

%build
NOCONFIGURE=1 ./autogen.sh
%configure --disable-static --enable-hybris=yes

make

%install
%make_install
install -D -m 644 -o root -g root omx/gstomx.conf $RPM_BUILD_ROOT/etc/xdg/gstomx.conf

%files
%defattr(-,root,root,-)
%{_libdir}/gstreamer-0.10/libgstopenmax.so
%config %{_sysconfdir}/xdg/gstomx.conf
