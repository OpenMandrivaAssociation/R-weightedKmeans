%global packname  weightedKmeans
%global rlibdir  %{_libdir}/R/library

Name:             R-%{packname}
Version:          1.2.0
Release:          1
Summary:          Weighted KMeans Clustering
Group:            Sciences/Mathematics
License:          GPLv3+
URL:              https://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz

Requires:         R-lattice R-latticeExtra R-clv 


BuildRequires:    R-devel Rmath-devel texlive-collection-latex R-lattice R-latticeExtra R-clv


%description
Entropy weighted kmeans (ewkm) is a weighted subspace clustering algorithm
that is well suited to very high dimensional data. Weights are calculated
as the importance of a variable with regard to cluster membership. The
feature group weighted kmenas (fgkm) extends this concept by grouping
features and weighting the group in addition to weihgting individual

%prep
%setup -q -c -n %{packname}

%build

%install
mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%check
%{_bindir}/R CMD check %{packname}

%files
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/html
%doc %{rlibdir}/%{packname}/DESCRIPTION
%doc %{rlibdir}/%{packname}/LICENSE
%doc %{rlibdir}/%{packname}/ChangeLog
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/help
%{rlibdir}/%{packname}/data
%{rlibdir}/%{packname}/libs
