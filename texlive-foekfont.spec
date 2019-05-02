# revision 15878
# category Package
# catalog-ctan /fonts/foekfont
# catalog-date 2007-02-27 14:19:10 +0100
# catalog-license gpl
# catalog-version undef
Name:		texlive-foekfont
Version:	20190228
Release:	1
Summary:	The title font of the Mads Fok magazine
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/fonts/foekfont
License:	GPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/foekfont.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/foekfont.doc.tar.xz
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
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar fonts tex doc %{buildroot}%{_texmfdistdir}


%changelog
* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 20070227-2
+ Revision: 752005
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 20070227-1
+ Revision: 718475
- texlive-foekfont
- texlive-foekfont
- texlive-foekfont
- texlive-foekfont

