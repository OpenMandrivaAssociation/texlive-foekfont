%global tl_name foekfont
%global tl_revision 15878

Name:		texlive-%{tl_name}
Version:	%{tl_revision}
Release:	1
Summary:	The title font of the Mads Fok magazine
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/fonts/foekfont
License:	gpl
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/foekfont.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/foekfont.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Requires:	texlive-tlpkg
Provides:	texlive(%{tl_name}) = %{version}

%description
The bundle provides an Adobe Type 1 font, and LaTeX support for its use.
The magazine web site shows the font in use in a few places.


%install -a
mkdir -p %{buildroot}%{_texmf_updmap_d}
cat > %{buildroot}%{_texmf_updmap_d}/%{tl_name} <<'TL_DROPIN_EOF'
# from foekfont:
Map foekfont.map
TL_DROPIN_EOF
