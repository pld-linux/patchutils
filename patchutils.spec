%define _pre pre3
Summary:	Patchutils is a small collection of programs that operate on patch files
Summary(pl):	Kolekcja maЁych programСw operuj╠cych na plikach patch
Summary(pt_BR):	UtilitАrio para Patches
Summary(ru):	Набор инструментов для работы с patch-файлами
Summary(uk):	Наб╕р ╕нструмент╕в для роботи з patch-файлами
Name:		patchutils
Version:	0.2.25
Release:	0.%{_pre}.1
License:	GPL
Group:		Applications/Text
Source0:	http://cyberelk.net/tim/data/patchutils/stable/%{name}-%{version}%{_pre}.tar.bz2
# Source0-md5:	81210503d7c6a316642e0fde4b18c037
Patch1:		%{name}-fixcvsdiff.patch
URL:		http://cyberelk.net/tim/patchutils/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	diffutils
BuildRequires:	patch
Requires:	diffutils
Requires:	patch
Provides:	interdiff
Obsoletes:	interdiff
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

%description -l pl
Interdiff generuje inkrementalne patche z dwСch patchy stworzonych w
stosunku do jednego ╪rСdЁa.

Combinediff generuje pojedyЯczy patch z dwСch inkrementalnych patchy
pozwalaj╠c na ich Ё╠czenie. Wygenerowany patch modyfikuje pliki
jedynie jednokrotnie.

Filterdiff wybierze fragmenty patcha modyfikuj╠ce pliki pasuj╠ce (lub
nie pasuj╠ce) do wzorca shella.

Fixcvsdiff sЁu©y do poprawiania plikСw wygenerowanych przez `cvs
diff'.

Rediff poprawia rЙcznie-edytowane patche poprzez porСwnanie
oryginalnego patcha ze zmodyfikowanym i poprawianie przesuniЙФ i
zliczeЯ.

Lsdiff wy╤wietla krСtk╠ listЙ plikСw, ktСre patch modyfikuje wraz z
(opcjonalnie) numerami linii ka©dej zmiany.

Splitdiff dzieli patch na wiЙcej patchy tak, ©e poszczegСlne patche
modyfikuj╠ jedynie okre╤lony plik jednokrotnie. W ten sposСb plik
zawieraj╠cy kilka inkrementalnych zmian mo©e byФ zamieniony w kilka
inkrementalnych Ёat.

Grepdiff wy╤wietla listЙ plikСw modyfikowanych przez patch gdzie patch
zawiera okre╤lone wyra©enie regularne.

%description -l pt_BR
Interdiff gera um patch incrementado de dois patches de uma fonte
comum. Por exemplo, se vocЙ aplicou um pre-patch (na mesma Аrvore
original), vocЙ pode usar o interdiff para gerar o patch que vocЙ
deseja aplicar. VocЙ tambИm pode usА-lo para rever as mudanГas entre
dois pre-patches.

Combinediff gera um Зnico patch a partir de dois patches
incrementados, permitindo consolidar os patches em um. O patch
resultante altera uma vez apenas cada arquivo.

Filterdiff selecionarА as partes dos patches que se aplicam a arquivos
que batem com uma string do shell (ou nЦo, se desejado).

Fixcvsdiff serve para corrigir a saМda do 'cvsdiff'.

Rediff corrige patches escritos manualmente, comparando o patch
original com o modificado e ajustando os contadores e os balanГos.

Lsdiff mostra uma pequena lista dos arquivos afetados em um patch,
junto com (opcionalmente) o nЗmero de linhas do inМcio de cada patch.

Splitdiff separa patches de um arquivo de patch assim cada novo patch
altera um arquivo por vez. Desta forma, um arquivo contendo vАrias
adiГУes pode ser dividido em patches individuais.

Grepdiff mostra uma lista de arquivos modificados por um patch no qual
o patch contИm a expressЦo regular dada.

%description -l ru
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

%description -l uk
Patchutils м╕стить наступн╕ утил╕ти: interdiff, combinediff,
filterdiff, fixcvsdiff, rediff, lsdiff та splitdiff. За допомогою
interdiff можна створювати ╕нкрементальний patch м╕ж двома
patch-файлами, що в╕дносяться до одного й того ж дерева вих╕дних
текст╕в. combinediff створю╓ кумулятивний файл розб╕жностей з двох
╕нкрементальних patch-файл╕в. filterdiff - для видалення з набору
patch-файл╕в непотр╕бних patch'╕в на основ╕ шаблон╕в ╕мен файл╕в, що
модиф╕куються. lsdiff да╓ перел╕к файл╕в, що зм╕нюються при
"прикладанн╕" patch-файлу. rediff коректу╓ patch-файли, як╕
редагувались вручну.

%prep
%setup -q -n %{name}-%{version}%{_pre}
%patch1 -p0

%build
rm -f missing
%{__aclocal}
%{__autoconf}
%{__automake}
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README TODO
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man?/*
