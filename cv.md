- 👋 Hi, I’m @Killerbee7
- 👀 I’m interested in ...
- 🌱 I’m currently learning ...
- 💞️ I’m looking to collaborate on ...
- 📫 How to reach me ...

<!---
Killerbee7/Killerbee7 is a ✨ special ✨ repository because its `README.md` (this file) appears on your GitHub profile.
You can click the Preview link to take a look at your changes.
--->
% FortySecondsCV LaTeX template
% Copyright © 2019 René Wirnata <rene.wirnata@pandascience.net>
% Licensed under the 3-Clause BSD License. See LICENSE file for details.
%
% Attributions
% ------------
% * fortysecondscv is based on the twentysecondcv class by Carmine Spagnuolo 
%   (cspagnuolo@unisa.it), released under the MIT license and available under
%   https://github.com/spagnuolocarmine/TwentySecondsCurriculumVitae-LaTex
% * further attributions are indicated immediately before corresponding code


%-------------------------------------------------------------------------------
%                             ADDITIONAL PACKAGES
%-------------------------------------------------------------------------------
\documentclass[
  a4paper, 
%   showframes,
%   maincolor=cvgreen,
%   sectioncolor=red,
%   subsectioncolor=orange
%   sidebarwidth=0.4\paperwidth,
%   topbottommargin=0.03\paperheight,
%   leftrightmargin=20pt
]{fortysecondscv}

% improve word spacing and hyphenation
\usepackage{microtype}
\usepackage{ragged2e}

% take care of proper font encoding
\ifxetex
	\usepackage{fontspec}
	\defaultfontfeatures{Ligatures=TeX}
% \newfontfamily\headingfont[Path = fonts/]{segoeuib.ttf} % local font
\else
	\usepackage[utf8]{inputenc}
	\usepackage[T1]{fontenc}
% \usepackage[sfdefault]{noto} % use noto google font
\fi

% enable mathematical syntax for some symbols like \varnothing
\usepackage{amssymb}

% bubble diagram configuration
\usepackage{smartdiagram}
\smartdiagramset{
  % defaut font size is \large, so adjust to harmonize with sidebar layout
  bubble center node font = \footnotesize,
  bubble node font = \footnotesize,
  % default: 4cm/2.5cm; make minimum diameter relative to sidebar size
  bubble center node size = 0.4\sidebartextwidth,
  bubble node size = 0.25\sidebartextwidth,
  distance center/other bubbles = 1.5em,
  % set center bubble color
  bubble center node color = maincolor!70,
  % define the list of colors usable in the diagram
  set color list = {maincolor!10, maincolor!40,
  maincolor!20, maincolor!60, maincolor!35},
  % sets the opacity at which the bubbles are shown
  bubble fill opacity = 0.8,
}


%-------------------------------------------------------------------------------
%                            PERSONAL INFORMATION
%-------------------------------------------------------------------------------
% profile picture
\cvprofilepic{dd.jpg}
% your name
\cvname{Dibya Dahal}
% job title/career
\cvjobtitle{Software and Electronics Engineer}
% date of birth
\cvbirthday{Dec 6, 1993}
% short address/location, use \newline if more than 1 line is required
\cvaddress{Sananjalankuja 5H 62,\newline 00730 Helsinki,Finland}
% phone number
\cvphone{+358406582221}
% personal website
\cvsite{https://www.linkedin.com/in/dibya-dahal-8a10b1236/}

% email address
\cvmail{dahal.dibya7@gmail.com}

% add additional information
% \newcommand{\additional}{some more?}


%-------------------------------------------------------------------------------
%                              SIDEBAR 1st PAGE
%-------------------------------------------------------------------------------
% overwrite default icons and order of personal information
% \renewcommand{\personaltable}{%
% 	\begin{personal}[0.8em]
% 		\circleicon{\faKey}      & \cvkey  \\
% 		\circleicon{\faAt}       & \cvmail \\
% 		\circleicon{\faGlobe}    & \cvsite \\
% 		\circleicon{\faPhone}    & \cvphone \\
% 		\circleicon{\faEnvelope} & \cvaddress \\
% 		\circleicon{\faInfo}     & \cvbirthday \\
% 		% add another line
% 		\circleicon{\faQuestion} & \additional
% 	\end{personal}
% }

% add more profile sections to sidebar on first page
\addtofrontsidebar{
	
	% include gosquare national flags from https://github.com/gosquared/flags;
	% naming according to ISO 3166-1 alpha-2 country codes
	\graphicspath{{pics/flags/}}

	\profilesection{Languages}
		
		\pointskill{\flag{np1.png}}{Nepali}{5}
		\pointskill{\flag{GB.png}}{English}{4}
		
		\pointskill{\flag{fin.jpg}}{Finnish}{2}


	\profilesection{Hobbies}
	    \skill{\ }{Playing Cricket and Table Tennis}
	    \skill{\ }{Cycling}
	    \skill{\ }{Reading Manga}
}


%-------------------------------------------------------------------------------
%                              SIDEBAR 2nd PAGE
%-------------------------------------------------------------------------------



%-------------------------------------------------------------------------------
%                         TABLE ENTRIES RIGHT COLUMN
%-------------------------------------------------------------------------------
\begin{document}

\makefrontsidebar

\cvsection{Profile}
\begin{cvtable}

\cvitem{Myself}{A responsible and motivated individual. Good at working and collaborating with team members to strive for the best possible results.I am flexible, reliable and
possess excellent time keeping skills.}{}{}


\cvitem{}{}{}

\cvitem{Objective}{To be associated with a progressive organisation that gives me scopes to gain and enrich my skills at congruent to a global level , to learn team dynamics and to work towards the growth of the organisation.}{   }{}


\end{cvtable}

\cvsection{Education}

\begin{cvtable}
	
	\cvitem{ 2014 -- 2020}{Bacherlor of  Science}{Metropolia University of Applied Sciences, Finland                                 }
		{Electronics Engineering}{ }
		\end{cvtable}
	   
	   \begin{cvtable}
	       
	                
	\cvitem{2011--2013}{High School}{Infotech Higher Secondary School, Nepal}{Major: Science}
	

\end{cvtable}
\cvsection{Project}
\begin{cvtable}
	\cvitem{ Thesis}{Biometric Voting System}{Metropolia University of Applied Sciences, Finland}

	\cvitem{}{Designed and successfully tested an embedded voting system using microcontroller, fingerprint module, LCD and other electronic components. }{            }{}
	
	
	



\end{cvtable}

\begin{cvtable}
    
\end{cvtable}

\begin{cvtable}
	\cvitem{ Innovation Project}{Recharge station}{Metropolia University of Applied Sciences, Finland}

	\cvitem{}{Designed and tested a prototype device for charging smartphones and tablets using exercise bike. It was designed for an old age home where residents can exercise and charge devices at the same time.}{            }{}
	
	
	



\end{cvtable}



\cvsection{Experience}
\begin{cvtable}
	\cvitem{05.01.2017--05.06.2017}{Trainee}{Parsa FM Private Limited, Nepal}

	\cvitem{}{Worked as assistant Broadcast Engineer.Major tasks include setting up and
repairing equipments, monitoring and maintaining transmission feeds, and regulating the audio components of br adcasting.}{            }{}
	
	
	



\end{cvtable}

\cvsection{Skills}
		\skill{\ }{AutoCAD}
		\skill{\ }{MATLAB}
        \skill{\ }{Microcontrollers}
	    \skill{\ }{PCB Design}
	    \skill{\ }{Embedded Systems}
	    	    \skill{\ }{Power Electronics}
	    	    
	    	    \cvsection{IT Skills}
		\skill{\ }{C}
		\skill{\ }{C++}
        \skill{\ }{Python}
    	\skill{\ }{}
	   

\end{document}
