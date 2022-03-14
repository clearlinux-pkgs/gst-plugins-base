#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0x5D2EEE6F6F349D7C (tim@centricular.com)
#
Name     : gst-plugins-base
Version  : 1.20.1
Release  : 56
URL      : https://gstreamer.freedesktop.org/src/gst-plugins-base/gst-plugins-base-1.20.1.tar.xz
Source0  : https://gstreamer.freedesktop.org/src/gst-plugins-base/gst-plugins-base-1.20.1.tar.xz
Source1  : https://gstreamer.freedesktop.org/src/gst-plugins-base/gst-plugins-base-1.20.1.tar.xz.asc
Summary  : No detailed summary available
Group    : Development/Tools
License  : GPL-2.0 LGPL-2.1
Requires: gst-plugins-base-bin = %{version}-%{release}
Requires: gst-plugins-base-data = %{version}-%{release}
Requires: gst-plugins-base-filemap = %{version}-%{release}
Requires: gst-plugins-base-lib = %{version}-%{release}
Requires: gst-plugins-base-license = %{version}-%{release}
Requires: gst-plugins-base-locales = %{version}-%{release}
Requires: gst-plugins-base-man = %{version}-%{release}
BuildRequires : SDL2-dev
BuildRequires : buildreq-kde
BuildRequires : buildreq-meson
BuildRequires : buildreq-qmake
BuildRequires : clutter-dev
BuildRequires : glu-dev
BuildRequires : gobject-introspection-dev
BuildRequires : graphene-dev
BuildRequires : gstreamer-dev
BuildRequires : libgudev-dev
BuildRequires : libjpeg-turbo-dev
BuildRequires : libogg-dev
BuildRequires : libvorbis-dev
BuildRequires : mesa-dev
BuildRequires : opus-dev
BuildRequires : orc-dev
BuildRequires : pkgconfig(alsa)
BuildRequires : pkgconfig(gstreamer-audio-1.0)
BuildRequires : pkgconfig(gstreamer-sdp-1.0)
BuildRequires : pkgconfig(gstreamer-video-1.0)
BuildRequires : pkgconfig(gudev-1.0)
BuildRequires : pkgconfig(iso-codes)
BuildRequires : pkgconfig(sdl)
BuildRequires : pkgconfig(theoradec)
BuildRequires : pkgconfig(wayland-protocols)
BuildRequires : pkgconfig(x11)
BuildRequires : pkgconfig(xv)
BuildRequires : qtbase-dev
BuildRequires : valgrind

%description
The RTP libraries
---------------------
RTP Buffers
-----------
The real time protocol as described in RFC 3550 requires the use of special
packets containing an additional RTP header of at least 12 bytes. GStreamer
provides some helper functions for creating and parsing these RTP headers.
The result is a normal #GstBuffer with an additional RTP header.
RTP buffers are usually created with gst_rtp_buffer_new_allocate() or
gst_rtp_buffer_new_allocate_len(). These functions create buffers with a
preallocated space of memory. It will also ensure that enough memory
is allocated for the RTP header. The first function is used when the payload
size is known. gst_rtp_buffer_new_allocate_len() should be used when the size
of the whole RTP buffer (RTP header + payload) is known.
When receiving RTP buffers from a network, gst_rtp_buffer_new_take_data()
should be used when the user would like to parse that RTP packet. (TODO Ask
Wim what the real purpose of this function is as it seems to simply create a
duplicate GstBuffer with the same data as the previous one). The
function will create a new RTP buffer with the given data as the whole RTP
packet. Alternatively, gst_rtp_buffer_new_copy_data() can be used if the user
wishes to make a copy of the data before using it in the new RTP buffer.
It is now possible to use all the gst_rtp_buffer_get_*() or
gst_rtp_buffer_set_*() functions to read or write the different parts of the
RTP header such as the payload type, the sequence number or the RTP
timestamp. The use can also retrieve a pointer to the actual RTP payload data
using the gst_rtp_buffer_get_payload() function.

%package bin
Summary: bin components for the gst-plugins-base package.
Group: Binaries
Requires: gst-plugins-base-data = %{version}-%{release}
Requires: gst-plugins-base-license = %{version}-%{release}
Requires: gst-plugins-base-filemap = %{version}-%{release}

%description bin
bin components for the gst-plugins-base package.


%package data
Summary: data components for the gst-plugins-base package.
Group: Data

%description data
data components for the gst-plugins-base package.


%package dev
Summary: dev components for the gst-plugins-base package.
Group: Development
Requires: gst-plugins-base-lib = %{version}-%{release}
Requires: gst-plugins-base-bin = %{version}-%{release}
Requires: gst-plugins-base-data = %{version}-%{release}
Provides: gst-plugins-base-devel = %{version}-%{release}
Requires: gst-plugins-base = %{version}-%{release}

%description dev
dev components for the gst-plugins-base package.


%package filemap
Summary: filemap components for the gst-plugins-base package.
Group: Default

%description filemap
filemap components for the gst-plugins-base package.


%package lib
Summary: lib components for the gst-plugins-base package.
Group: Libraries
Requires: gst-plugins-base-data = %{version}-%{release}
Requires: gst-plugins-base-license = %{version}-%{release}
Requires: gst-plugins-base-filemap = %{version}-%{release}

%description lib
lib components for the gst-plugins-base package.


%package license
Summary: license components for the gst-plugins-base package.
Group: Default

%description license
license components for the gst-plugins-base package.


%package locales
Summary: locales components for the gst-plugins-base package.
Group: Default

%description locales
locales components for the gst-plugins-base package.


%package man
Summary: man components for the gst-plugins-base package.
Group: Default

%description man
man components for the gst-plugins-base package.


%prep
%setup -q -n gst-plugins-base-1.20.1
cd %{_builddir}/gst-plugins-base-1.20.1
pushd ..
cp -a gst-plugins-base-1.20.1 buildavx2
popd
pushd ..
cp -a gst-plugins-base-1.20.1 buildavx512
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1647283633
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto "
CFLAGS="$CFLAGS" CXXFLAGS="$CXXFLAGS" LDFLAGS="$LDFLAGS" meson --libdir=lib64 --prefix=/usr --buildtype=plain --wrap-mode=nodownload \
-Dtheora=enabled  builddir
ninja -v -C builddir
CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 -O3" CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 " LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3" meson --libdir=lib64 --prefix=/usr --buildtype=plain --wrap-mode=nodownload \
-Dtheora=enabled  builddiravx2
ninja -v -C builddiravx2
CFLAGS="$CFLAGS -m64 -march=x86-64-v4 -Wl,-z,x86-64-v4 -O3" CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v4 -Wl,-z,x86-64-v4 " LDFLAGS="$LDFLAGS -m64 -march=x86-64-v4" meson --libdir=lib64 --prefix=/usr --buildtype=plain --wrap-mode=nodownload \
-Dtheora=enabled  builddiravx512
ninja -v -C builddiravx512

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
meson test -C builddir --print-errorlogs || :

%install
mkdir -p %{buildroot}/usr/share/package-licenses/gst-plugins-base
cp %{_builddir}/gst-plugins-base-1.20.1/COPYING %{buildroot}/usr/share/package-licenses/gst-plugins-base/39743f6cf5d70ee54b72485784313148db159a70
cp %{_builddir}/gst-plugins-base-1.20.1/docs/random/LICENSE %{buildroot}/usr/share/package-licenses/gst-plugins-base/22990b105a08bb838c95fcc4bc5450c6dfdc79ac
DESTDIR=%{buildroot}-v3 ninja -C builddiravx2 install
DESTDIR=%{buildroot}-v4 ninja -C builddiravx512 install
DESTDIR=%{buildroot} ninja -C builddir install
%find_lang gst-plugins-base-1.0
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot}/usr/share/clear/optimized-elf/ %{buildroot}/usr/share/clear/filemap/filemap-%{name}
/usr/bin/elf-move.py avx512 %{buildroot}-v4 %{buildroot}/usr/share/clear/optimized-elf/ %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/gst-device-monitor-1.0
/usr/bin/gst-discoverer-1.0
/usr/bin/gst-play-1.0
/usr/share/clear/optimized-elf/bin*

%files data
%defattr(-,root,root,-)
/usr/lib64/girepository-1.0/GstAllocators-1.0.typelib
/usr/lib64/girepository-1.0/GstApp-1.0.typelib
/usr/lib64/girepository-1.0/GstAudio-1.0.typelib
/usr/lib64/girepository-1.0/GstGL-1.0.typelib
/usr/lib64/girepository-1.0/GstGLEGL-1.0.typelib
/usr/lib64/girepository-1.0/GstGLWayland-1.0.typelib
/usr/lib64/girepository-1.0/GstGLX11-1.0.typelib
/usr/lib64/girepository-1.0/GstPbutils-1.0.typelib
/usr/lib64/girepository-1.0/GstRtp-1.0.typelib
/usr/lib64/girepository-1.0/GstRtsp-1.0.typelib
/usr/lib64/girepository-1.0/GstSdp-1.0.typelib
/usr/lib64/girepository-1.0/GstTag-1.0.typelib
/usr/lib64/girepository-1.0/GstVideo-1.0.typelib
/usr/share/gir-1.0/*.gir
/usr/share/gst-plugins-base/1.0/license-translations.dict

%files dev
%defattr(-,root,root,-)
/usr/include/gstreamer-1.0/gst/allocators/allocators-prelude.h
/usr/include/gstreamer-1.0/gst/allocators/allocators.h
/usr/include/gstreamer-1.0/gst/allocators/gstdmabuf.h
/usr/include/gstreamer-1.0/gst/allocators/gstfdmemory.h
/usr/include/gstreamer-1.0/gst/allocators/gstphysmemory.h
/usr/include/gstreamer-1.0/gst/app/app-enumtypes.h
/usr/include/gstreamer-1.0/gst/app/app-prelude.h
/usr/include/gstreamer-1.0/gst/app/app.h
/usr/include/gstreamer-1.0/gst/app/gstappsink.h
/usr/include/gstreamer-1.0/gst/app/gstappsrc.h
/usr/include/gstreamer-1.0/gst/audio/audio-buffer.h
/usr/include/gstreamer-1.0/gst/audio/audio-channel-mixer.h
/usr/include/gstreamer-1.0/gst/audio/audio-channels.h
/usr/include/gstreamer-1.0/gst/audio/audio-converter.h
/usr/include/gstreamer-1.0/gst/audio/audio-enumtypes.h
/usr/include/gstreamer-1.0/gst/audio/audio-format.h
/usr/include/gstreamer-1.0/gst/audio/audio-info.h
/usr/include/gstreamer-1.0/gst/audio/audio-prelude.h
/usr/include/gstreamer-1.0/gst/audio/audio-quantize.h
/usr/include/gstreamer-1.0/gst/audio/audio-resampler.h
/usr/include/gstreamer-1.0/gst/audio/audio.h
/usr/include/gstreamer-1.0/gst/audio/gstaudioaggregator.h
/usr/include/gstreamer-1.0/gst/audio/gstaudiobasesink.h
/usr/include/gstreamer-1.0/gst/audio/gstaudiobasesrc.h
/usr/include/gstreamer-1.0/gst/audio/gstaudiocdsrc.h
/usr/include/gstreamer-1.0/gst/audio/gstaudioclock.h
/usr/include/gstreamer-1.0/gst/audio/gstaudiodecoder.h
/usr/include/gstreamer-1.0/gst/audio/gstaudioencoder.h
/usr/include/gstreamer-1.0/gst/audio/gstaudiofilter.h
/usr/include/gstreamer-1.0/gst/audio/gstaudioiec61937.h
/usr/include/gstreamer-1.0/gst/audio/gstaudiometa.h
/usr/include/gstreamer-1.0/gst/audio/gstaudioringbuffer.h
/usr/include/gstreamer-1.0/gst/audio/gstaudiosink.h
/usr/include/gstreamer-1.0/gst/audio/gstaudiosrc.h
/usr/include/gstreamer-1.0/gst/audio/gstaudiostreamalign.h
/usr/include/gstreamer-1.0/gst/audio/streamvolume.h
/usr/include/gstreamer-1.0/gst/fft/fft-prelude.h
/usr/include/gstreamer-1.0/gst/fft/fft.h
/usr/include/gstreamer-1.0/gst/fft/gstfft.h
/usr/include/gstreamer-1.0/gst/fft/gstfftf32.h
/usr/include/gstreamer-1.0/gst/fft/gstfftf64.h
/usr/include/gstreamer-1.0/gst/fft/gstffts16.h
/usr/include/gstreamer-1.0/gst/fft/gstffts32.h
/usr/include/gstreamer-1.0/gst/gl/egl/egl.h
/usr/include/gstreamer-1.0/gst/gl/egl/gstegl.h
/usr/include/gstreamer-1.0/gst/gl/egl/gsteglimage.h
/usr/include/gstreamer-1.0/gst/gl/egl/gstgldisplay_egl.h
/usr/include/gstreamer-1.0/gst/gl/egl/gstgldisplay_egl_device.h
/usr/include/gstreamer-1.0/gst/gl/egl/gstglmemoryegl.h
/usr/include/gstreamer-1.0/gst/gl/gl-enumtypes.h
/usr/include/gstreamer-1.0/gst/gl/gl-prelude.h
/usr/include/gstreamer-1.0/gst/gl/gl.h
/usr/include/gstreamer-1.0/gst/gl/glprototypes/all_functions.h
/usr/include/gstreamer-1.0/gst/gl/glprototypes/base.h
/usr/include/gstreamer-1.0/gst/gl/glprototypes/blending.h
/usr/include/gstreamer-1.0/gst/gl/glprototypes/buffer_storage.h
/usr/include/gstreamer-1.0/gst/gl/glprototypes/buffers.h
/usr/include/gstreamer-1.0/gst/gl/glprototypes/debug.h
/usr/include/gstreamer-1.0/gst/gl/glprototypes/eglimage.h
/usr/include/gstreamer-1.0/gst/gl/glprototypes/fbo.h
/usr/include/gstreamer-1.0/gst/gl/glprototypes/fixedfunction.h
/usr/include/gstreamer-1.0/gst/gl/glprototypes/gles.h
/usr/include/gstreamer-1.0/gst/gl/glprototypes/gstgl_compat.h
/usr/include/gstreamer-1.0/gst/gl/glprototypes/gstgl_gles2compat.h
/usr/include/gstreamer-1.0/gst/gl/glprototypes/opengl.h
/usr/include/gstreamer-1.0/gst/gl/glprototypes/query.h
/usr/include/gstreamer-1.0/gst/gl/glprototypes/shaders.h
/usr/include/gstreamer-1.0/gst/gl/glprototypes/sync.h
/usr/include/gstreamer-1.0/gst/gl/glprototypes/vao.h
/usr/include/gstreamer-1.0/gst/gl/gstgl_enums.h
/usr/include/gstreamer-1.0/gst/gl/gstgl_fwd.h
/usr/include/gstreamer-1.0/gst/gl/gstglapi.h
/usr/include/gstreamer-1.0/gst/gl/gstglbasefilter.h
/usr/include/gstreamer-1.0/gst/gl/gstglbasememory.h
/usr/include/gstreamer-1.0/gst/gl/gstglbasesrc.h
/usr/include/gstreamer-1.0/gst/gl/gstglbuffer.h
/usr/include/gstreamer-1.0/gst/gl/gstglbufferpool.h
/usr/include/gstreamer-1.0/gst/gl/gstglcolorconvert.h
/usr/include/gstreamer-1.0/gst/gl/gstglcontext.h
/usr/include/gstreamer-1.0/gst/gl/gstglcontextconfig.h
/usr/include/gstreamer-1.0/gst/gl/gstgldebug.h
/usr/include/gstreamer-1.0/gst/gl/gstgldisplay.h
/usr/include/gstreamer-1.0/gst/gl/gstglfeature.h
/usr/include/gstreamer-1.0/gst/gl/gstglfilter.h
/usr/include/gstreamer-1.0/gst/gl/gstglformat.h
/usr/include/gstreamer-1.0/gst/gl/gstglframebuffer.h
/usr/include/gstreamer-1.0/gst/gl/gstglfuncs.h
/usr/include/gstreamer-1.0/gst/gl/gstglmemory.h
/usr/include/gstreamer-1.0/gst/gl/gstglmemorypbo.h
/usr/include/gstreamer-1.0/gst/gl/gstgloverlaycompositor.h
/usr/include/gstreamer-1.0/gst/gl/gstglquery.h
/usr/include/gstreamer-1.0/gst/gl/gstglrenderbuffer.h
/usr/include/gstreamer-1.0/gst/gl/gstglshader.h
/usr/include/gstreamer-1.0/gst/gl/gstglshaderstrings.h
/usr/include/gstreamer-1.0/gst/gl/gstglsl.h
/usr/include/gstreamer-1.0/gst/gl/gstglslstage.h
/usr/include/gstreamer-1.0/gst/gl/gstglsyncmeta.h
/usr/include/gstreamer-1.0/gst/gl/gstglupload.h
/usr/include/gstreamer-1.0/gst/gl/gstglutils.h
/usr/include/gstreamer-1.0/gst/gl/gstglviewconvert.h
/usr/include/gstreamer-1.0/gst/gl/gstglwindow.h
/usr/include/gstreamer-1.0/gst/gl/wayland/gstgldisplay_wayland.h
/usr/include/gstreamer-1.0/gst/gl/wayland/wayland.h
/usr/include/gstreamer-1.0/gst/gl/x11/gstgldisplay_x11.h
/usr/include/gstreamer-1.0/gst/gl/x11/x11.h
/usr/include/gstreamer-1.0/gst/pbutils/codec-utils.h
/usr/include/gstreamer-1.0/gst/pbutils/descriptions.h
/usr/include/gstreamer-1.0/gst/pbutils/encoding-profile.h
/usr/include/gstreamer-1.0/gst/pbutils/encoding-target.h
/usr/include/gstreamer-1.0/gst/pbutils/gstaudiovisualizer.h
/usr/include/gstreamer-1.0/gst/pbutils/gstdiscoverer.h
/usr/include/gstreamer-1.0/gst/pbutils/gstpluginsbaseversion.h
/usr/include/gstreamer-1.0/gst/pbutils/install-plugins.h
/usr/include/gstreamer-1.0/gst/pbutils/missing-plugins.h
/usr/include/gstreamer-1.0/gst/pbutils/pbutils-enumtypes.h
/usr/include/gstreamer-1.0/gst/pbutils/pbutils-prelude.h
/usr/include/gstreamer-1.0/gst/pbutils/pbutils.h
/usr/include/gstreamer-1.0/gst/riff/riff-ids.h
/usr/include/gstreamer-1.0/gst/riff/riff-media.h
/usr/include/gstreamer-1.0/gst/riff/riff-prelude.h
/usr/include/gstreamer-1.0/gst/riff/riff-read.h
/usr/include/gstreamer-1.0/gst/riff/riff.h
/usr/include/gstreamer-1.0/gst/rtp/gstrtcpbuffer.h
/usr/include/gstreamer-1.0/gst/rtp/gstrtp-enumtypes.h
/usr/include/gstreamer-1.0/gst/rtp/gstrtpbaseaudiopayload.h
/usr/include/gstreamer-1.0/gst/rtp/gstrtpbasedepayload.h
/usr/include/gstreamer-1.0/gst/rtp/gstrtpbasepayload.h
/usr/include/gstreamer-1.0/gst/rtp/gstrtpbuffer.h
/usr/include/gstreamer-1.0/gst/rtp/gstrtpdefs.h
/usr/include/gstreamer-1.0/gst/rtp/gstrtphdrext.h
/usr/include/gstreamer-1.0/gst/rtp/gstrtpmeta.h
/usr/include/gstreamer-1.0/gst/rtp/gstrtppayloads.h
/usr/include/gstreamer-1.0/gst/rtp/rtp-prelude.h
/usr/include/gstreamer-1.0/gst/rtp/rtp.h
/usr/include/gstreamer-1.0/gst/rtsp/gstrtsp-enumtypes.h
/usr/include/gstreamer-1.0/gst/rtsp/gstrtsp.h
/usr/include/gstreamer-1.0/gst/rtsp/gstrtspconnection.h
/usr/include/gstreamer-1.0/gst/rtsp/gstrtspdefs.h
/usr/include/gstreamer-1.0/gst/rtsp/gstrtspextension.h
/usr/include/gstreamer-1.0/gst/rtsp/gstrtspmessage.h
/usr/include/gstreamer-1.0/gst/rtsp/gstrtsprange.h
/usr/include/gstreamer-1.0/gst/rtsp/gstrtsptransport.h
/usr/include/gstreamer-1.0/gst/rtsp/gstrtspurl.h
/usr/include/gstreamer-1.0/gst/rtsp/rtsp-prelude.h
/usr/include/gstreamer-1.0/gst/rtsp/rtsp.h
/usr/include/gstreamer-1.0/gst/sdp/gstmikey.h
/usr/include/gstreamer-1.0/gst/sdp/gstsdp.h
/usr/include/gstreamer-1.0/gst/sdp/gstsdpmessage.h
/usr/include/gstreamer-1.0/gst/sdp/sdp-prelude.h
/usr/include/gstreamer-1.0/gst/sdp/sdp.h
/usr/include/gstreamer-1.0/gst/tag/gsttagdemux.h
/usr/include/gstreamer-1.0/gst/tag/gsttagmux.h
/usr/include/gstreamer-1.0/gst/tag/tag-enumtypes.h
/usr/include/gstreamer-1.0/gst/tag/tag-prelude.h
/usr/include/gstreamer-1.0/gst/tag/tag.h
/usr/include/gstreamer-1.0/gst/tag/xmpwriter.h
/usr/include/gstreamer-1.0/gst/video/colorbalance.h
/usr/include/gstreamer-1.0/gst/video/colorbalancechannel.h
/usr/include/gstreamer-1.0/gst/video/gstvideoaffinetransformationmeta.h
/usr/include/gstreamer-1.0/gst/video/gstvideoaggregator.h
/usr/include/gstreamer-1.0/gst/video/gstvideocodecalphameta.h
/usr/include/gstreamer-1.0/gst/video/gstvideodecoder.h
/usr/include/gstreamer-1.0/gst/video/gstvideoencoder.h
/usr/include/gstreamer-1.0/gst/video/gstvideofilter.h
/usr/include/gstreamer-1.0/gst/video/gstvideometa.h
/usr/include/gstreamer-1.0/gst/video/gstvideopool.h
/usr/include/gstreamer-1.0/gst/video/gstvideosink.h
/usr/include/gstreamer-1.0/gst/video/gstvideotimecode.h
/usr/include/gstreamer-1.0/gst/video/gstvideoutils.h
/usr/include/gstreamer-1.0/gst/video/navigation.h
/usr/include/gstreamer-1.0/gst/video/video-anc.h
/usr/include/gstreamer-1.0/gst/video/video-blend.h
/usr/include/gstreamer-1.0/gst/video/video-chroma.h
/usr/include/gstreamer-1.0/gst/video/video-color.h
/usr/include/gstreamer-1.0/gst/video/video-converter.h
/usr/include/gstreamer-1.0/gst/video/video-dither.h
/usr/include/gstreamer-1.0/gst/video/video-enumtypes.h
/usr/include/gstreamer-1.0/gst/video/video-event.h
/usr/include/gstreamer-1.0/gst/video/video-format.h
/usr/include/gstreamer-1.0/gst/video/video-frame.h
/usr/include/gstreamer-1.0/gst/video/video-hdr.h
/usr/include/gstreamer-1.0/gst/video/video-info.h
/usr/include/gstreamer-1.0/gst/video/video-multiview.h
/usr/include/gstreamer-1.0/gst/video/video-overlay-composition.h
/usr/include/gstreamer-1.0/gst/video/video-prelude.h
/usr/include/gstreamer-1.0/gst/video/video-resampler.h
/usr/include/gstreamer-1.0/gst/video/video-scaler.h
/usr/include/gstreamer-1.0/gst/video/video-tile.h
/usr/include/gstreamer-1.0/gst/video/video.h
/usr/include/gstreamer-1.0/gst/video/videodirection.h
/usr/include/gstreamer-1.0/gst/video/videoorientation.h
/usr/include/gstreamer-1.0/gst/video/videooverlay.h
/usr/lib64/gstreamer-1.0/include/gst/gl/gstglconfig.h
/usr/lib64/libgstallocators-1.0.so
/usr/lib64/libgstapp-1.0.so
/usr/lib64/libgstaudio-1.0.so
/usr/lib64/libgstfft-1.0.so
/usr/lib64/libgstgl-1.0.so
/usr/lib64/libgstpbutils-1.0.so
/usr/lib64/libgstriff-1.0.so
/usr/lib64/libgstrtp-1.0.so
/usr/lib64/libgstrtsp-1.0.so
/usr/lib64/libgstsdp-1.0.so
/usr/lib64/libgsttag-1.0.so
/usr/lib64/libgstvideo-1.0.so
/usr/lib64/pkgconfig/gstreamer-allocators-1.0.pc
/usr/lib64/pkgconfig/gstreamer-app-1.0.pc
/usr/lib64/pkgconfig/gstreamer-audio-1.0.pc
/usr/lib64/pkgconfig/gstreamer-fft-1.0.pc
/usr/lib64/pkgconfig/gstreamer-gl-1.0.pc
/usr/lib64/pkgconfig/gstreamer-gl-egl-1.0.pc
/usr/lib64/pkgconfig/gstreamer-gl-prototypes-1.0.pc
/usr/lib64/pkgconfig/gstreamer-gl-wayland-1.0.pc
/usr/lib64/pkgconfig/gstreamer-gl-x11-1.0.pc
/usr/lib64/pkgconfig/gstreamer-pbutils-1.0.pc
/usr/lib64/pkgconfig/gstreamer-plugins-base-1.0.pc
/usr/lib64/pkgconfig/gstreamer-riff-1.0.pc
/usr/lib64/pkgconfig/gstreamer-rtp-1.0.pc
/usr/lib64/pkgconfig/gstreamer-rtsp-1.0.pc
/usr/lib64/pkgconfig/gstreamer-sdp-1.0.pc
/usr/lib64/pkgconfig/gstreamer-tag-1.0.pc
/usr/lib64/pkgconfig/gstreamer-video-1.0.pc

%files filemap
%defattr(-,root,root,-)
/usr/share/clear/filemap/filemap-gst-plugins-base

%files lib
%defattr(-,root,root,-)
/usr/lib64/gstreamer-1.0/libgstadder.so
/usr/lib64/gstreamer-1.0/libgstalsa.so
/usr/lib64/gstreamer-1.0/libgstapp.so
/usr/lib64/gstreamer-1.0/libgstaudioconvert.so
/usr/lib64/gstreamer-1.0/libgstaudiomixer.so
/usr/lib64/gstreamer-1.0/libgstaudiorate.so
/usr/lib64/gstreamer-1.0/libgstaudioresample.so
/usr/lib64/gstreamer-1.0/libgstaudiotestsrc.so
/usr/lib64/gstreamer-1.0/libgstcompositor.so
/usr/lib64/gstreamer-1.0/libgstencoding.so
/usr/lib64/gstreamer-1.0/libgstgio.so
/usr/lib64/gstreamer-1.0/libgstogg.so
/usr/lib64/gstreamer-1.0/libgstopengl.so
/usr/lib64/gstreamer-1.0/libgstopus.so
/usr/lib64/gstreamer-1.0/libgstoverlaycomposition.so
/usr/lib64/gstreamer-1.0/libgstpango.so
/usr/lib64/gstreamer-1.0/libgstpbtypes.so
/usr/lib64/gstreamer-1.0/libgstplayback.so
/usr/lib64/gstreamer-1.0/libgstrawparse.so
/usr/lib64/gstreamer-1.0/libgstsubparse.so
/usr/lib64/gstreamer-1.0/libgsttcp.so
/usr/lib64/gstreamer-1.0/libgsttheora.so
/usr/lib64/gstreamer-1.0/libgsttypefindfunctions.so
/usr/lib64/gstreamer-1.0/libgstvideoconvert.so
/usr/lib64/gstreamer-1.0/libgstvideorate.so
/usr/lib64/gstreamer-1.0/libgstvideoscale.so
/usr/lib64/gstreamer-1.0/libgstvideotestsrc.so
/usr/lib64/gstreamer-1.0/libgstvolume.so
/usr/lib64/gstreamer-1.0/libgstvorbis.so
/usr/lib64/gstreamer-1.0/libgstximagesink.so
/usr/lib64/gstreamer-1.0/libgstxvimagesink.so
/usr/lib64/libgstallocators-1.0.so.0
/usr/lib64/libgstallocators-1.0.so.0.2001.0
/usr/lib64/libgstapp-1.0.so.0
/usr/lib64/libgstapp-1.0.so.0.2001.0
/usr/lib64/libgstaudio-1.0.so.0
/usr/lib64/libgstaudio-1.0.so.0.2001.0
/usr/lib64/libgstfft-1.0.so.0
/usr/lib64/libgstfft-1.0.so.0.2001.0
/usr/lib64/libgstgl-1.0.so.0
/usr/lib64/libgstgl-1.0.so.0.2001.0
/usr/lib64/libgstpbutils-1.0.so.0
/usr/lib64/libgstpbutils-1.0.so.0.2001.0
/usr/lib64/libgstriff-1.0.so.0
/usr/lib64/libgstriff-1.0.so.0.2001.0
/usr/lib64/libgstrtp-1.0.so.0
/usr/lib64/libgstrtp-1.0.so.0.2001.0
/usr/lib64/libgstrtsp-1.0.so.0
/usr/lib64/libgstrtsp-1.0.so.0.2001.0
/usr/lib64/libgstsdp-1.0.so.0
/usr/lib64/libgstsdp-1.0.so.0.2001.0
/usr/lib64/libgsttag-1.0.so.0
/usr/lib64/libgsttag-1.0.so.0.2001.0
/usr/lib64/libgstvideo-1.0.so.0
/usr/lib64/libgstvideo-1.0.so.0.2001.0
/usr/share/clear/optimized-elf/lib*

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/gst-plugins-base/22990b105a08bb838c95fcc4bc5450c6dfdc79ac
/usr/share/package-licenses/gst-plugins-base/39743f6cf5d70ee54b72485784313148db159a70

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/gst-device-monitor-1.0.1
/usr/share/man/man1/gst-discoverer-1.0.1
/usr/share/man/man1/gst-play-1.0.1

%files locales -f gst-plugins-base-1.0.lang
%defattr(-,root,root,-)

