# Five Clique
A solution to the problem of finding five English words with 25 distinct characters.

# Description
This solution is inspired by the wonderful A problem squared podcast by Hill and Parker. In episode 38, Hill and Parker are searching for five English words with distinct letters. Parker's proposed solution builds pairs of distinct words and then tries to merge these pairs to groups of five (henceforth named 'The Parker algorithm'). According to Parker, executing the Parker algorithm on a laptop took about a month. This appeared to the author as optimizable.

# Solution
The solution proposed here represents the problem as intersections of complementary sets. In particular, we find all the complementary sets to each letter. And then loop choosing words from such complementary sets doing the intersection of 5, 10, 15, 20 letters (and breaking and going back when faced against empty sets) until we get a final non-empty set in the complementary of the already 20 letters picked. In average, we finish from 10seconds to 2minutes (depending on the set order the execution follows), rather than a month or 30 minutes, as in the Parker or Benjamin algorithm!
