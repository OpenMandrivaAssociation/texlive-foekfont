Name:		texlive-foekfont
Version:	15878
Release:	2
Summary:	The title font of the Mads Fok magazine
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/fonts/foekfont
License:	GPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/foekfont.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/foekfont.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The bundle provides an Adobe Type 1 font, and LaTeX support for
its use. The magazine web site shows the font in use in a few
places.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/fonts/map/dvips/foekfont/foekfont.map
%{_texmfdistdir}/fonts/tfm/public/foekfont/foekfont.tfm
%{_texmfdistdir}/fonts/type1/public/foekfont/FoekFont.pfb
%{_texmfdistdir}/tex/latex/foekfont/foekfont.sty
%{_texmfdistdir}/tex/latex/foekfont/ot1foekfont.fd
%{_texmfdistdir}/tex/latex/foekfont/t1foekfont.fd
%doc %{_texmfdistdir}/doc/latex/foekfont/FoekFont.sfd
%doc %{_texmfdistdir}/doc/latex/foekfont/README
%doc %{_texmfdistdir}/doc/latex/foekfont/foekfont.pdf
%doc %{_texmfdistdir}/doc/latex/foekfont/foekfont.tex

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar fonts tex doc %{buildroot}%{_texmfdistdir}
