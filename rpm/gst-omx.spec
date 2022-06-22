Name:           gstreamer1.0-omx
Summary:        GStreamer OpenMAX IL wrappers
Version:        1.10.4
Release:        1
License:        LGPL v2.1+
URL:            https://github.com/sailfishos/gst-omx
Source0:        %{name}-%{version}.tar.gz
Patch1:         0001-Enable-hybris-support.patch
Patch2:         0002-Error-out-if-encoder-doesn-t-accept-our-color-format.patch
Patch3:         0003-Add-GST_VIDEO_FORMAT_NV12_64Z32-to-the-video-format.patch
Patch4:         0004-Fix-error-when-h264-stream-resolution-change.patch
Patch5:         0005-Fix-endless-loop-on-reconfiguration.patch
Patch6:         0006-Prevent-starvation-when-using-buffer-pools.patch
Patch7:         0007-Add-support-for-android-native-buffers.patch
Patch8:         0008-Correctly-align-encoder-input-planes.patch
Patch9:         0009-Enable-the-storeMetaDataInBuffer-encoder-option.patch
Patch10:        0010-Don-t-require-parsed-mpeg4.patch
Patch11:        0011-Utilize-android-color-conversion-for-decoder-output.patch
Patch12:        0012-Skip-OMX-header-version-if-not-defined.patch
Patch13:        0013-omx-Fix-timeout-on-video-decoder-flush.patch
Patch14:        0014-omx-Try-to-fall-back-to-old-Android-native-buffers.patch
Patch15:        0015-omx-Properly-support-OMX_EventPortSettingsChanged-parameters.patch

BuildRequires:  droidmedia-devel
BuildRequires:  droid-hal-devel
BuildRequires:  pkgconfig(libandroid-properties)
BuildRequires:  pkgconfig(gstreamer-1.0)
BuildRequires:  pkgconfig(gstreamer-plugins-base-1.0)
BuildRequires:  pkgconfig(nemo-gstreamer-interfaces-1.0)
BuildRequires:  gstreamer1.0-droid-devel
BuildRequires:  pkgconfig(libhardware)
BuildRequires:  pkgconfig(wayland-egl)
BuildRequires:  pkgconfig(wayland-client)
BuildRequires:  pkgconfig(wayland-cursor)
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libtool

%description
GStreamer OpenMAX IL wrappers

%prep
%setup -q -n %{name}-%{version}/upstream
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1
%patch7 -p1
%patch8 -p1
%patch9 -p1
%patch10 -p1
%patch11 -p1
%patch12 -p1
%patch13 -p1
%patch14 -p1
%patch15 -p1

%build
sed -i -e 's/GTK_DOC_CHECK.*//' configure.ac
export NOCONFIGURE=1
%autogen
%configure --disable-static --with-omx-target=hybris --with-omx-header-path=/usr/lib/droid-devel/include/mm-core/omxcore

make

%install
%make_install

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%defattr(-,root,root,-)
%{_libdir}/gstreamer-1.0/libgstomx.so
