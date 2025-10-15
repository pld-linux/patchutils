Summary:	Patchutils is a small collection of programs that operate on patch files
Summary(pl.UTF-8):	Kolekcja małych programów operujących na plikach patch
Summary(pt_BR.UTF-8):	Utilitário para Patches
Summary(ru.UTF-8):	Набор инструментов для работы с patch-файлами
Summary(uk.UTF-8):	Набір інструментів для роботи з patch-файлами
Name:		patchutils
Version:	0.4.4
Release:	1
License:	GPL v2+
Group:		Applications/Text
# also http://cyberelk.net/tim/data/patchutils/stable/
Source0:	https://github.com/twaugh/patchutils/releases/download/%{version}/%{name}-%{version}.tar.xz
# Source0-md5:	7781c0d48979d2dc2c7cfeec831b5232
Patch0:		%{name}-fixcvsdiff.patch
URL:		http://cyberelk.net/tim/patchutils/
BuildRequires:	autoconf >= 2.50
BuildRequires:	automake >= 1.6
BuildRequires:	pcre2-posix-devel
BuildRequires:	perl-base
BuildRequires:	tar >= 1:1.22
BuildRequires:	xmlto
BuildRequires:	xz
Requires:	diffutils
Requires:	patch >= 2.1
Provides:	interdiff
Obsoletes:	interdiff
Conflicts:	bash-completion < 1:2.11-3
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

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

%description -l pl.UTF-8
Interdiff generuje przyrostowe patche z dwóch patchy stworzonych w
stosunku do jednego źródła.

Combinediff generuje pojedynczy patch z dwóch przyrostowych patchy
pozwalając na ich łączenie. Wygenerowany patch modyfikuje pliki
jedynie jednokrotnie.

Filterdiff wybierze fragmenty patcha modyfikujące pliki pasujące (lub
nie pasujące) do wzorca shella.

Fixcvsdiff służy do poprawiania plików wygenerowanych przez `cvs
diff'.

Rediff poprawia ręcznie modyfikowane patche poprzez porównanie
oryginalnego patcha ze zmodyfikowanym i poprawianie przesunięć i
zliczeń.

Lsdiff wyświetla krótką listę plików, które patch modyfikuje wraz z
(opcjonalnie) numerami linii każdej zmiany.

Splitdiff dzieli patch na więcej patchy tak, że poszczególne patche
modyfikują jedynie określony plik jednokrotnie. W ten sposób plik
zawierający kilka przyrostowych zmian może być zamieniony w kilka
przyrostowych łat.

Grepdiff wyświetla listę plików modyfikowanych przez patch gdzie patch
zawiera określone wyrażenie regularne.

%description -l pt_BR.UTF-8
Interdiff gera um patch incrementado de dois patches de uma fonte
comum. Por exemplo, se você aplicou um pre-patch (na mesma árvore
original), você pode usar o interdiff para gerar o patch que você
deseja aplicar. Você também pode usá-lo para rever as mudanças entre
dois pre-patches.

Combinediff gera um único patch a partir de dois patches
incrementados, permitindo consolidar os patches em um. O patch
resultante altera uma vez apenas cada arquivo.

Filterdiff selecionará as partes dos patches que se aplicam a arquivos
que batem com uma string do shell (ou não, se desejado).

Fixcvsdiff serve para corrigir a saída do 'cvsdiff'.

Rediff corrige patches escritos manualmente, comparando o patch
original com o modificado e ajustando os contadores e os balanços.

Lsdiff mostra uma pequena lista dos arquivos afetados em um patch,
junto com (opcionalmente) o número de linhas do início de cada patch.

Splitdiff separa patches de um arquivo de patch assim cada novo patch
altera um arquivo por vez. Desta forma, um arquivo contendo várias
adições pode ser dividido em patches individuais.

Grepdiff mostra uma lista de arquivos modificados por um patch no qual
o patch contém a expressão regular dada.

%description -l ru.UTF-8
Patchutils содержит следующие утилиты: interdiff, combinediff,
filterdiff, fixcvsdiff, rediff, lsdiff та splitdiff. При помощи
interdiff можно создавать инкрементальный patch между двумя
patch-файлами, относящимися к одному и тому же дереву исходных
текстов. combinediff создает кумулятивный файл расхождений из двух
инкрементальных patch-файлов. filterdiff - для удаления из набора
patch-файлов ненужных patch'ей на основе шаблонов имен модифицируемых
файлов. lsdiff дает список файлов, изменяемых при применении
patch-файла. rediff корректирует patch-файлы, которые редактировались
вручную.

%description -l uk.UTF-8
Patchutils містить наступні утиліти: interdiff, combinediff,
filterdiff, fixcvsdiff, rediff, lsdiff та splitdiff. За допомогою
interdiff можна створювати інкрементальний patch між двома
patch-файлами, що відносяться до одного й того ж дерева вихідних
текстів. combinediff створює кумулятивний файл розбіжностей з двох
інкрементальних patch-файлів. filterdiff - для видалення з набору
patch-файлів непотрібних patch'ів на основі шаблонів імен файлів, що
модифікуються. lsdiff дає перелік файлів, що змінюються при
"прикладанні" patch-файлу. rediff коректує patch-файли, які
редагувались вручну.

%prep
%setup -q
%patch -P0 -p0

%build
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--with-pcre2
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# conflict with subversion-tools

%{__rm} $RPM_BUILD_ROOT%{_bindir}/svndiff

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS BUGS ChangeLog NEWS README.md TODO
%attr(755,root,root) %{_bindir}/combinediff
%attr(755,root,root) %{_bindir}/dehtmldiff
%attr(755,root,root) %{_bindir}/editdiff
%attr(755,root,root) %{_bindir}/espdiff
%attr(755,root,root) %{_bindir}/filterdiff
%attr(755,root,root) %{_bindir}/fixcvsdiff
%attr(755,root,root) %{_bindir}/flipdiff
%attr(755,root,root) %{_bindir}/gitdiff
%attr(755,root,root) %{_bindir}/gitdiffview
%attr(755,root,root) %{_bindir}/gitshow
%attr(755,root,root) %{_bindir}/gitshowview
%attr(755,root,root) %{_bindir}/grepdiff
%attr(755,root,root) %{_bindir}/interdiff
%attr(755,root,root) %{_bindir}/lsdiff
%attr(755,root,root) %{_bindir}/patchview
%attr(755,root,root) %{_bindir}/recountdiff
%attr(755,root,root) %{_bindir}/rediff
%attr(755,root,root) %{_bindir}/splitdiff
%attr(755,root,root) %{_bindir}/svndiffview
%attr(755,root,root) %{_bindir}/unwrapdiff
%{_mandir}/man1/combinediff.1*
%{_mandir}/man1/dehtmldiff.1*
%{_mandir}/man1/editdiff.1*
%{_mandir}/man1/espdiff.1*
%{_mandir}/man1/filterdiff.1*
%{_mandir}/man1/fixcvsdiff.1*
%{_mandir}/man1/flipdiff.1*
%{_mandir}/man1/gitdiff.1*
%{_mandir}/man1/gitdiffview.1*
%{_mandir}/man1/gitshow.1*
%{_mandir}/man1/gitshowview.1*
%{_mandir}/man1/grepdiff.1*
%{_mandir}/man1/interdiff.1*
%{_mandir}/man1/lsdiff.1*
%{_mandir}/man1/patchview.1*
%{_mandir}/man1/recountdiff.1*
%{_mandir}/man1/rediff.1*
%{_mandir}/man1/splitdiff.1*
%{_mandir}/man1/svndiff.1*
%{_mandir}/man1/svndiffview.1*
%{_mandir}/man1/unwrapdiff.1*
%{bash_compdir}/combinediff
%{bash_compdir}/dehtmldiff
%{bash_compdir}/editdiff
%{bash_compdir}/espdiff
%{bash_compdir}/filterdiff
%{bash_compdir}/fixcvsdiff
%{bash_compdir}/flipdiff
%{bash_compdir}/gitdiff
%{bash_compdir}/gitdiffview
%{bash_compdir}/grepdiff
%{bash_compdir}/interdiff
%{bash_compdir}/lsdiff
%{bash_compdir}/patchview
%{bash_compdir}/recountdiff
%{bash_compdir}/rediff
%{bash_compdir}/splitdiff
%{bash_compdir}/svndiff
%{bash_compdir}/svndiffview
%{bash_compdir}/unwrapdiff
