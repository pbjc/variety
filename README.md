Variety: Sorting Reddit Posts for Content Diversity
===================================================

Variety takes a user’s subscribed subreddits and re-ranks threads in order to
place threads with diverse content at the top. Threads that receive high scores
according to Variety’s ranking algorithms are those that have multifaceted
discussion (e.g.: individual posts on a thread show a diversity of political
opinion) and where interlocutors are reasonable, as determined by sentiment
analysis. It is our hope that by using Variety, users will be able to consider
all sides of an issue before creating an informed opinion rather than blindly
parroting echo chamber opinions.

Status
------
Currently, we only compute and output scores for individual thread features. In
the feature, we will combine these features in an intelligent way to produce a
single score. A machine learning approach to this will require datasets labeled
for content diversity. If you've got one on hand, please share it with us ;).

Usage
-----
```bash
# pip3 install -r requirements.text
$ python3 main.py <Reddit submission url>
```

Features
--------
Polarity: how negative or positive comments are. Range: [-1, 1].
Subjectivity: how objective or subjective comments are. Range: [0, 1].
Link count: how many links comments contain.
CommentLength: how many words comments contain.

To compute scores for an entire comment thread, each comment is scored in
isolation and weighted by its relative number of upvotes.
