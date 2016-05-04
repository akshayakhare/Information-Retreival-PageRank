# PageRank
Runs the PageRank algorithm to rank given sites

Steps for running the program:
---------------------------------------------------------------------------------------------------------------------------
1. Install Python if not already installed from https://www.python.org/downloads/  version 2.7.10
2. The file 'Page_Rank_with_in_links.py' contains the algorithm for page rank
3. Change the location of the output file if needed on line 187 & 199, else it will print the output files in the same location
4. In order to execute the Page_Rank_with_in_links.py file, go to python shell and type  
	execfile('Page_Rank_with_in_links.py')
5. Provide the necessary file name or path name as mentioned in the screen


References:
----------------------------------------------------------------------------------------------------------------------------
http://stackoverflow.com/-> Helping out for various logic and syntax issues in python
https://www.python.org/doc/


Findings and output:
----------------------------------------------------------------------------------------------------------------------------
proportion of pages with no out-links 0.360016538727
Proportion of Pages with initially less ranking 0.786117261753
Proportion of zero in links to total pages 0.0780693212049

******************************************************************************************************
Top 50 pages with highest ranking:->
"Top50_Page_Rankings.txt"

******************************************************************************************************
Top 50 pages with highest inlinks:->
"Top50_Pages_with_Inlinks.txt"

******************************************************************************************************
The proportions and Perplexity values are given in the below file:
"Proportions and Perplexity_Values.txt"

******************************************************************************************************
Names of the files which contain Page Ranking for Sample Graph for 1, 10 and 100 loops are given below:
"PageRanking_on_sample_pages_for_1_loop.txt"
"PageRanking_on_sample_pages_for_10_loop.txt"
"PageRanking_on_sample_pages_for_100_loop.txt"

******************************************************************************************************
The analysis of the output received:
"Analysis_On_The_PageRanking_Results.txt" 

******************************************************************************************************
All Pages sorted with PageRank Value:
"PageRanking.txt"

******************************************************************************************************
All Pages sorted with Their Inlinks count:
"PageRanking_Inlinks.txt"
