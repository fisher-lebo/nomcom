nomcom
======

**NOTICE: This repo has moved to [github.com/aaron-lebo/nomcom](https://github.com/aaron-lebo/nomcom).**

combinations of names of notable individuals, such as:

* Elton John Oliver Reed
  * [Elton John](http://en.wikipedia.org/wiki/Elton_John)
  * [John Oliver](http://en.wikipedia.org/wiki/John_Oliver)
  * [Oliver Reed](http://en.wikipedia.org/wiki/Oliver_Reed)

Please see [combos.txt](https://github.com/fisher-lebo/nomcom/blob/master/combos.txt) for full results.

On Reddit there is a user with the username [AlGoreVidalSassoon](http://reddit.com/u/AlGoreVidalSassoon). This is the combination of [Al Gore](http://en.wikipedia.org/wiki/Al_Gore) + [Gore Vidal](http://en.wikipedia.org/wiki/Gore_Vidal) + [Vidal Sassoon](http://en.wikipedia.org/wiki/Vidal_Sassoon), which struck me as terribly clever so I wanted to have some way to automate the combining of names in this way.

After some Googling, I struggled to find anything relevant, which suprised me somewhat as I think this is a fun puzzle. I had some idea of the approach I needed to do it myself, but then struggled to find a database of historical names anywhere. Wikipedia to the rescue. One of Wikipedia's many lists of lists include notable individuals grouped by [nationality](http://en.wikipedia.org/wiki/Lists_of_people_by_nationality). The first part of the script scrapes a number of these individual pages. The current database generated from this includes people from Britain as well as Americans from each individual state. These were chosen in particular to both limit the amount of data that needed to be pulled as well as to keep things relatively simple with Anglicized names.

The next part attempts to match the names. Each name is converted to first name + last name, so Ralph Waldo Emerson becomes Ralph Emerson. This does not keep perfectly with the historical record, but it makes sure that in each combination of three names, each section is the name of an individual. For example, if Woodrow T Wilson was used, one of the combinations could be Woodrow T Wilson Chandler Bing. Woodrow T and T Wilson aren't the names of individuals we are aiming for. Breaking each name down to first name + last name keeps a nice symmetry.

The matching algorithim is naive but works. Currently it combines 3 names, but these matches could be as small or large as desired. The initial input includes 28,364 names and the final result is 37,166 combinations.

Thanks to [Matthew Martin](http://github.com/phy1729) of the [Linux User's Group @ UT Dallas](http://lug.utdallas.edu) for algorithm help. 
