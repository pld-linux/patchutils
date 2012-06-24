%define _pre pre3
Summary:	Patchutils is a small collection of programs that operate on patch files
Summary(pl):	Kolekcja ma�ych program�w operuj�cych na plikach patch
Summary(pt_BR):	Utilit�rio para Patches
Summary(ru):	����� ������������ ��� ������ � patch-�������
Summary(uk):	��¦� ���������Ԧ� ��� ������ � patch-�������
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
Interdiff generuje inkrementalne patche z dw�ch patchy stworzonych w
stosunku do jednego �r�d�a.

Combinediff generuje pojedy�czy patch z dw�ch inkrementalnych patchy
pozwalaj�c na ich ��czenie. Wygenerowany patch modyfikuje pliki
jedynie jednokrotnie.

Filterdiff wybierze fragmenty patcha modyfikuj�ce pliki pasuj�ce (lub
nie pasuj�ce) do wzorca shella.

Fixcvsdiff s�u�y do poprawiania plik�w wygenerowanych przez `cvs
diff'.

Rediff poprawia r�cznie-edytowane patche poprzez por�wnanie
oryginalnego patcha ze zmodyfikowanym i poprawianie przesuni�� i
zlicze�.

Lsdiff wy�wietla kr�tk� list� plik�w, kt�re patch modyfikuje wraz z
(opcjonalnie) numerami linii ka�dej zmiany.

Splitdiff dzieli patch na wi�cej patchy tak, �e poszczeg�lne patche
modyfikuj� jedynie okre�lony plik jednokrotnie. W ten spos�b plik
zawieraj�cy kilka inkrementalnych zmian mo�e by� zamieniony w kilka
inkrementalnych �at.

Grepdiff wy�wietla list� plik�w modyfikowanych przez patch gdzie patch
zawiera okre�lone wyra�enie regularne.

%description -l pt_BR
Interdiff gera um patch incrementado de dois patches de uma fonte
comum. Por exemplo, se voc� aplicou um pre-patch (na mesma �rvore
original), voc� pode usar o interdiff para gerar o patch que voc�
deseja aplicar. Voc� tamb�m pode us�-lo para rever as mudan�as entre
dois pre-patches.

Combinediff gera um �nico patch a partir de dois patches
incrementados, permitindo consolidar os patches em um. O patch
resultante altera uma vez apenas cada arquivo.

Filterdiff selecionar� as partes dos patches que se aplicam a arquivos
que batem com uma string do shell (ou n�o, se desejado).

Fixcvsdiff serve para corrigir a sa�da do 'cvsdiff'.

Rediff corrige patches escritos manualmente, comparando o patch
original com o modificado e ajustando os contadores e os balan�os.

Lsdiff mostra uma pequena lista dos arquivos afetados em um patch,
junto com (opcionalmente) o n�mero de linhas do in�cio de cada patch.

Splitdiff separa patches de um arquivo de patch assim cada novo patch
altera um arquivo por vez. Desta forma, um arquivo contendo v�rias
adi��es pode ser dividido em patches individuais.

Grepdiff mostra uma lista de arquivos modificados por um patch no qual
o patch cont�m a express�o regular dada.

%description -l ru
Patchutils �������� ��������� �������: interdiff, combinediff,
filterdiff, fixcvsdiff, rediff, lsdiff �� splitdiff. ��� ������
interdiff ����� ��������� ��������������� patch ����� �����
patch-�������, ������������ � ������ � ���� �� ������ ��������
�������. combinediff ������� ������������ ���� ����������� �� ����
��������������� patch-������. filterdiff - ��� �������� �� ������
patch-������ �������� patch'�� �� ������ �������� ���� ��������������
������. lsdiff ���� ������ ������, ���������� ��� ����������
patch-�����. rediff ������������ patch-�����, ������� ���������������
�������.

%description -l uk
Patchutils ͦ����� ������Φ ���̦��: interdiff, combinediff,
filterdiff, fixcvsdiff, rediff, lsdiff �� splitdiff. �� ���������
interdiff ����� ���������� ��������������� patch ͦ� �����
patch-�������, �� צ��������� �� ������ � ���� � ������ ��Ȧ����
����Ԧ�. combinediff ������� ������������ ���� ���¦������� � ����
��������������� patch-���̦�. filterdiff - ��� ��������� � ������
patch-���̦� �����Ҧ���� patch'�� �� ����צ �����Φ� ���� ���̦�, ��
����Ʀ�������. lsdiff ��� ����̦� ���̦�, �� �ͦ������� ���
"���������Φ" patch-�����. rediff ������դ patch-�����, �˦
������������ ������.

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
