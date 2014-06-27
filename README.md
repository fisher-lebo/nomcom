nomcom
======

combinations of names of notable individuals, such as:

* Elton John Oliver Reed
  * [Elton John](http://en.wikipedia.org/Elton_John)
  * [John Oliver](http://en.wikipedia.org/John_Oliver)
  * [Oliver Reed](http://en.wikipedia.org/Oliver_Reed)

On Reddit there is a user with the username [AlGoreVidalSassoon](http://reddit.com/u/AlGoreVidalSassoon). This is the combination of Al Gore + Gore Vidal + Vidal Sassoon, which struck me as terribly clever so I wanted to have some way to automate the combining of names in this way.

After some Googling, I struggled to find anything relevant, which suprised me somewhat as I think this is a fun puzzle. I had some idea of the approach I needed to do it myself, but then struggled to find a database of historical names anywhere. Wikipedia to the rescue. One of Wikipedia's many lists of lists include notable individuals grouped by [nationality](http://en.wikipedia.org/wiki/Lists_of_people_by_nationality). The first part of the script simply scapes a number of these individual pages. The current database generated from this includes people from Britons as well as Americans from each individual state. 

The next part attempts to match the names. Each name is converted to first name + last name, so Ralph Waldo Emerson becomes Ralph Emerson. This does not keep perfectly with the historical record, but it makes sure that in each combination of three names, each section is the name of an individual. For example, if Woodrow T Wilson was used, one of the combinations could be Woodrow T Wilson Chandler Bing. Woodrow T and T Wilson aren't the names of individuals we are aiming for. Breaking each name down to first name + last name keeps a nice symmetry.

The matching algorithim is naive but works. Currently it combines 3 names, but these match could be as small or large as desired.
