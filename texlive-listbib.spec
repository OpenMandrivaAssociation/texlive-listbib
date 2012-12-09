# revision 26126
# category Package
# catalog-ctan /macros/latex/contrib/listbib
# catalog-date 2012-04-21 20:14:11 +0200
# catalog-license gpl
# catalog-version 2.2
Name:		texlive-listbib
Version:	2.2
Release:	3
Summary:	Lists contents of BibTeX files
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/listbib
License:	GPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/listbib.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/listbib.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/listbib.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea
Provides:	texlive-listbib.bin = %{EVRD}

%description
Generates listings of bibliographic data bases in BibTeX format
-- for example for archival purposes. Included is a listbib.bst
which is better suited for this purpose than the standard
styles.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_bindir}/listbib
%{_texmfdistdir}/bibtex/bst/listbib/listbib.bst
%{_texmfdistdir}/scripts/listbib/listbib
%{_texmfdistdir}/tex/latex/listbib/listbib.cfg
%{_texmfdistdir}/tex/latex/listbib/listbib.sty
%{_texmfdistdir}/tex/latex/listbib/listbib.tex
%doc %{_texmfdistdir}/doc/latex/listbib/listbib-doc.pdf
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
mkdir -p %{buildroot}%{_bindir}
pushd %{buildroot}%{_bindir}
    ln -sf %{_texmfdistdir}/scripts/listbib/listbib listbib
popd
mkdir -p %{buildroot}%{_datadir}
cp -fpar texmf-dist %{buildroot}%{_datadir}


%changelog
* Mon Jun 11 2012 Paulo Andrade <pcpa@mandriva.com.br> 2.2-3
+ Revision: 804923
- Update to latest release.

* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 2.2-2
+ Revision: 753318
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 2.2-1
+ Revision: 718865
- texlive-listbib
- texlive-listbib
- texlive-listbib
- texlive-listbib

