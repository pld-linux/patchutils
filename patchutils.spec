Summary:	Patchutils is a small collection of programs that operate on patch files
Summary(pl):	Kolekcja ma³ych programów operuj±cych na plikach patch
Name:		patchutils
Version:	0.2.11
Release:	3
License:	GPL
Group:		Applications/Text
Source0:	http://cyberelk.net/tim/data/patchutils/stable/%{name}-%{version}.tar.gz
Patch0:		%{name}-DESTDIR.patch
Patch1:		%{name}-fixcvsdiff.patch
Patch2:		%{name}-context.patch
URL:		http://cyberelk.net/tim/patchutils/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	diffutils
BuildRequires:	patch
Requires:	diffutils
Requires:	patch
Provides:	interdiff
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Obsoletes:	interdiff

%description
Interdiff generates an incremental patch from two patches against a
common source. For example, if you have applied a pre-patch to a
source tree, and wish to apply another pre-patch (which is against the
same original source tree), you can use interdiff to generate the
patch that you need to apply. You can also use this to review changes
between two pre-patches.

Combinediff generates a single patch from two incremental patches,
allowing you to merge patches together. The resulting patch file only
alters each file once.

Filterdiff will select the portions of a patch file that apply to
files matching (or, alternatively, not matching) a shell wildcard.

Fixcvsdiff is for correcting the output of 'cvs diff'.

Rediff corrects hand-edited patches, by comparing the original patch
with the modified one and adjusting the offsets and counts.

Lsdiff displays a short listing of affected files in a patch file,
along with (optionally) the line numbers of the start of each patch.

Splitdiff separates out patches from a patch file so that each new
patch file only alters any given file once. In this way, a file
containing several incremental patches can be split into individual
incremental patches.

Grepdiff displays a list of the files modified by a patch where the
patch contains a given regular expression.

%description -l pl
Interdiff generuje inkrementalne patche z dwóch patchy stworzonych w
stosunku do jednego ¼ród³a.

Combinediff generuje pojedyñczy patch z dwóch inkrementalnych patchy
pozwalaj±c na ich ³±czenie. Wygenerowany patch modyfikuje pliki
jedynie jednokrotnie.

Filterdiff wybierze fragmenty patcha modyfikuj±ce pliki pasuj±ce (lub
nie pasuj±ce) do wzorca shella.

Fixcvsdiff s³u¿y do poprawiania plików wygenerowanych przez `cvs
diff'.

Rediff poprawia rêcznie-edytowane patche poprzez porównanie
oryginalnego patcha ze zmodyfikowanym i poprawianie przesuniêæ i
zliczeñ.

Lsdiff wy¶wietla krótk± listê plików, które patch modyfikuje wraz z
(opcjonalnie) numerami linii ka¿dej zmiany.

Splitdiff dzieli patch na wiêcej patchy tak, ¿e poszczególne patche
modyfikuj± jedynie okre¶lony plik jednokrotnie. W ten sposób plik
zawieraj±cy kilka inkrementalnych zmian mo¿e byæ zamieniony w kilka
inkrementalnych ³at.

Grepdiff wy¶wietla listê plików modyfikowanych przez patch gdzie patch
zawiera okre¶lone wyra¿enie regularne.

%prep
%setup -q
%patch0 -p1
%patch1 -p0
%patch2 -p1

%build
rm -f missing
aclocal
autoconf
automake -a -c -f
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

gzip -9nf NEWS README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man?/*
