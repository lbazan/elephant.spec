%global pypi_name elephant

Name:           python-%{pypi_name}
Version:        0.6.2
Release:        1%{?dist}
Summary:        Elephant is a package for analysis of electrophysiology data in Python

License:        BSD
URL:            http://neuralensemble.org/elephant
Source0:        %{url}/archive/v%{version}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch
 
BuildRequires:	python3-devel
BuildRequires:	python3dist(neo)
BuildRequires:	python3dist(nose)
BuildRequires:	python3dist(numpy)
BuildRequires:	python3dist(numpydoc)
BuildRequires:	python3dist(pandas)
BuildRequires:	python3dist(quantities)
BuildRequires:	python3dist(scikit-learn)
BuildRequires:	python3dist(scipy)
BuildRequires:	python3dist(setuptools)
BuildRequires:	python3dist(six)
BuildRequires:	python3dist(sphinx)
BuildRequires: 	python3-sphinx_rtd_theme
BuildRequires:	python3dist(sphinx-gallery)
BuildRequires:	python3dist(sphinxcontrib-bibtex)

%description
Elephant - Electrophysiology Analysis Toolkit Elephant is a package for the
analysis of neurophysiology data, based on Neo.

%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}
 
Requires:	python3dist(neo)
Requires:	python3dist(nose)
Requires:	python3dist(numpy)
Requires:	python3dist(numpydoc)
Requires:	python3dist(pandas)
Requires:	python3dist(quantities)
Requires:	python3dist(scikit-learn)
Requires:	python3dist(scipy)
Requires:	python3dist(six)
Requires:	python3dist(sphinx)
Requires:	python3-sphinx_rtd_theme
Requires:	python3dist(sphinx-gallery)
Requires:	python3dist(sphinxcontrib-bibtex)

%description -n python3-%{pypi_name}
Elephant - Electrophysiology Analysis Toolkit Elephant is a package for the
analysis of neurophysiology data, based on Neo.

%package -n python-%{pypi_name}-doc
Summary:        elephant documentation
%description -n python-%{pypi_name}-doc
Documentation for elephant

%prep
%autosetup -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%build
%py3_build
# generate html docs 
PYTHONPATH=${PWD} sphinx-build-3 doc html
# remove the sphinx-build leftovers
rm -rf html/.{doctrees,buildinfo}

%install
%py3_install

%check
%{__python3} setup.py test

%files -n python3-%{pypi_name}
%license LICENSE.txt elephant/spade_src/LICENSE
%doc README.rst elephant/current_source_density_src/README.md
%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/%{pypi_name}-%{version}-py?.?.egg-info

%files -n python-%{pypi_name}-doc
%doc html
%license LICENSE.txt elephant/spade_src/LICENSE

%changelog
* Wed May 29 2019 Luis Bazan <lbazan@fedoraproject.org - 0.6.2-1
- Initial package.
