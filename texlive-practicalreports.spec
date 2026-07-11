%global tl_name practicalreports
%global tl_revision 52312

Name:		texlive-%{tl_name}
Epoch:		1
Version:	2.0.3
Release:	%{tl_revision}.1
Summary:	Some macros for writing practical reports
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/practicalreports
License:	lppl1.3c
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/practicalreports.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/practicalreports.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This package provides a handful of macros for writing up science
practical reports.

