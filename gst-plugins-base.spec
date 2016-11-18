#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : gst-plugins-base
Version  : 1.10.1
Release  : 10
URL      : https://gstreamer.freedesktop.org/src/gst-plugins-base/gst-plugins-base-1.10.1.tar.xz
Source0  : https://gstreamer.freedesktop.org/src/gst-plugins-base/gst-plugins-base-1.10.1.tar.xz
Summary  : GStreamer streaming media framework plug-ins
Group    : Development/Tools
License  : GPL-2.0
Requires: gst-plugins-base-bin
Requires: gst-plugins-base-lib
Requires: gst-plugins-base-data
Requires: gst-plugins-base-doc
Requires: gst-plugins-base-locales
BuildRequires : docbook-xml
BuildRequires : gettext
BuildRequires : gobject-introspection
BuildRequires : gobject-introspection-dev
BuildRequires : gstreamer-dev
BuildRequires : gtk-doc
BuildRequires : gtk-doc-dev
BuildRequires : libxslt-bin
BuildRequires : perl(XML::Parser)
BuildRequires : pkgconfig(alsa)
BuildRequires : pkgconfig(gio-unix-2.0)
BuildRequires : pkgconfig(gtk+-3.0)
BuildRequires : pkgconfig(gtk+-x11-3.0)
BuildRequires : pkgconfig(ogg)
BuildRequires : pkgconfig(pango)
BuildRequires : pkgconfig(theoradec)
BuildRequires : pkgconfig(vorbis)
BuildRequires : pkgconfig(x11)
BuildRequires : pkgconfig(xext)
BuildRequires : pkgconfig(xv)
BuildRequires : pkgconfig(zlib)
BuildRequires : valgrind

%description
GStreamer is a streaming media framework, based on graphs of filters which
operate on media data. Applications using this library can do anything
from real-time sound processing to playing videos, and just about anything
else media-related.  Its plugin-based architecture means that new data
types or processing capabilities can be added simply by installing new
plug-ins.

%package bin
Summary: bin components for the gst-plugins-base package.
Group: Binaries
Requires: gst-plugins-base-data

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
Requires: gst-plugins-base-lib
Requires: gst-plugins-base-bin
Requires: gst-plugins-base-data
Provides: gst-plugins-base-devel

%description dev
dev components for the gst-plugins-base package.


%package doc
Summary: doc components for the gst-plugins-base package.
Group: Documentation

%description doc
doc components for the gst-plugins-base package.


%package lib
Summary: lib components for the gst-plugins-base package.
Group: Libraries
Requires: gst-plugins-base-data

%description lib
lib components for the gst-plugins-base package.


%package locales
Summary: locales components for the gst-plugins-base package.
Group: Default

%description locales
locales components for the gst-plugins-base package.


%prep
%setup -q -n gst-plugins-base-1.10.1

%build
export LANG=C
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -falign-functions=32 -flto -fno-semantic-interposition "
export FCFLAGS="$CFLAGS -O3 -falign-functions=32 -flto -fno-semantic-interposition "
export FFLAGS="$CFLAGS -O3 -falign-functions=32 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -falign-functions=32 -flto -fno-semantic-interposition "
%configure --disable-static --enable-theora
make V=1  %{?_smp_mflags}

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost
make VERBOSE=1 V=1 %{?_smp_mflags} check || :

%install
rm -rf %{buildroot}
%make_install
%find_lang gst-plugins-base-1.0

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/gst-device-monitor-1.0
/usr/bin/gst-discoverer-1.0
/usr/bin/gst-play-1.0

%files data
%defattr(-,root,root,-)
/usr/share/gst-plugins-base/1.0/license-translations.dict

%files dev
%defattr(-,root,root,-)
/usr/include/gstreamer-1.0/gst/allocators/allocators.h
/usr/include/gstreamer-1.0/gst/allocators/gstdmabuf.h
/usr/include/gstreamer-1.0/gst/allocators/gstfdmemory.h
/usr/include/gstreamer-1.0/gst/app/app.h
/usr/include/gstreamer-1.0/gst/app/gstappsink.h
/usr/include/gstreamer-1.0/gst/app/gstappsrc.h
/usr/include/gstreamer-1.0/gst/audio/audio-channel-mixer.h
/usr/include/gstreamer-1.0/gst/audio/audio-channels.h
/usr/include/gstreamer-1.0/gst/audio/audio-converter.h
/usr/include/gstreamer-1.0/gst/audio/audio-enumtypes.h
/usr/include/gstreamer-1.0/gst/audio/audio-format.h
/usr/include/gstreamer-1.0/gst/audio/audio-info.h
/usr/include/gstreamer-1.0/gst/audio/audio-quantize.h
/usr/include/gstreamer-1.0/gst/audio/audio-resampler.h
/usr/include/gstreamer-1.0/gst/audio/audio.h
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
/usr/include/gstreamer-1.0/gst/audio/streamvolume.h
/usr/include/gstreamer-1.0/gst/fft/fft.h
/usr/include/gstreamer-1.0/gst/fft/gstfft.h
/usr/include/gstreamer-1.0/gst/fft/gstfftf32.h
/usr/include/gstreamer-1.0/gst/fft/gstfftf64.h
/usr/include/gstreamer-1.0/gst/fft/gstffts16.h
/usr/include/gstreamer-1.0/gst/fft/gstffts32.h
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
/usr/include/gstreamer-1.0/gst/pbutils/pbutils.h
/usr/include/gstreamer-1.0/gst/riff/riff-ids.h
/usr/include/gstreamer-1.0/gst/riff/riff-media.h
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
/usr/include/gstreamer-1.0/gst/rtp/gstrtppayloads.h
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
/usr/include/gstreamer-1.0/gst/rtsp/rtsp.h
/usr/include/gstreamer-1.0/gst/sdp/gstmikey.h
/usr/include/gstreamer-1.0/gst/sdp/gstsdp.h
/usr/include/gstreamer-1.0/gst/sdp/gstsdpmessage.h
/usr/include/gstreamer-1.0/gst/sdp/sdp.h
/usr/include/gstreamer-1.0/gst/tag/gsttagdemux.h
/usr/include/gstreamer-1.0/gst/tag/gsttagmux.h
/usr/include/gstreamer-1.0/gst/tag/tag.h
/usr/include/gstreamer-1.0/gst/tag/xmpwriter.h
/usr/include/gstreamer-1.0/gst/video/colorbalance.h
/usr/include/gstreamer-1.0/gst/video/colorbalancechannel.h
/usr/include/gstreamer-1.0/gst/video/gstvideoaffinetransformationmeta.h
/usr/include/gstreamer-1.0/gst/video/gstvideodecoder.h
/usr/include/gstreamer-1.0/gst/video/gstvideoencoder.h
/usr/include/gstreamer-1.0/gst/video/gstvideofilter.h
/usr/include/gstreamer-1.0/gst/video/gstvideometa.h
/usr/include/gstreamer-1.0/gst/video/gstvideopool.h
/usr/include/gstreamer-1.0/gst/video/gstvideosink.h
/usr/include/gstreamer-1.0/gst/video/gstvideotimecode.h
/usr/include/gstreamer-1.0/gst/video/gstvideoutils.h
/usr/include/gstreamer-1.0/gst/video/navigation.h
/usr/include/gstreamer-1.0/gst/video/video-blend.h
/usr/include/gstreamer-1.0/gst/video/video-chroma.h
/usr/include/gstreamer-1.0/gst/video/video-color.h
/usr/include/gstreamer-1.0/gst/video/video-converter.h
/usr/include/gstreamer-1.0/gst/video/video-dither.h
/usr/include/gstreamer-1.0/gst/video/video-enumtypes.h
/usr/include/gstreamer-1.0/gst/video/video-event.h
/usr/include/gstreamer-1.0/gst/video/video-format.h
/usr/include/gstreamer-1.0/gst/video/video-frame.h
/usr/include/gstreamer-1.0/gst/video/video-info.h
/usr/include/gstreamer-1.0/gst/video/video-multiview.h
/usr/include/gstreamer-1.0/gst/video/video-overlay-composition.h
/usr/include/gstreamer-1.0/gst/video/video-resampler.h
/usr/include/gstreamer-1.0/gst/video/video-scaler.h
/usr/include/gstreamer-1.0/gst/video/video-tile.h
/usr/include/gstreamer-1.0/gst/video/video.h
/usr/include/gstreamer-1.0/gst/video/videodirection.h
/usr/include/gstreamer-1.0/gst/video/videoorientation.h
/usr/include/gstreamer-1.0/gst/video/videooverlay.h
/usr/lib64/*.so
/usr/lib64/girepository-1.0/GstAllocators-1.0.typelib
/usr/lib64/girepository-1.0/GstApp-1.0.typelib
/usr/lib64/girepository-1.0/GstAudio-1.0.typelib
/usr/lib64/girepository-1.0/GstFft-1.0.typelib
/usr/lib64/girepository-1.0/GstPbutils-1.0.typelib
/usr/lib64/girepository-1.0/GstRtp-1.0.typelib
/usr/lib64/girepository-1.0/GstRtsp-1.0.typelib
/usr/lib64/girepository-1.0/GstSdp-1.0.typelib
/usr/lib64/girepository-1.0/GstTag-1.0.typelib
/usr/lib64/girepository-1.0/GstVideo-1.0.typelib
/usr/lib64/pkgconfig/*.pc
/usr/share/gir-1.0/*.gir

%files doc
%defattr(-,root,root,-)
%doc /usr/share/man/man1/*
/usr/share/gtk-doc/html/gst-plugins-base-libs-1.0/annotation-glossary.html
/usr/share/gtk-doc/html/gst-plugins-base-libs-1.0/api-index-deprecated.html
/usr/share/gtk-doc/html/gst-plugins-base-libs-1.0/api-index-full.html
/usr/share/gtk-doc/html/gst-plugins-base-libs-1.0/compiling.html
/usr/share/gtk-doc/html/gst-plugins-base-libs-1.0/gst-plugins-base-libs-1.0.devhelp2
/usr/share/gtk-doc/html/gst-plugins-base-libs-1.0/gst-plugins-base-libs-GstAudioConverter.html
/usr/share/gtk-doc/html/gst-plugins-base-libs-1.0/gst-plugins-base-libs-GstAudioQuantize.html
/usr/share/gtk-doc/html/gst-plugins-base-libs-1.0/gst-plugins-base-libs-GstVideoChroma.html
/usr/share/gtk-doc/html/gst-plugins-base-libs-1.0/gst-plugins-base-libs-GstVideoDecoder.html
/usr/share/gtk-doc/html/gst-plugins-base-libs-1.0/gst-plugins-base-libs-GstVideoDither.html
/usr/share/gtk-doc/html/gst-plugins-base-libs-1.0/gst-plugins-base-libs-GstVideoEncoder.html
/usr/share/gtk-doc/html/gst-plugins-base-libs-1.0/gst-plugins-base-libs-GstVideoPool.html
/usr/share/gtk-doc/html/gst-plugins-base-libs-1.0/gst-plugins-base-libs-GstVideoResampler.html
/usr/share/gtk-doc/html/gst-plugins-base-libs-1.0/gst-plugins-base-libs-GstVideoScaler.html
/usr/share/gtk-doc/html/gst-plugins-base-libs-1.0/gst-plugins-base-libs-appsink.html
/usr/share/gtk-doc/html/gst-plugins-base-libs-1.0/gst-plugins-base-libs-appsrc.html
/usr/share/gtk-doc/html/gst-plugins-base-libs-1.0/gst-plugins-base-libs-dmabuf.html
/usr/share/gtk-doc/html/gst-plugins-base-libs-1.0/gst-plugins-base-libs-encoding-profile.html
/usr/share/gtk-doc/html/gst-plugins-base-libs-1.0/gst-plugins-base-libs-fdmemory.html
/usr/share/gtk-doc/html/gst-plugins-base-libs-1.0/gst-plugins-base-libs-gstaudio.html
/usr/share/gtk-doc/html/gst-plugins-base-libs-1.0/gst-plugins-base-libs-gstaudiobasesink.html
/usr/share/gtk-doc/html/gst-plugins-base-libs-1.0/gst-plugins-base-libs-gstaudiobasesrc.html
/usr/share/gtk-doc/html/gst-plugins-base-libs-1.0/gst-plugins-base-libs-gstaudiocdsrc.html
/usr/share/gtk-doc/html/gst-plugins-base-libs-1.0/gst-plugins-base-libs-gstaudiochannels.html
/usr/share/gtk-doc/html/gst-plugins-base-libs-1.0/gst-plugins-base-libs-gstaudioclock.html
/usr/share/gtk-doc/html/gst-plugins-base-libs-1.0/gst-plugins-base-libs-gstaudiodecoder.html
/usr/share/gtk-doc/html/gst-plugins-base-libs-1.0/gst-plugins-base-libs-gstaudioencoder.html
/usr/share/gtk-doc/html/gst-plugins-base-libs-1.0/gst-plugins-base-libs-gstaudiofilter.html
/usr/share/gtk-doc/html/gst-plugins-base-libs-1.0/gst-plugins-base-libs-gstaudioiec61937.html
/usr/share/gtk-doc/html/gst-plugins-base-libs-1.0/gst-plugins-base-libs-gstaudiometa.html
/usr/share/gtk-doc/html/gst-plugins-base-libs-1.0/gst-plugins-base-libs-gstaudioringbuffer.html
/usr/share/gtk-doc/html/gst-plugins-base-libs-1.0/gst-plugins-base-libs-gstaudiosink.html
/usr/share/gtk-doc/html/gst-plugins-base-libs-1.0/gst-plugins-base-libs-gstaudiosrc.html
/usr/share/gtk-doc/html/gst-plugins-base-libs-1.0/gst-plugins-base-libs-gstcolorbalance.html
/usr/share/gtk-doc/html/gst-plugins-base-libs-1.0/gst-plugins-base-libs-gstcolorbalancechannel.html
/usr/share/gtk-doc/html/gst-plugins-base-libs-1.0/gst-plugins-base-libs-gstdiscoverer.html
/usr/share/gtk-doc/html/gst-plugins-base-libs-1.0/gst-plugins-base-libs-gstfft.html
/usr/share/gtk-doc/html/gst-plugins-base-libs-1.0/gst-plugins-base-libs-gstfftf32.html
/usr/share/gtk-doc/html/gst-plugins-base-libs-1.0/gst-plugins-base-libs-gstfftf64.html
/usr/share/gtk-doc/html/gst-plugins-base-libs-1.0/gst-plugins-base-libs-gstffts16.html
/usr/share/gtk-doc/html/gst-plugins-base-libs-1.0/gst-plugins-base-libs-gstffts32.html
/usr/share/gtk-doc/html/gst-plugins-base-libs-1.0/gst-plugins-base-libs-gstmikey.html
/usr/share/gtk-doc/html/gst-plugins-base-libs-1.0/gst-plugins-base-libs-gstnavigation.html
/usr/share/gtk-doc/html/gst-plugins-base-libs-1.0/gst-plugins-base-libs-gstpbutils.html
/usr/share/gtk-doc/html/gst-plugins-base-libs-1.0/gst-plugins-base-libs-gstpbutilscodecutils.html
/usr/share/gtk-doc/html/gst-plugins-base-libs-1.0/gst-plugins-base-libs-gstpbutilsdescriptions.html
/usr/share/gtk-doc/html/gst-plugins-base-libs-1.0/gst-plugins-base-libs-gstpbutilsinstallplugins.html
/usr/share/gtk-doc/html/gst-plugins-base-libs-1.0/gst-plugins-base-libs-gstpbutilsmissingplugins.html
/usr/share/gtk-doc/html/gst-plugins-base-libs-1.0/gst-plugins-base-libs-gstpluginsbaseversion.html
/usr/share/gtk-doc/html/gst-plugins-base-libs-1.0/gst-plugins-base-libs-gstriff.html
/usr/share/gtk-doc/html/gst-plugins-base-libs-1.0/gst-plugins-base-libs-gstrtcpbuffer.html
/usr/share/gtk-doc/html/gst-plugins-base-libs-1.0/gst-plugins-base-libs-gstrtpbaseaudiopayload.html
/usr/share/gtk-doc/html/gst-plugins-base-libs-1.0/gst-plugins-base-libs-gstrtpbasedepayload.html
/usr/share/gtk-doc/html/gst-plugins-base-libs-1.0/gst-plugins-base-libs-gstrtpbasepayload.html
/usr/share/gtk-doc/html/gst-plugins-base-libs-1.0/gst-plugins-base-libs-gstrtpbuffer.html
/usr/share/gtk-doc/html/gst-plugins-base-libs-1.0/gst-plugins-base-libs-gstrtphdrext.html
/usr/share/gtk-doc/html/gst-plugins-base-libs-1.0/gst-plugins-base-libs-gstrtppayloads.html
/usr/share/gtk-doc/html/gst-plugins-base-libs-1.0/gst-plugins-base-libs-gstrtspconnection.html
/usr/share/gtk-doc/html/gst-plugins-base-libs-1.0/gst-plugins-base-libs-gstrtspdefs.html
/usr/share/gtk-doc/html/gst-plugins-base-libs-1.0/gst-plugins-base-libs-gstrtspextension.html
/usr/share/gtk-doc/html/gst-plugins-base-libs-1.0/gst-plugins-base-libs-gstrtspmessage.html
/usr/share/gtk-doc/html/gst-plugins-base-libs-1.0/gst-plugins-base-libs-gstrtsprange.html
/usr/share/gtk-doc/html/gst-plugins-base-libs-1.0/gst-plugins-base-libs-gstrtsptransport.html
/usr/share/gtk-doc/html/gst-plugins-base-libs-1.0/gst-plugins-base-libs-gstrtspurl.html
/usr/share/gtk-doc/html/gst-plugins-base-libs-1.0/gst-plugins-base-libs-gstsdpmessage.html
/usr/share/gtk-doc/html/gst-plugins-base-libs-1.0/gst-plugins-base-libs-gststreamvolume.html
/usr/share/gtk-doc/html/gst-plugins-base-libs-1.0/gst-plugins-base-libs-gsttag.html
/usr/share/gtk-doc/html/gst-plugins-base-libs-1.0/gst-plugins-base-libs-gsttagdemux.html
/usr/share/gtk-doc/html/gst-plugins-base-libs-1.0/gst-plugins-base-libs-gsttagexif.html
/usr/share/gtk-doc/html/gst-plugins-base-libs-1.0/gst-plugins-base-libs-gsttagid3.html
/usr/share/gtk-doc/html/gst-plugins-base-libs-1.0/gst-plugins-base-libs-gsttaglanguagecodes.html
/usr/share/gtk-doc/html/gst-plugins-base-libs-1.0/gst-plugins-base-libs-gsttaglicenses.html
/usr/share/gtk-doc/html/gst-plugins-base-libs-1.0/gst-plugins-base-libs-gsttagmux.html
/usr/share/gtk-doc/html/gst-plugins-base-libs-1.0/gst-plugins-base-libs-gsttagvorbis.html
/usr/share/gtk-doc/html/gst-plugins-base-libs-1.0/gst-plugins-base-libs-gsttagxmp.html
/usr/share/gtk-doc/html/gst-plugins-base-libs-1.0/gst-plugins-base-libs-gsttagxmpwriter.html
/usr/share/gtk-doc/html/gst-plugins-base-libs-1.0/gst-plugins-base-libs-gstvideo.html
/usr/share/gtk-doc/html/gst-plugins-base-libs-1.0/gst-plugins-base-libs-gstvideoaffinetransformationmeta.html
/usr/share/gtk-doc/html/gst-plugins-base-libs-1.0/gst-plugins-base-libs-gstvideodirection.html
/usr/share/gtk-doc/html/gst-plugins-base-libs-1.0/gst-plugins-base-libs-gstvideofilter.html
/usr/share/gtk-doc/html/gst-plugins-base-libs-1.0/gst-plugins-base-libs-gstvideometa.html
/usr/share/gtk-doc/html/gst-plugins-base-libs-1.0/gst-plugins-base-libs-gstvideoorientation.html
/usr/share/gtk-doc/html/gst-plugins-base-libs-1.0/gst-plugins-base-libs-gstvideooverlay.html
/usr/share/gtk-doc/html/gst-plugins-base-libs-1.0/gst-plugins-base-libs-gstvideooverlaycomposition.html
/usr/share/gtk-doc/html/gst-plugins-base-libs-1.0/gst-plugins-base-libs-gstvideosink.html
/usr/share/gtk-doc/html/gst-plugins-base-libs-1.0/gst-plugins-base-libs-gstvideoutils.html
/usr/share/gtk-doc/html/gst-plugins-base-libs-1.0/gstreamer-allocators.html
/usr/share/gtk-doc/html/gst-plugins-base-libs-1.0/gstreamer-app.html
/usr/share/gtk-doc/html/gst-plugins-base-libs-1.0/gstreamer-audio.html
/usr/share/gtk-doc/html/gst-plugins-base-libs-1.0/gstreamer-base-utils.html
/usr/share/gtk-doc/html/gst-plugins-base-libs-1.0/gstreamer-ffft.html
/usr/share/gtk-doc/html/gst-plugins-base-libs-1.0/gstreamer-libs-hierarchy.html
/usr/share/gtk-doc/html/gst-plugins-base-libs-1.0/gstreamer-mikey.html
/usr/share/gtk-doc/html/gst-plugins-base-libs-1.0/gstreamer-plugins-base.html
/usr/share/gtk-doc/html/gst-plugins-base-libs-1.0/gstreamer-riff.html
/usr/share/gtk-doc/html/gst-plugins-base-libs-1.0/gstreamer-rtp.html
/usr/share/gtk-doc/html/gst-plugins-base-libs-1.0/gstreamer-rtsp.html
/usr/share/gtk-doc/html/gst-plugins-base-libs-1.0/gstreamer-sdp.html
/usr/share/gtk-doc/html/gst-plugins-base-libs-1.0/gstreamer-tag.html
/usr/share/gtk-doc/html/gst-plugins-base-libs-1.0/gstreamer-video.html
/usr/share/gtk-doc/html/gst-plugins-base-libs-1.0/home.png
/usr/share/gtk-doc/html/gst-plugins-base-libs-1.0/index.html
/usr/share/gtk-doc/html/gst-plugins-base-libs-1.0/left-insensitive.png
/usr/share/gtk-doc/html/gst-plugins-base-libs-1.0/left.png
/usr/share/gtk-doc/html/gst-plugins-base-libs-1.0/right-insensitive.png
/usr/share/gtk-doc/html/gst-plugins-base-libs-1.0/right.png
/usr/share/gtk-doc/html/gst-plugins-base-libs-1.0/style.css
/usr/share/gtk-doc/html/gst-plugins-base-libs-1.0/up-insensitive.png
/usr/share/gtk-doc/html/gst-plugins-base-libs-1.0/up.png
/usr/share/gtk-doc/html/gst-plugins-base-plugins-1.0/ch01.html
/usr/share/gtk-doc/html/gst-plugins-base-plugins-1.0/ch02.html
/usr/share/gtk-doc/html/gst-plugins-base-plugins-1.0/gst-plugins-base-plugins-1.0.devhelp2
/usr/share/gtk-doc/html/gst-plugins-base-plugins-1.0/gst-plugins-base-plugins-adder.html
/usr/share/gtk-doc/html/gst-plugins-base-plugins-1.0/gst-plugins-base-plugins-alsamidisrc.html
/usr/share/gtk-doc/html/gst-plugins-base-plugins-1.0/gst-plugins-base-plugins-alsasink.html
/usr/share/gtk-doc/html/gst-plugins-base-plugins-1.0/gst-plugins-base-plugins-alsasrc.html
/usr/share/gtk-doc/html/gst-plugins-base-plugins-1.0/gst-plugins-base-plugins-appsink.html
/usr/share/gtk-doc/html/gst-plugins-base-plugins-1.0/gst-plugins-base-plugins-appsrc.html
/usr/share/gtk-doc/html/gst-plugins-base-plugins-1.0/gst-plugins-base-plugins-audioconvert.html
/usr/share/gtk-doc/html/gst-plugins-base-plugins-1.0/gst-plugins-base-plugins-audiorate.html
/usr/share/gtk-doc/html/gst-plugins-base-plugins-1.0/gst-plugins-base-plugins-audioresample.html
/usr/share/gtk-doc/html/gst-plugins-base-plugins-1.0/gst-plugins-base-plugins-audiotestsrc.html
/usr/share/gtk-doc/html/gst-plugins-base-plugins-1.0/gst-plugins-base-plugins-cdparanoiasrc.html
/usr/share/gtk-doc/html/gst-plugins-base-plugins-1.0/gst-plugins-base-plugins-clockoverlay.html
/usr/share/gtk-doc/html/gst-plugins-base-plugins-1.0/gst-plugins-base-plugins-decodebin.html
/usr/share/gtk-doc/html/gst-plugins-base-plugins-1.0/gst-plugins-base-plugins-decodebin3.html
/usr/share/gtk-doc/html/gst-plugins-base-plugins-1.0/gst-plugins-base-plugins-encodebin.html
/usr/share/gtk-doc/html/gst-plugins-base-plugins-1.0/gst-plugins-base-plugins-giosink.html
/usr/share/gtk-doc/html/gst-plugins-base-plugins-1.0/gst-plugins-base-plugins-giosrc.html
/usr/share/gtk-doc/html/gst-plugins-base-plugins-1.0/gst-plugins-base-plugins-giostreamsink.html
/usr/share/gtk-doc/html/gst-plugins-base-plugins-1.0/gst-plugins-base-plugins-giostreamsrc.html
/usr/share/gtk-doc/html/gst-plugins-base-plugins-1.0/gst-plugins-base-plugins-multifdsink.html
/usr/share/gtk-doc/html/gst-plugins-base-plugins-1.0/gst-plugins-base-plugins-multisocketsink.html
/usr/share/gtk-doc/html/gst-plugins-base-plugins-1.0/gst-plugins-base-plugins-oggaviparse.html
/usr/share/gtk-doc/html/gst-plugins-base-plugins-1.0/gst-plugins-base-plugins-oggdemux.html
/usr/share/gtk-doc/html/gst-plugins-base-plugins-1.0/gst-plugins-base-plugins-oggmux.html
/usr/share/gtk-doc/html/gst-plugins-base-plugins-1.0/gst-plugins-base-plugins-oggparse.html
/usr/share/gtk-doc/html/gst-plugins-base-plugins-1.0/gst-plugins-base-plugins-ogmaudioparse.html
/usr/share/gtk-doc/html/gst-plugins-base-plugins-1.0/gst-plugins-base-plugins-ogmtextparse.html
/usr/share/gtk-doc/html/gst-plugins-base-plugins-1.0/gst-plugins-base-plugins-ogmvideoparse.html
/usr/share/gtk-doc/html/gst-plugins-base-plugins-1.0/gst-plugins-base-plugins-opusdec.html
/usr/share/gtk-doc/html/gst-plugins-base-plugins-1.0/gst-plugins-base-plugins-opusenc.html
/usr/share/gtk-doc/html/gst-plugins-base-plugins-1.0/gst-plugins-base-plugins-parsebin.html
/usr/share/gtk-doc/html/gst-plugins-base-plugins-1.0/gst-plugins-base-plugins-playbin.html
/usr/share/gtk-doc/html/gst-plugins-base-plugins-1.0/gst-plugins-base-plugins-playbin3.html
/usr/share/gtk-doc/html/gst-plugins-base-plugins-1.0/gst-plugins-base-plugins-playsink.html
/usr/share/gtk-doc/html/gst-plugins-base-plugins-1.0/gst-plugins-base-plugins-plugin-adder.html
/usr/share/gtk-doc/html/gst-plugins-base-plugins-1.0/gst-plugins-base-plugins-plugin-alsa.html
/usr/share/gtk-doc/html/gst-plugins-base-plugins-1.0/gst-plugins-base-plugins-plugin-app.html
/usr/share/gtk-doc/html/gst-plugins-base-plugins-1.0/gst-plugins-base-plugins-plugin-audioconvert.html
/usr/share/gtk-doc/html/gst-plugins-base-plugins-1.0/gst-plugins-base-plugins-plugin-audiorate.html
/usr/share/gtk-doc/html/gst-plugins-base-plugins-1.0/gst-plugins-base-plugins-plugin-audioresample.html
/usr/share/gtk-doc/html/gst-plugins-base-plugins-1.0/gst-plugins-base-plugins-plugin-audiotestsrc.html
/usr/share/gtk-doc/html/gst-plugins-base-plugins-1.0/gst-plugins-base-plugins-plugin-cdparanoia.html
/usr/share/gtk-doc/html/gst-plugins-base-plugins-1.0/gst-plugins-base-plugins-plugin-encoding.html
/usr/share/gtk-doc/html/gst-plugins-base-plugins-1.0/gst-plugins-base-plugins-plugin-gio.html
/usr/share/gtk-doc/html/gst-plugins-base-plugins-1.0/gst-plugins-base-plugins-plugin-ivorbisdec.html
/usr/share/gtk-doc/html/gst-plugins-base-plugins-1.0/gst-plugins-base-plugins-plugin-libvisual.html
/usr/share/gtk-doc/html/gst-plugins-base-plugins-1.0/gst-plugins-base-plugins-plugin-ogg.html
/usr/share/gtk-doc/html/gst-plugins-base-plugins-1.0/gst-plugins-base-plugins-plugin-opus.html
/usr/share/gtk-doc/html/gst-plugins-base-plugins-1.0/gst-plugins-base-plugins-plugin-pango.html
/usr/share/gtk-doc/html/gst-plugins-base-plugins-1.0/gst-plugins-base-plugins-plugin-playback.html
/usr/share/gtk-doc/html/gst-plugins-base-plugins-1.0/gst-plugins-base-plugins-plugin-subparse.html
/usr/share/gtk-doc/html/gst-plugins-base-plugins-1.0/gst-plugins-base-plugins-plugin-tcp.html
/usr/share/gtk-doc/html/gst-plugins-base-plugins-1.0/gst-plugins-base-plugins-plugin-theora.html
/usr/share/gtk-doc/html/gst-plugins-base-plugins-1.0/gst-plugins-base-plugins-plugin-typefindfunctions.html
/usr/share/gtk-doc/html/gst-plugins-base-plugins-1.0/gst-plugins-base-plugins-plugin-videoconvert.html
/usr/share/gtk-doc/html/gst-plugins-base-plugins-1.0/gst-plugins-base-plugins-plugin-videorate.html
/usr/share/gtk-doc/html/gst-plugins-base-plugins-1.0/gst-plugins-base-plugins-plugin-videoscale.html
/usr/share/gtk-doc/html/gst-plugins-base-plugins-1.0/gst-plugins-base-plugins-plugin-videotestsrc.html
/usr/share/gtk-doc/html/gst-plugins-base-plugins-1.0/gst-plugins-base-plugins-plugin-volume.html
/usr/share/gtk-doc/html/gst-plugins-base-plugins-1.0/gst-plugins-base-plugins-plugin-vorbis.html
/usr/share/gtk-doc/html/gst-plugins-base-plugins-1.0/gst-plugins-base-plugins-plugin-ximagesink.html
/usr/share/gtk-doc/html/gst-plugins-base-plugins-1.0/gst-plugins-base-plugins-plugin-xvimagesink.html
/usr/share/gtk-doc/html/gst-plugins-base-plugins-1.0/gst-plugins-base-plugins-socketsrc.html
/usr/share/gtk-doc/html/gst-plugins-base-plugins-1.0/gst-plugins-base-plugins-ssaparse.html
/usr/share/gtk-doc/html/gst-plugins-base-plugins-1.0/gst-plugins-base-plugins-streamsynchronizer.html
/usr/share/gtk-doc/html/gst-plugins-base-plugins-1.0/gst-plugins-base-plugins-subparse.html
/usr/share/gtk-doc/html/gst-plugins-base-plugins-1.0/gst-plugins-base-plugins-subtitleoverlay.html
/usr/share/gtk-doc/html/gst-plugins-base-plugins-1.0/gst-plugins-base-plugins-tcpclientsink.html
/usr/share/gtk-doc/html/gst-plugins-base-plugins-1.0/gst-plugins-base-plugins-tcpclientsrc.html
/usr/share/gtk-doc/html/gst-plugins-base-plugins-1.0/gst-plugins-base-plugins-tcpserversink.html
/usr/share/gtk-doc/html/gst-plugins-base-plugins-1.0/gst-plugins-base-plugins-tcpserversrc.html
/usr/share/gtk-doc/html/gst-plugins-base-plugins-1.0/gst-plugins-base-plugins-textoverlay.html
/usr/share/gtk-doc/html/gst-plugins-base-plugins-1.0/gst-plugins-base-plugins-textrender.html
/usr/share/gtk-doc/html/gst-plugins-base-plugins-1.0/gst-plugins-base-plugins-theoradec.html
/usr/share/gtk-doc/html/gst-plugins-base-plugins-1.0/gst-plugins-base-plugins-theoraenc.html
/usr/share/gtk-doc/html/gst-plugins-base-plugins-1.0/gst-plugins-base-plugins-theoraparse.html
/usr/share/gtk-doc/html/gst-plugins-base-plugins-1.0/gst-plugins-base-plugins-timeoverlay.html
/usr/share/gtk-doc/html/gst-plugins-base-plugins-1.0/gst-plugins-base-plugins-uridecodebin.html
/usr/share/gtk-doc/html/gst-plugins-base-plugins-1.0/gst-plugins-base-plugins-urisourcebin.html
/usr/share/gtk-doc/html/gst-plugins-base-plugins-1.0/gst-plugins-base-plugins-videoconvert.html
/usr/share/gtk-doc/html/gst-plugins-base-plugins-1.0/gst-plugins-base-plugins-videorate.html
/usr/share/gtk-doc/html/gst-plugins-base-plugins-1.0/gst-plugins-base-plugins-videoscale.html
/usr/share/gtk-doc/html/gst-plugins-base-plugins-1.0/gst-plugins-base-plugins-videotestsrc.html
/usr/share/gtk-doc/html/gst-plugins-base-plugins-1.0/gst-plugins-base-plugins-volume.html
/usr/share/gtk-doc/html/gst-plugins-base-plugins-1.0/gst-plugins-base-plugins-vorbisdec.html
/usr/share/gtk-doc/html/gst-plugins-base-plugins-1.0/gst-plugins-base-plugins-vorbisenc.html
/usr/share/gtk-doc/html/gst-plugins-base-plugins-1.0/gst-plugins-base-plugins-vorbisparse.html
/usr/share/gtk-doc/html/gst-plugins-base-plugins-1.0/gst-plugins-base-plugins-vorbistag.html
/usr/share/gtk-doc/html/gst-plugins-base-plugins-1.0/gst-plugins-base-plugins-ximagesink.html
/usr/share/gtk-doc/html/gst-plugins-base-plugins-1.0/gst-plugins-base-plugins-xvimagesink.html
/usr/share/gtk-doc/html/gst-plugins-base-plugins-1.0/home.png
/usr/share/gtk-doc/html/gst-plugins-base-plugins-1.0/index.html
/usr/share/gtk-doc/html/gst-plugins-base-plugins-1.0/left-insensitive.png
/usr/share/gtk-doc/html/gst-plugins-base-plugins-1.0/left.png
/usr/share/gtk-doc/html/gst-plugins-base-plugins-1.0/right-insensitive.png
/usr/share/gtk-doc/html/gst-plugins-base-plugins-1.0/right.png
/usr/share/gtk-doc/html/gst-plugins-base-plugins-1.0/style.css
/usr/share/gtk-doc/html/gst-plugins-base-plugins-1.0/up-insensitive.png
/usr/share/gtk-doc/html/gst-plugins-base-plugins-1.0/up.png

%files lib
%defattr(-,root,root,-)
/usr/lib64/*.so.*
/usr/lib64/gstreamer-1.0/libgstadder.so
/usr/lib64/gstreamer-1.0/libgstalsa.so
/usr/lib64/gstreamer-1.0/libgstapp.so
/usr/lib64/gstreamer-1.0/libgstaudioconvert.so
/usr/lib64/gstreamer-1.0/libgstaudiorate.so
/usr/lib64/gstreamer-1.0/libgstaudioresample.so
/usr/lib64/gstreamer-1.0/libgstaudiotestsrc.so
/usr/lib64/gstreamer-1.0/libgstencodebin.so
/usr/lib64/gstreamer-1.0/libgstgio.so
/usr/lib64/gstreamer-1.0/libgstogg.so
/usr/lib64/gstreamer-1.0/libgstpango.so
/usr/lib64/gstreamer-1.0/libgstplayback.so
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

%files locales -f gst-plugins-base-1.0.lang 
%defattr(-,root,root,-)

