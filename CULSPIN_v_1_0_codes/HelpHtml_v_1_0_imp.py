#!/usr/bin/env python
# -*- coding: cp1252 -*- 

# main window

'''
Created on 30/05/2009

@author: Chachy
'''
import wx
import wx.html
import os, sys



class MyHtmlFrame(wx.Frame):
    def __init__(self, parent, title, pag, raiz_images= os.getcwd()+"\\"):
        wx.Frame.__init__(self, parent, -1, title,pos=(0,30),size=(950,500))
        os.chdir(raiz_images)
        html = wx.html.HtmlWindow(self,-1, pos=(0,30), size=(900,500))
        html.SetBackgroundColour(wx.Colour(160,160,255, 250))
        if pag == 'page1':
            page = """
<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN">
<html>
<head>
  <meta 
 content="text/html; charset=ISO-8859-1"
 http-equiv="content-type">
  <title>Quick help about Input file format</title>
</head>
<body bgcolor= #EFFFFF>
<font face = \"times new roman\" color=#06159A size=4><i><b>
&nbsp;&nbsp;&nbsp;&nbsp;<li>I- Input file(s) format:</b></i></font>
<font face = \"times new roman\" colo=\"black\" size=4><i> this spint control box allows to select, among five input file 
format, the one that corresponds to our data.</i></font></li><br>
                                <br>
                                <div align=center>
                                <img style="width: 599px; height: 229px;" alt=""
                                src='images/inputfileformat.jpg'>
                                </div>
    <BLOCKQUOTE>
        <font face = \"times new roman\" color=#06159A size=4><b><i>
        a) Text file by rows:</i></b></font>
        <font face = \"times new roman\" colo=\"black\" size=4><i>in this format each row is a case.</i></font></li><br>
        <br>
            <ul><li><font face = \"times new roman\" colo=\"black\" size=4><i><b>Letter sequences:</b></i></font></li><br>
            <br>
            <font size=2><samp>Cha[01]
            GDDGGGGGDGGGDGDDGGGDGGGDGDGGDGDDDDGGGGGDGGDDGGGGGGGGGGGGKKKKKAAAKKAKKKKAAK<br>
            Cha[02]
            DDGGDGGGGGGGGDGGGDGDDDDDDGGGGGDGGDDGGGGGGGGGGGGGGGGKKKKKAAAKKAKKKKK<br>
            Cha[03]
            GDGGDGGGGGGGGDGGGDGDDGGGDGGGDGDGGDGDDDDGGGGGDGGDDGGGGGGGGGGKKKKKAAAKKAKKKKKKAAA</samp></font><br>
            <li><font face = \"times new roman\" size=4><i><b>Numerics sequences:</b></i></font><br>
            <br>
            <font size=2><samp>Cha[01]
            -7.86E-05 2.18E-07 9.60E-05 0.00036601 0.0008102 0.00142856
            0.00222112 0.00318787 0.00432881<br>
            Cha[02] 2.18E-07 9.60E-05
            0.00036601 0.0008102 0.00142856 0.00222112
            0.00318787 0.00432881 -7.86E-05</small><br>
            Cha[03] 9.60E-05 0.00036601
            0.0008102 0.00142856 0.00222112 0.00318787
            0.00432881 0.00564393</samp></font><br>
            </ul>
        <ul><font face = \"times new roman\" color=#06159A size=4><i><b>
        b-) Text file by columns:</b></i></font>
        <font face = \"times new roman\" color=\"black\" size=4><i> in this format each column is a case.</i></font><br>
        <br>
            <ul><li><font face = \"times new roman\" size=4><i><b>Letter sequences:</b></i></font><br>
            <br>
            <font size=2><samp>Cha[01]Cha[02] Cha[03]<br>
                D G G<br>
                D D D<br>
                G D G<br>
                G G G<br>
                D G D<br>
                G D G<br>
                G G G<br>
                G G G<br>
                G G G<br>
                G G G<br>
                G G G<br>
                G G G</samp></font><br>
                </ul>
            <ul><li><font face = \"times new roman\" size=4><i><b>Numerics sequences:</b></i></font><br>
            <br>
                <font size=2><samp>Cha[01] Cha[02] Cha[03]<br>
                -7.86E-05 2.18E-07 9.60E-05<br>
                2.18E-07 9.60E-05 0.00036601<br>
                9.60E-05 0.00036601 0.0008102<br>
                0.00036601 0.0008102 0.00142856<br>
                0.0008102 0.00142856 0.00222112<br>
                0.00142856 0.00222112 0.00318787<br>
                0.00222112 0.00318787 0.00432881<br>
                0.00318787 0.00432881 0.00564393<br>
                0.00432881 0.00564393 0.00713324<br>
                0.00564393 0.00713324 0.00879674<br>
                0.00713324 0.00879674 0.01063443<br>
                0.00879674 0.01063443 0.01264631<br>
                0.01063443 0.01264631 0.01483238<br>
                0.01264631 0.01483238 0.01719263<br>
                0.01483238 0.01719263 0.01972708</samp></font><br>
                </ul>
                <br>
        <font face = \"times new roman\" color=#06159A size=4><i><b>c-) Text file in FASTA format:</b></i></font>
        <BLOCKQUOTE> 
            <font size=2><samp>&gt;gi|221068402|ref|ZP_03544507.1|enzyme [Comamonas testosteroni
            KF-1]<br>
            MSEPVNQWPQTLEERIDRLESLDAIRQLAGKYSLSLDMRDMDAHVNLFAPDIKVGKEKVGRAHFMAWQDS<br>
            TLRDQFTGTSHHLGQHIIEFVDRDHATGVVYSKNEHECGAEWVIMQMLYWDDYERIDGQWYFRRRLPCYW<br>
            YATDLNKPPIGDMKMRWPGREPYHGAFHELFPSWKEFWAQRPGKDQLPQVAAPAPLEQFLRTMRRGTPAP<br>
            RMRVR<br>
            <br>
            &gt;gi|220713425|gb|EED68793.1| enzyme [Comamonas testosteroni KF-1]<br>
            MSEPVNQWPQTLEERIDRLESLDAIRQLAGKYSLSLDMRDMDAHVNLFAPDIKVGKEKVGRAHFMAWQDS<br>
            TLRDQFTGTSHHLGQHIIEFVDRDHATGVVYSKNEHECGAEWVIMQMLYWDDYERIDGQWYFRRRLPCYW<br>
            YATDLNKPPIGDMKMRWPGREPYHGAFHELFPSWKEFWAQRPGKDQLPQVAAPAPLEQFLRTMRRGTPAP<br>
            RMRVR<br>
            <br>
            &gt;gi|77361071|ref|YP_340646.1| enzyme; class II aldolase/adducin,
            N-terminal<br>
            [Pseudoalteromonas haloplanktis TAC125]<br>
            MKKYDGLNQSMLERFATRPGRKELLPELSEKAQVALMCRMLIREGWDEHIAGHITYRLENGNILTNPWEL<br>
            AWGELTASDIVTLDPKGNVLDSDWNVTPAIGLHLQLHAMRPDVHVVIHNHPHWSGIWACMQKVPPVYDQA<br>
            SAYCGVELPLYDEYEGTFENEATSLSAVEALGDAKWALLANHGSLVVGKNLRQAHLRAITLEWRSKRAYE<br>
            VELAGGGRPLSDEEVKKVSIADDNGFPFVWEAMARKELRLDPGLVD<br>
            <br>
            &gt;gi|77360245|ref|YP_339820.1| enzyme [Pseudoalteromonas
            haloplanktis TAC125]<br>
            MQYLVISDIYGKTPCLQQLAKHFNAENQIVDPYNGVHQALENEEEYYKLFIKHCGHDEYAAKLEEYFNKL<br>
            SKPTICIAFSAGASAAWRAQASTTTTHLKKVIAFYPTQIRNYLNIDAIHPCEFIFPGFEPHFNVDELITN<br>
            LSAKNNVRCLKTLYLHGFMNQQSQNFSEYGYQYFYKVIKTANSEAH</samp></font><br>
            <p><font color=#0000FF size=2><b>Note:</b></font>
            <font size=2><i>In the cases of proteins, if the option protein is selected, each amino acid in the sequences is 
            codified in one of the four different amino acids classes determined by the different side chains: non-polar and neutral; 
            polar and neutral; acidic and polar; and basic and polar.</i></font></p>
            </BLOCKQUOTE> 
        <font face = \"times new roman\" color=#06159A size=4><i><b>d-) Text or CSV files of MS data:</b></i></font>
        <font face = \"times new roman\" size=4><i> In this option each case is in independent file and has two columns 
        mass/charge, Intensity with header or not.</i></font><br>
        <br>
            <ul><li><font face = \"times new roman\" size=4><i><b>Text files:</b></i></font>
            <font face = \"times new roman\" size=3><i> (\"tab\" separated columns)</i></font><br>
            <br>
                <font size=2><samp>2.5660&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;0.6601<br>
                3.6601&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;8.9102<br>
                8.1024&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;42.0856<br>
                14.2856&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;22.2112<br>
                22.2112&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;3.8787<br>
                31.8787&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;4.3288<br>
                43.2881&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;56.4393<br>
                56.4393&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;71.3324<br>
                71.3324&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;87.9674<br>
                87.9674&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;90.0000<br>
                106.3443&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;12.1631<br>
                126.4631&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;8.3238<br>
                148.3238&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;100.9263</samp></font><br>
                </ul>
                <br>
            <ul><li><font face = \"times new roman\" size=4><i><b>CSV files:</b></i></font>
                <font face = \"times new roman\" size=3><i> (\",\" separated columns)</i></font><br>
                <br>
                <font size=2><samp>m/Z,Intensity<br>
                2.5660,0.6601<br>
                3.6601,8.9102<br>
                8.1024,42.0856<br>
                14.2856,22.2112<br>
                22.2112,3.8787<br>
                31.8787,4.3288<br>
                43.2881,56.4393<br>
                56.4393,71.3324<br>
                71.3324,87.9674<br>
                87.9674,90.0000<br>
                106.3443,12.1631<br>
                126.4631,8.3238<br>
                148.3238,100.9263</samp></font>
                </ul>
</BLOCKQUOTE> 
</body>
</html>
"""
        elif pag == 'page2':
            page="""
<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN">
<html>
<head>
  <meta
 content="text/html; charset=ISO-8859-1"
 http-equiv="content-type">
  <title>Quick help about classes for
numerics sequences</title>
</head>
<body bgcolor= #EFFFFF>
<font face = \"times new roman\" color=#06159A size=4><i><b>
&nbsp;&nbsp;&nbsp;&nbsp;<li>II- Classes for numerics sequences:</font></i></b>
<font face = \"times new roman\" color=\"black\" size=4><i> this spin control box will be enable when an numeric input 
format is selected and it offers two different heuristics to transform the numeric data into letters sequences.</font></i><br>
                                <br>
                                <div align=center>
                                <img style="width: 599px; height: 229px;" alt=""
                                src='images/clasesnumericas.jpg'>
                                </div>
    <BLOCKQUOTE>
    <ul>
        <li><p><font face = \"times new roman\" color=#06159A size=4><i><b> n Regular Interval Classes:</b></i></font> 
        <font face = \"times new roman\" color=\"black\" size=4><i> in this option numeric data is divided in n 
        intervals or classes (2 &le; n &le; 10) and to each one of them is assigned a letter. This way, the elements 
        or signs of the numeric sequence are coded with the letter from the class to which belongs.</i></font></p></li>
        <br>
        <li><p><font face = \"times new roman\" color=#06159A size=4><i><b> n &sigma;-Interval Classes:</b></i></font> 
        <font face = \"times new roman\" color=\"black\" size=4><i> in this option the numeric data is 
        divided in 2n+2 intervals (2 &le; n &le; 4) that are function of its standard deviation. To each one of class 
        is assigned a letter and the element or signal of the numeric sequence are code with the letter from 
        the class to which belongs.</i></font></p></li>
        </ul>
        <p><font color=#0000FF size=2><b>Note:</b></font>
        <font size=2><i>In the cases of MS data, this program version transforms the original data in numerics sequences 
        obtained by means of the m/z and intensity values multiplication and after that, it makes the transformation in 
        the letters sequences using the heuristic selected by de user.</i></font></p>
        </BLOCKQUOTE>
</body>
</html>
"""
        elif pag == 'page3':
            page="""
<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN">
<html>
<head>
  <meta
 content="text/html; charset=ISO-8859-1"
 http-equiv="content-type">
  <title>Quick help about indices levels</title>
</head>
<body bgcolor= #EFFFFF>
<font face = \"times new roman\" color=#06159A size=4><i><b>
&nbsp;&nbsp;&nbsp;&nbsp;<li>IV- Indices levels:</font></i></b>
<font face = \"times new roman\" color=\"black\" size=4><i> this spin control box will be enable after one or more spiral graph have
been built and it offers three options to compute the TIs.</font></i><br>
<br>
                                <div align=center>
                                <img style="width: 599px; height: 229px;" alt=""
                                src='images/indiceslevels.jpg'>
                                </div>
    <BLOCKQUOTE>
    <ul>
        <li><p><font face = \"times new roman\" color=#06159A size=4><i><b> by classes in gnomons:</b></i></font> 
        <font face = \"times new roman\" color=\"black\" size=4><i> in this option the two family of TIs are calculated 
        for each one of the classes in each one of the gnnomons. If one class is not present in certain gnomon, its frequency and Shannon 
        entropy in this gnomon are zero. This option is more useful when the sequences are small and they have a few classes, 
        otherwise, a too high number of indices is obtained.</i></font></p></li>
        <br>
        <li><p><font face = \"times new roman\" color=#06159A size=4><i><b> by classes in global graph:</b></i></font> 
        <font face = \"times new roman\" color=\"black\" size=4><i> in this option the two family of TIs are calculated 
        for each one of the classes in the global graph. It other words, the sum of degrees of one class in all the gnomons 
        is used to calculate the indices of this class. This option reduces the total number of indices for what it is attractive 
        when we work with very long sequences.</i></font></p></li>
        <br>
        <li><p><font face = \"times new roman\" color=#06159A size=4><i><b> by gnomons:</b></i></font> 
        <font face = \"times new roman\" color=\"black\" size=4><i> in this option the two families of TIs are calculated 
        by gnomon (independently of the classes). It other words, the sum of degrees of all the classes in one gnomon is used 
        to calculate the indices of this gnomon. This option is more useful when the sequences have a great number of 
        classes and have a moderated size.</i></font></p></li>
        </ul>
        </BLOCKQUOTE>
</body>
</html>
"""
        else:
            page = """
<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN">
<html>
<head>
  <meta
 content="text/html; charset=ISO-8859-1"
 http-equiv="content-type">
  <title>CULSPIN Help</title>
</head>
<body bgcolor= #EFFFFF>
<div align=center><b><font face = \"times new roman\" color=\"red\" size=7>CULSPIN </font>
<font face = \"times new roman\" color=#06159A size=7>- </font>
<font face = \"times new roman\" color=\"red\" size=7>C</font>
<font face = \"times new roman\" color=#06159A size=7>ompute&nbsp;&nbsp;</font>
<font face = \"times new roman\" color=\"red\" size=7>UL</font>
<font face = \"times new roman\" color=#06159A size=7>am&nbsp;&nbsp;</font>
<font face = \"times new roman\" color=\"red\" size=7>SP</font>
<font face = \"times new roman\" color=#06159A size=7>iral&nbsp;&nbsp;</font>
<font face = \"times new roman\" color=\"red\" size=7>IN</font>
<font face = \"times new roman\" color=#06159A size=7>dices&nbsp;&nbsp;1.0&nbsp;&nbsp;HELP</font></b><br>
</div>
<div align=center>
<img style="width: 155px; height: 150px;"
 alt=""
 src='images/iniciohelp.jpg'><br>
</div>
<p><i>&nbsp;&nbsp;&nbsp;&nbsp;<font face = \"times new roman\" color=\"red\" size=4><b>CULSPIN</b></font> 
<font face = \"times new roman\" size=4>is a application that use an type of numeric representations named Ulam spiral. 
The mathematician Stanisław Ulam discovered it in 1963 and latter the spiral became highly popularized as visual picture 
in a number of Scientific American in 1964. To construct the spiral one must write down a regular grid of numbers, starting 
with one at the center, and spiraling out the rest of integer numbers [1-4] just as you can see in the image of below.<br>
                                        <br>
                                        <div align=center>
                                        <img style="width: 599px; height: 229px;"
                                         alt=""
                                         src='images/spiralnum.jpg'><br>
                                        </div>
&nbsp;&nbsp;&nbsp;&nbsp;In mathematics, this is a simple method of graphing numbers that reveals very hidden patterns in 
numeric series and sequences. In molecular sciences this Spiral representation was associated to a graph in order to represent 
DNA nucleotide sequences in a seminar work after Randic et al. [5]; who called it the four-color map representation of DNA. 
The name refers to a classification of DNA sequence letters in four classes (A, T, G, and C). This work opened an interesting 
way for the application of Ulam Spiral graphs in molecular sciences.<br>
&nbsp;&nbsp;&nbsp;&nbsp; CULSPIN helps you to transform any letter sequence in a particular Ulam Spiral representation (call here as 
U-graph) and to compute two family of Topological Indices (TIs). These indices can be calculated for all the classes in each Ulam 
gnomon, for all the classes in global graph and for each gnomon. Also the 2D U-graph genarated by this application can be 
exported in order to calculate other indices families using a great variety of existent programs. All these numerics indices can be 
used for the statistical analysis of your initial data. The initial use of this program is the creation of statistical models 
for a great variety of molecular systems .</font></i></p><br>
<br>
<font face = \"times new roman\" color=#06159A size=6><b>What CULSPIN can do?</b></font><br>
<br>
<ul>
    <i><font face = \"times new roman\" size=4>
    <li><b>Read</b> letter <b>sequences</b>, organized by rows or columns, from <b>TXT</b> file;</li>
    <li><b>Read</b> letter <b>sequences</b> in <b>FASTA</b> format from <b>TXT</b> file;</li>
    <li><b>Read</b> numerics <b>sequences</b>, organized by rows or columns, from <b>TXT</b> file;</li>
    <li><b>Read</b> Mass Spectra <b>(MS)</b> data from multiple <b>TXT</b> or <b>CSV</b> files;</li>
    <li><b>Encode</b> numerics <b>sequences</b> and <b>MS</b> data in letter <b>sequences</b>;</li>
    <li><b>Transform</b> any letter <b>sequence</b> in an <b>U-graph</b> connecting the nodes that have the same letter (same class);</li>
    <li><b>Compute</b> two family of <b>TIs</b> using the U-graph;</li>
    <li><b>Plot</b> and <b>Visualize</b> the <b>U-graph</b> and shows the <b>TIs</b> values;</li>
    <li><b>Export</b> the <b>U-graph</b> connectivity as <b>CT</b> or <b>NET</b> file;</li>
    <li><b>Save</b> the <b>TIs</b> values in <b>TXT</b> or <b>CSV</b> file.</li></font></i><br>
</ul>
<font face = \"times new roman\" color=#06159A size=6><b>How to use CULSPIN?</b></font><br>
    <br>
    <font face = \"times new roman\" size=4><i>&nbsp;&nbsp;&nbsp;&nbsp;CULSPIN is a Python/wxPython application that has 
    a main menu bar with the fallowing options: </i></font><br>
                                        <br>
                                        <div align=center>
                                        <img style="width: 599px; height: 229px;"
                                         alt=""
                                         src='images/menubar.jpg'><br>
                                        </div>
    <BLOCKQUOTE>
        <font face = \"times new roman\" color=#06159A size=4><i><b>- File :</b></i></font><br>
            <ul>
            <font face = \"times new roman\" size=4><i>
            <li><b>Open file :</b> it allws to select the input file(s) for open it and to upload the data. 
            Once finished the reading, the sequences are shown in a list box.</li>
            <li><b>Reload seqeunces :</b> it allws to work again with all the original sequences. It is only 
            activate when we was not built the spiral to some original sequence. Once finished, all the initial
            sequences are shown in a list box.</li>
            <li><b>Make a copy of :</b> save in a .txt file the original sequences or those that were studied, organizing them such 
            and like that they are shown in the list box. It is activate when the input data did not have this format.</li>
            <li><b>Export graph :</b> to export the connectivity information of alls U-graphs in <b>\" .ct\"</b> or <b>\" .net\" </b> 
            files in order to open them with other programs to make another calculations.</li> 
            <li><b>Save Indices :</b> to store the indices values in one <b>\" .txt\"</b> or <b>\" .csv\"</b> file for the posterior 
            statistical analysis.</li>
            <li><b>Quit :</b> to exit of application.</i></font></li><br>
            </ul>
        <font face = \"times new roman\" color=#06159A size=4><i><b>- Submit :</b></i></font><br>
            <ul>
            <font face = \"times new roman\" size=4><i>
            <li><b>Build Spiral :</b> to Build the U-graph and connect the nodes with the same class to each one of the selected sequences .</li> 
            <li><b>Calculate Indices :</b> to compute the TIs using the U-graph of the selected sequences. Once finiched the operation the 
            results are available in a new page of the notebook.</i></font></li><br>
            </ul>
        <font face = \"times new roman\" color=#06159A size=4><i><b>- View :</b></i></font><br>
            <ul>
            <font face = \"times new roman\" size=4><i>
            <li><b>View a graph :</b> to plot and to visualize, in an independent windows, the U-graph of one selected sequence. It is only enable 
            after an <b>Build Spiral</b> operation.</i></font></li><br>
            </ul>
        <font face = \"times new roman\" color=#06159A size=4><i><b>- Help :</b></i></font><br>
            <ul> 
            <font face = \"times new roman\" size=4><i>  
            <li><b>Help :</b> to read this help document.</li> 
            <li><b>About :</b> to read the classic about windows.</i></font></li>
            </ul>
    </BLOCKQUOTE>
    <br>
    <font face = \"times new roman\" size=4><i>&nbsp;&nbsp;&nbsp;&nbsp;CULSPIN is an Notebook format application. 
    At the beginning, the main window shows only one page <b>Options</b> and after an <b>Calculate Indices</b> 
    operation, one page with the <b>Indices</b> is added.</i></font><br>
                                        <br>
                                        <div align=center>
                                        <img style="width: 599px; height: 229px;"
                                         alt=""
                                         src='images/opcionsculspin.jpg'><br>
                                        </div>
<br>
<font face = \"times new roman\" color=#06159A size=5><i><b>- Options page :</b></i></font>
<font face = \"times new roman\" size=4><i> in this page there are four defined areas:</i></font><br>
<br>
<font face = \"times new roman\" color=#06159A size=4><i><b>
&nbsp;&nbsp;&nbsp;&nbsp;<li>I- Input file(s) format:</b></i></font>
<font face = \"times new roman\" colo=\"black\" size=4><i> this spint control box allows to select, among five input file 
format, the one that corresponds to our data.</i></font></li><br>
                                <br>
                                <div align=center>
                                <img style="width: 599px; height: 229px;" alt=""
                                src='images/inputfileformat.jpg'>
                                </div>
    <BLOCKQUOTE>
        <font face = \"times new roman\" color=#06159A size=4><b><i>
        a) Text file by rows:</i></b></font>
        <font face = \"times new roman\" colo=\"black\" size=4><i>in this format each row is a case.</i></font></li><br>
        <br>
            <ul><li><font face = \"times new roman\" colo=\"black\" size=4><i><b>Letter sequences:</b></i></font></li><br>
            <br>
            <font size=2><samp>Cha[01]
            GDDGGGGGDGGGDGDDGGGDGGGDGDGGDGDDDDGGGGGDGGDDGGGGGGGGGGGGKKKKKAAAKKAKKKKAAK<br>
            Cha[02]
            DDGGDGGGGGGGGDGGGDGDDDDDDGGGGGDGGDDGGGGGGGGGGGGGGGGKKKKKAAAKKAKKKKK<br>
            Cha[03]
            GDGGDGGGGGGGGDGGGDGDDGGGDGGGDGDGGDGDDDDGGGGGDGGDDGGGGGGGGGGKKKKKAAAKKAKKKKKKAAA</samp></font><br>
            <li><font face = \"times new roman\" size=4><i><b>Numerics sequences:</b></i></font><br>
            <br>
            <font size=2><samp>Cha[01]
            -7.86E-05 2.18E-07 9.60E-05 0.00036601 0.0008102 0.00142856
            0.00222112 0.00318787 0.00432881<br>
            Cha[02] 2.18E-07 9.60E-05
            0.00036601 0.0008102 0.00142856 0.00222112
            0.00318787 0.00432881 -7.86E-05</small><br>
            Cha[03] 9.60E-05 0.00036601
            0.0008102 0.00142856 0.00222112 0.00318787
            0.00432881 0.00564393</samp></font><br>
            </ul>
        <ul><font face = \"times new roman\" color=#06159A size=4><i><b>
        b-) Text file by columns:</b></i></font>
        <font face = \"times new roman\" color=\"black\" size=4><i> in this format each column is a case.</i></font><br>
        <br>
            <ul><li><font face = \"times new roman\" size=4><i><b>Letter sequences:</b></i></font><br>
            <br>
            <font size=2><samp>Cha[01]Cha[02] Cha[03]<br>
                D G G<br>
                D D D<br>
                G D G<br>
                G G G<br>
                D G D<br>
                G D G<br>
                G G G<br>
                G G G<br>
                G G G<br>
                G G G<br>
                G G G<br>
                G G G</samp></font><br>
                </ul>
            <ul><li><font face = \"times new roman\" size=4><i><b>Numerics sequences:</b></i></font><br>
            <br>
                <font size=2><samp>Cha[01] Cha[02] Cha[03]<br>
                -7.86E-05 2.18E-07 9.60E-05<br>
                2.18E-07 9.60E-05 0.00036601<br>
                9.60E-05 0.00036601 0.0008102<br>
                0.00036601 0.0008102 0.00142856<br>
                0.0008102 0.00142856 0.00222112<br>
                0.00142856 0.00222112 0.00318787<br>
                0.00222112 0.00318787 0.00432881<br>
                0.00318787 0.00432881 0.00564393<br>
                0.00432881 0.00564393 0.00713324<br>
                0.00564393 0.00713324 0.00879674<br>
                0.00713324 0.00879674 0.01063443<br>
                0.00879674 0.01063443 0.01264631<br>
                0.01063443 0.01264631 0.01483238<br>
                0.01264631 0.01483238 0.01719263<br>
                0.01483238 0.01719263 0.01972708</samp></font><br>
                </ul>
                <br>
        <font face = \"times new roman\" color=#06159A size=4><i><b>c-) Text file in FASTA format:</b></i></font>
        <BLOCKQUOTE> 
            <font size=2><samp>&gt;gi|221068402|ref|ZP_03544507.1|enzyme [Comamonas testosteroni
            KF-1]<br>
            MSEPVNQWPQTLEERIDRLESLDAIRQLAGKYSLSLDMRDMDAHVNLFAPDIKVGKEKVGRAHFMAWQDS<br>
            TLRDQFTGTSHHLGQHIIEFVDRDHATGVVYSKNEHECGAEWVIMQMLYWDDYERIDGQWYFRRRLPCYW<br>
            YATDLNKPPIGDMKMRWPGREPYHGAFHELFPSWKEFWAQRPGKDQLPQVAAPAPLEQFLRTMRRGTPAP<br>
            RMRVR<br>
            <br>
            &gt;gi|220713425|gb|EED68793.1| enzyme [Comamonas testosteroni KF-1]<br>
            MSEPVNQWPQTLEERIDRLESLDAIRQLAGKYSLSLDMRDMDAHVNLFAPDIKVGKEKVGRAHFMAWQDS<br>
            TLRDQFTGTSHHLGQHIIEFVDRDHATGVVYSKNEHECGAEWVIMQMLYWDDYERIDGQWYFRRRLPCYW<br>
            YATDLNKPPIGDMKMRWPGREPYHGAFHELFPSWKEFWAQRPGKDQLPQVAAPAPLEQFLRTMRRGTPAP<br>
            RMRVR<br>
            <br>
            &gt;gi|77361071|ref|YP_340646.1| enzyme; class II aldolase/adducin,
            N-terminal<br>
            [Pseudoalteromonas haloplanktis TAC125]<br>
            MKKYDGLNQSMLERFATRPGRKELLPELSEKAQVALMCRMLIREGWDEHIAGHITYRLENGNILTNPWEL<br>
            AWGELTASDIVTLDPKGNVLDSDWNVTPAIGLHLQLHAMRPDVHVVIHNHPHWSGIWACMQKVPPVYDQA<br>
            SAYCGVELPLYDEYEGTFENEATSLSAVEALGDAKWALLANHGSLVVGKNLRQAHLRAITLEWRSKRAYE<br>
            VELAGGGRPLSDEEVKKVSIADDNGFPFVWEAMARKELRLDPGLVD<br>
            <br>
            &gt;gi|77360245|ref|YP_339820.1| enzyme [Pseudoalteromonas
            haloplanktis TAC125]<br>
            MQYLVISDIYGKTPCLQQLAKHFNAENQIVDPYNGVHQALENEEEYYKLFIKHCGHDEYAAKLEEYFNKL<br>
            SKPTICIAFSAGASAAWRAQASTTTTHLKKVIAFYPTQIRNYLNIDAIHPCEFIFPGFEPHFNVDELITN<br>
            LSAKNNVRCLKTLYLHGFMNQQSQNFSEYGYQYFYKVIKTANSEAH</samp></font><br>
            <p><font color=#0000FF size=2><b>Note:</b></font>
            <font size=2><i>In the cases of proteins, if the option protein is selected, each amino acid in the sequences is 
            codified in one of the four different amino acids classes determined by the different side chains: non-polar and neutral; 
            polar and neutral; acidic and polar; and basic and polar.</i></font></p>
            </BLOCKQUOTE> 
        <font face = \"times new roman\" color=#06159A size=4><i><b>d-) Text or CSV files of MS data:</b></i></font>
        <font face = \"times new roman\" size=4><i> In this option each case is in independent file and has two columns 
        mass/charge, Intensity with header or not.</i></font><br>
        <br>
            <ul><li><font face = \"times new roman\" size=4><i><b>Text files:</b></i></font>
            <font face = \"times new roman\" size=3><i> (\"tab\" separated columns)</i></font><br>
            <br>
                <font size=2><samp>2.5660&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;0.6601<br>
                3.6601&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;8.9102<br>
                8.1024&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;42.0856<br>
                14.2856&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;22.2112<br>
                22.2112&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;3.8787<br>
                31.8787&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;4.3288<br>
                43.2881&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;56.4393<br>
                56.4393&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;71.3324<br>
                71.3324&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;87.9674<br>
                87.9674&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;90.0000<br>
                106.3443&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;12.1631<br>
                126.4631&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;8.3238<br>
                148.3238&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;100.9263</samp></font><br>
                </ul>
                <br>
            <ul><li><font face = \"times new roman\" size=4><i><b>CSV files:</b></i></font>
                <font face = \"times new roman\" size=3><i> (\",\" separated columns)</i></font><br>
                <br>
                <font size=2><samp>m/Z,Intensity<br>
                2.5660,0.6601<br>
                3.6601,8.9102<br>
                8.1024,42.0856<br>
                14.2856,22.2112<br>
                22.2112,3.8787<br>
                31.8787,4.3288<br>
                43.2881,56.4393<br>
                56.4393,71.3324<br>
                71.3324,87.9674<br>
                87.9674,90.0000<br>
                106.3443,12.1631<br>
                126.4631,8.3238<br>
                148.3238,100.9263</samp></font>
                </ul>
</BLOCKQUOTE> 
<font face = \"times new roman\" color=#06159A size=4><i><b>
&nbsp;&nbsp;&nbsp;&nbsp;<li>II- Classes for numerics sequences:</font></i></b>
<font face = \"times new roman\" color=\"black\" size=4><i> this spin control box will be enable when an numeric input 
format is selected and it offers two different heuristics to transform the numeric data into letters sequences.</font></i><br>
                                <br>
                                <div align=center>
                                <img style="width: 599px; height: 229px;" alt=""
                                src='images/clasesnumericas.jpg'>
                                </div>
    <BLOCKQUOTE>
    <ul>
        <li><p><font face = \"times new roman\" color=#06159A size=4><i><b> n Regular Interval Classes:</b></i></font> 
        <font face = \"times new roman\" color=\"black\" size=4><i> in this option numeric data is divided in n 
        intervals or classes (2 &le; n &le; 10) and to each one of them is assigned a letter. This way, the elements 
        or signs of the numeric sequence are coded with the letter from the class to which belongs.</i></font></p></li>
        <br>
        <li><p><font face = \"times new roman\" color=#06159A size=4><i><b> n &sigma;-Interval Classes:</b></i></font> 
        <font face = \"times new roman\" color=\"black\" size=4><i> in this option the numeric data is 
        divided in 2n+2 intervals (2 &le; n &le; 4) that are function of its standard deviation. To each one of class 
        is assigned a letter and the element or signal of the numeric sequence are code with the letter from 
        the class to which belongs.</i></font></p></li>
        </ul>
        <p><font color=#0000FF size=2><b>Note:</b></font>
        <font size=2><i>In the cases of MS data, this program version transforms the original data in numerics sequences 
        obtained by means of the m/z and intensity values multiplication and after that, it makes the transformation in 
        the letters sequences using the heuristic selected by de user.</i></font></p>
        </BLOCKQUOTE>
<font face = \"times new roman\" color=#06159A size=4><i><b>
&nbsp;&nbsp;&nbsp;&nbsp;<li>III- A list box for view/select sequences:</font></i></b>
    <font face = \"times new roman\" color=\"black\" size=4><i><b> this list box has the function to <b>show/select</b> 
    letters sequences. Firstly it is empty and it will show the sequences that were directly read from the input file or 
    those obtained by means of a previous encode (using the heuristic selected) in the case of the numeric data.<br>
                                <br>
                                <div align=center>
                                <img style="width: 599px; height: 229px;" alt=""
                                src='images/listbox1.jpg'>
                                </div><br>
    <br>
     Once the letters sequences have been shown, an invitation to select the sequences with those we wants to work is made. 
     A compact block of cases can be selected using the <b>Shift</b> key, alternated sequences with the <b>Ctrl</b> key or 
    marks the checkbox <b>Select all</b> to select alls of them.<br>
                                <br>
                                <div align=center>
                                <img style="width: 599px; height: 229px;" alt=""
                                src='images/listbox2.jpg'>
                                </div><br>
    <br>
    &nbsp;&nbsp;&nbsp;&nbsp;After the selected sequences are submited to the U-graph building (menu <b>Tools</b> option <b>Build 
    Spiral</b>), the list box only shows the submited sequences. At this time, an invitation to select the sequences to calculate 
    their indices or select one sequence to see its spiral graph is made.<br>
                                <br>
                                <div align=center>
                                <img style="width: 599px; height: 229px;" alt=""
                                src='images/listbox3.jpg'>
                                </div><br>
    <br>
    If you want it, all the original sequences (selected or not) they can be loaded and to be shown again by means of the option 
    <b>Reload sequences</b> in the file menu.</i></font><br>
<br>
<font face = \"times new roman\" color=#06159A size=4><i><b>
&nbsp;&nbsp;&nbsp;&nbsp;<li>IV- Indices levels:</font></i></b>
<font face = \"times new roman\" color=\"black\" size=4><i> this spin control box will be enable after one or more spiral graph have
been built and it offers three options to compute the TIs.</font></i><br>
<br>
                                <div align=center>
                                <img style="width: 599px; height: 229px;" alt=""
                                src='images/indiceslevels.jpg'>
                                </div>
    <BLOCKQUOTE>
    <ul>
        <li><p><font face = \"times new roman\" color=#06159A size=4><i><b> by classes in gnomons:</b></i></font> 
        <font face = \"times new roman\" color=\"black\" size=4><i> in this option the two family of TIs are calculated 
        for each one of the classes in each one of the gnnomons. If one class is not present in certain gnomon, its frequency and Shannon 
        entropy in this gnomon are zero. This option is more useful when the sequences are small and they have a few classes, 
        otherwise, a too high number of indices is obtained.</i></font></p></li>
        <br>
        <li><p><font face = \"times new roman\" color=#06159A size=4><i><b> by classes in global graph:</b></i></font> 
        <font face = \"times new roman\" color=\"black\" size=4><i> in this option the two family of TIs are calculated 
        for each one of the classes in the global graph. It other words, the sum of degrees of one class in all the gnomons 
        is used to calculate the indices of this class. This option reduces the total number of indices for what it is attractive 
        when we work with very long sequences.</i></font></p></li>
        <br>
        <li><p><font face = \"times new roman\" color=#06159A size=4><i><b> by gnomons:</b></i></font> 
        <font face = \"times new roman\" color=\"black\" size=4><i> in this option the two families of TIs are calculated 
        by gnomon (independently of the classes). In other words, the sum of degrees of all the classes in one gnomon is used 
        to calculate the indices of this gnomon. This option is more useful when the sequences have a great number of 
        classes and have a moderated size.</i></font></p></li>
        </ul>
        </BLOCKQUOTE>
<font face = \"times new roman\" color=#06159A size=5><i><b>- Indices page :</b></i></font>
<font face = \"times new roman\" size=4><i> this page is added after a <b>Calculate Indices</b> submition and it shows, in a grid 
format, the values of the calculated TIs.<br>
                                <br>
                                <div align=center>
                                <img style="width: 599px; height: 229px;" alt=""
                                src='images/gridindices.jpg'>
                                </div><br>
<br>
In this grid you can select one cell; an range of cells; or all the cells and copy the selection into clipboard using 
<b>Ctrl+C</b> combination. It is a rapid export procedure that allows to paste this values in another external application 
such as Exel.</i></font><br>
<br>
<font face = \"times new roman\" color=#06159A size=6><b>CULSPIN indices calculation.</b></font><br>
<p><font face = \"times new roman\" size=4><i>
&nbsp;&nbsp;&nbsp;&nbsp; The Ulam spiral representation can be divide in different regions or intervals named 
<b>GNOMONS</b> or angular disposition. To define the gnomons will be necessary to remember the oblong numbers 
that are those that can be represented by means of the product n(n+1) with natural n: 2, 6, 12, 20, 30, 42, 56, 
72, 90,.... These numbers divide to the group of natural numbers in intervals of growing longitude (2n), represented 
in the Ulam spiral in the image of below:</i></font></p><br>
                                    <br>
                                    <div align=center>
                                    <img style="width: 599px; height: 229px;"
                                     alt=""
                                     src='images/gnomoneshelp1.jpg'>
                                    </div>
<p><font face = \"times new roman\" size=4><i>It is easy to see that each couple of serial oblong numbers defines a gnomon. 
In the figure you can observe that those gnomons is inserted to form rectangles of growing magnitude. Thus can be defined, 
for each number the Ulam coordinate U<sub>n</sub> to the order number of the gnomon to which belongs. <br>
When a sequence is represented in our U-graph, each node it is an element of the sequence whose letter represents the class to 
which belongs, so in each gnomon there are one or more classes.</i></p><br>
                                    <br>
                                    <div align=center>
                                    <img style="width: 599px; height: 229px;"
                                     alt=""
                                     src='images/gnomoneshelp2.jpg'>
                                    </div><br>
<br>
<p><font face = \"times new roman\" size=4><i>In ours U-graphs the nodes are not only connected following the sequence order but rather CULSPIN also connects directly those 
nodes that belong to oneself class. For example U-graph of the sequence Cha[01] will be:</i></p></font><br>
<br>
<font size=2><samp>
Cha[01] GDDGGDGGGGGGGGDGGGDGDDGGGDGGGDGDGGDGDDDDGGGGGDGGDDGGGGGGGGGGGGGGGGKKKKKAAAKKAKKKKKKAAAKKKKAKKKKKAAKKKKKKKKKAAKKAAAAAK
</samp></font><br>
                                    <br>
                                    <div align=center>
                                    <img style="width: 599px; height: 229px;"
                                     alt=""
                                     src='images/cha01graphhelp.jpg'>
                                    </div><br>
<br>
<p><font face = \"times new roman\" size=4><i>&nbsp;&nbsp;&nbsp;&nbsp; If the degrees of a node is defined as the number of connections of this node and the total degrees as 
the sum of all the nodes degrees in the graph, the degrees of a gnomon can be defined as the sum of the nodes degreees in this 
gnomon. Using these terms and take into account that each nodes in ourw U-graph belong to one specific class, the frequency and 
Shannon entropy at different levels can be calculated according to: </i><p></font><br>
<br>
                                    <div align=center>
                                    <img style="width: 599px; height: 229px;"
                                     alt=""
                                     src='images/tablaindiceshelp.jpg'>
                                    </div><br>
<br>
<br>
                                    <div align=center>
                                    <img style="width: 599px; height: 229px;"
                                     alt=""
                                     src='images/bibliohelp.jpg'>
                                    </div><br>
<br>
</body>
</html>
"""
        html.SetPage(page)

#===============================================================================
# app = wx.PySimpleApp()
# frm = MyHtmlFrame(None, "Help ", 'page4', raiz_images= os.getcwd()+"\\")
# frm.Center()
# frm.Show()
# app.MainLoop()
#===============================================================================
