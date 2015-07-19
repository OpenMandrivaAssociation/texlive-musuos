# revision 24857
# category Package
# catalog-ctan /macros/latex/contrib/musuos
# catalog-date 2011-12-07 16:44:29 +0100
# catalog-license lppl
# catalog-version 1.1c
Name:		texlive-musuos
Version:	1.1c
Release:	11
Summary:	Typeset papers for the department of music, Osnabruck
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/musuos
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/musuos.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/musuos.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/musuos.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package provides a LaTeX class for typesetting term papers
at the institute of music and musicology of the University of
Osnabruck, Germany, according to the specifications of Prof.
Stefan Hahnheide. A biblatex style is provided.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/musuos/musuos.cls
%doc %{_texmfdistdir}/doc/latex/musuos/README
%doc %{_texmfdistdir}/doc/latex/musuos/musuos-doc.ist
%doc %{_texmfdistdir}/doc/latex/musuos/musuos.pdf
#- source
%doc %{_texmfdistdir}/source/latex/musuos/musuos.dtx
%doc %{_texmfdistdir}/source/latex/musuos/musuos.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}


%changelog
* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 1.1c-3
+ Revision: 754238
- Rebuild to reduce used resources

* Mon Dec 26 2011 Paulo Andrade <pcpa@mandriva.com.br> 1.1c-2
+ Revision: 745303
- texlive-musuos

* Sat Dec 17 2011 Paulo Andrade <pcpa@mandriva.com.br> 1.1c-1
+ Revision: 743313
- texlive-musuos

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 1.1a-1
+ Revision: 719091
- texlive-musuos
- texlive-musuos
- texlive-musuos
- texlive-musuos

