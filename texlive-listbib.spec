Name:		texlive-listbib
Version:	29349
Release:	2
Summary:	Lists contents of BibTeX files
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/listbib
License:	GPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/listbib.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/listbib.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/listbib.source.r%{version}.tar.xz
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
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_bindir}
pushd %{buildroot}%{_bindir}
ln -sf %{_texmfdistdir}/scripts/listbib/listbib listbib
popd
mkdir -p %{buildroot}%{_datadir}
cp -fpar texmf-dist %{buildroot}%{_datadir}
