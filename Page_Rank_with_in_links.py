from __future__ import division
from math import log
import operator
__author__ = 'Akshaya'


# // P is the set of all pages; |P| = N
# // S is the set of sink nodes, i.e., pages that have no out links
# // M(p) is the set (without duplicates) of pages that link to page p-> List_Mp
# // L(q) is the number of out-links (without duplicates) from page q-> List_Lq
# // d is the PageRank damping/teleportation factor; use d = 0.85 as a fairly typical value
#
# foreach page p in P
#   PR(p) = 1/N                          /* initial value */
#
# while PageRank has not converged do
#   sinkPR = 0
#   foreach page p in S                  /* calculate total sink PR */
#     sinkPR += PR(p)
#   foreach page p in P
#     newPR(p) = (1-d)/N                 /* teleportation */
#     newPR(p) += d*sinkPR/N             /* spread remaining sink PR evenly */
#     foreach page q in M(p)             /* pages pointing to p */
#       newPR(p) += d*PR(q)/L(q)         /* add share of PageRank from in-links */
#   foreach page p
#     PR(p) = newPR(p)
#
# return PR

def store_In_Links(str):
    str_list = str.split()
    str_list.pop(0)
    return (list(set(str_list)))

# fileOfLinks = open('H:\IR\In-Links-Sample.txt','r')
#fileOfLinks = open('H:\IR\In-Links.txt','r')
fileOfLinks = open(raw_input("Please enter the file name or the path along with the file name:\n"),'r')
P  =  set(fileOfLinks.readlines())
fileOfLinks.close()


list_Mp = []
# List_Lq = []
List_S = []
List_P = []

list_sinkPR = []
count = 0
# Puts all the values of the file into List_P with their initial values
# and the remaining values in List_Mp
for i in P:
    count = count + 1
    list_Mp.append(store_In_Links(i))
    List_P.append((i.split(' ')[0]).rstrip('\n'))

count_for_dict = 0
# dict_P represents Mp in the algorithm
dict_P = {}
# Puts all the values of the file into dict_P dictionary
# for i in List_P:
#     dict_P[i] = list_Mp[count_for_dict]
#     count_for_dict = count_for_dict + 1


# Finds the total no. of pages
N = P.__len__()


# PRp = []
# Probability of pages-> the final value which needs to be returned
dict_PRp = {}

# Puts all the values of the file into dict_P dictionary
for i in P:
    #
    i = i.split()
    dict_P[i[0]] = i[1:]

# Temporary Probability of pages which will be put into dict_Prp
dict_newPRp = {}

# Dictionary for representing L(q) in the algorithm
dict_Lq = {}

# Initializes all the pages with a default probability of 1/N
# Initializes the outlinks value (Lq) with zero
for i in List_P:
    dict_PRp[i] = 1.0/N
    dict_Lq[i] = 0

print "1/N",1/N
# Puts the actual value for (Lq)
for i in dict_P.values():
    for j in i:
        dict_Lq[j] += 1

# Finds the List of Sink Nodes (S)
for i in dict_Lq:
    if dict_Lq[i] == 0:
        List_S.append(i)

# The below code checks the total probability from all the pages, which should be equal to one
sum = 0
for i in dict_PRp:
    sum = sum + dict_PRp[i]

# Probability should come as one
print "sum of probabilities", sum

# PageRank damping/Teleportation factor, defined as 0.85
d = 0.85
d_complement = 1 - d
entropy = 0.0
perplexity = 0.0

# Contains the list of perplexity values for each convergence loop
List_Perplexity = []

# the boolean value for continuing the convergenec loop
is_converged = False

# Counts the convergence loop
count_converged = 0

# Calculated Original Page Rank for calculating proportion of pages whose page rank is less than their initial
dict_PRp_Original = dict_PRp

# PageRank Algorithm   Starts
while(not(is_converged)):
    # Calculation for perplexity to check if page rank has converged    Starts
    print "entropy ",entropy
    perplexity = 2 ** (entropy)
    print "perplexity",perplexity
    List_Perplexity.append(perplexity)
    if(List_Perplexity.__len__()>=4):
        if (abs((List_Perplexity[-1]) - (List_Perplexity[-2])) <1 and
           abs((List_Perplexity[-2]) -(List_Perplexity[-3])) <1 and
           abs((List_Perplexity[-3]) - (List_Perplexity[-4]))<1 ):
                is_converged = True
    # Calculation for perplexity to check if page rank has converged    Ends

    count_converged += 1
    print "Convergence no.", count_converged

    sinkPR = 0
    for i in List_S:
        sinkPR = sinkPR + dict_PRp[i]

    for i in List_P:
        dict_newPRp[i] = d_complement/N
        dict_newPRp[i] +=  d * (sinkPR / N)
        count_q = 0

        for j in dict_P[i]:
            dict_newPRp[i] += d * dict_PRp[j] / dict_Lq[j]

    for i in dict_PRp:
        dict_PRp[i] = dict_newPRp[i]

    # Calcualting Entropy   Starts
    entropy = 0
    for i in dict_PRp:
        entropy += dict_PRp[i]*log(1/dict_PRp[i],2)
    # Calcualting Entropy   Ends

# PageRank Algorithm   Ends

# Sorts the PageRank
sorted_PRp = sorted(dict_PRp.items(), key=operator.itemgetter(1), reverse = True)

dict_count_P = {}
for i in List_P:
    count_inlinks = 0
    for j in dict_P[i]:
        count_inlinks += 1
    dict_count_P[i] = count_inlinks

sorted_dict_count_P = sorted(dict_count_P.items(), key=operator.itemgetter(1), reverse = True)

# Calculates the sum of the probability after PageRanking algorithm, should be one
sum = 0
for i in dict_PRp:
    sum = sum + dict_PRp[i]
print sum

# Writes a file with top 50 pages
fileWithSortedPageRanking = open('PageRanking.txt','w')

# # Commented out the part which prints only till 50 pages
# count = 0
for i in sorted_PRp:
    fileWithSortedPageRanking.write(str(i)+"\n")
    # count = count + 1
    # if count > 50:
    #     break
fileWithSortedPageRanking.close()
print "The file with sorted page ranking has been created"
# Writes a file with top 50 inlinks
fileWithRankingOfInlinks = open('PageRanking_Inlinks.txt','w')

# # Commented out the part which prints only till 50 pages
# count = 0
for i in sorted_dict_count_P:
    fileWithRankingOfInlinks.write(str(i)+"\n")
    # count = count + 1
    # if count > 50:
        # break
fileWithRankingOfInlinks.close()
print "The file with sorted order of highest number of in-links has been created"

## The below code calculates the remaining questions asked in the assignment
List_No_Inlinks = []

print "pages with no out-links",List_S.__len__()
print "Total No. of pages",List_P.__len__()
print "proportion of pages with no out-links", List_S.__len__()/List_P.__len__()
# dict_PRp_less_ranking = {}
List_PRp_less_ranking = []
for i in List_P:
    if float(dict_PRp[i]) < 1/N:
        List_PRp_less_ranking.append(i)

print "dict_PRp_less_ranking", List_PRp_less_ranking.__len__()
print "Proportion of less ranking", List_PRp_less_ranking.__len__()/List_P.__len__()

List_zero_in_links = []

for i in List_P:
    if len(dict_P[i]) == 0:
        List_zero_in_links.append(i)

print "List_zero_in_links ",List_zero_in_links.__len__()
print "Proportion of zero links to total pages",List_zero_in_links.__len__()/List_P.__len__()
count = 1
for i in List_Perplexity:
    print "Convergence No.",count," Perplexity value ",i,"\n"
    count += 1
