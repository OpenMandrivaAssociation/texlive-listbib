Name:		texlive-listbib
Version:	2.2
Release:	1
Summary:	Lists contents of BibTeX files
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/listbib
License:	GPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/listbib.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/listbib.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/listbib.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3
Conflicts:	texlive-source <= 20110705-3

%description
Generates listings of bibliographic data bases in BibTeX format
-- for example for archival purposes. Included is a listbib.bst
which is better suited for this purpose than the standard
styles.

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
%{_texmfdistdir}/tex/latex/listbib/listbib.cfg
%{_texmfdistdir}/tex/latex/listbib/listbib.sty
%doc %{_texmfdistdir}/doc/latex/listbib/listbib
%doc %{_texmfdistdir}/doc/latex/listbib/listbib-doc.pdf
%doc %{_texmfdistdir}/doc/latex/listbib/listbib.doc
%doc %{_texmfdistdir}/doc/latex/listbib/listbib.tex
#- source
%doc %{_texmfdistdir}/source/latex/listbib/listbib-doc.drv
%doc %{_texmfdistdir}/source/latex/listbib/listbib.drv
%doc %{_texmfdistdir}/source/latex/listbib/listbib.dtx
%doc %{_texmfdistdir}/source/latex/listbib/listbib.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
