%global tl_name listbib
%global tl_revision 29349

Name:		texlive-%{tl_name}
Epoch:		1
Version:	2.2
Release:	%{tl_revision}.1
Summary:	Lists contents of BibTeX files
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/listbib
License:	gpl
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/listbib.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/listbib.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/listbib.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Requires:	texlive(listbib.bin)
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
Generates listings of bibliographic data bases in BibTeX format -- for
example for archival purposes. Included is a listbib.bst which is better
suited for this purpose than the standard styles.

