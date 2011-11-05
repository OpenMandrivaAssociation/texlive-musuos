# revision 24201
# category Package
# catalog-ctan /macros/latex/contrib/musuos
# catalog-date 2011-10-04 09:01:45 +0200
# catalog-license lppl
# catalog-version 1.1a
Name:		texlive-musuos
Version:	1.1a
Release:	1
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
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3
Conflicts:	texlive-source <= 20110705-3

%description
The package provides a LaTeX class for typesetting term papers
at the institute of music and musicology of the University of
Osnabruck, Germany, according to the specifications of Prof.
Stefan Hahnheide. A biblatex style is provided.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
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
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
