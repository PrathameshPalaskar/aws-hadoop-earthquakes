
Html
index.html

For accepting the input

Python.

Mapper.py : This is the code for the mapper to get the input file into the date and magnitude format into ranges through 0 to 10
Preducer.py : This is the output of the function which counts the number of earthquakes through the different ranges.
Pweek_mapper.py : Week wise mapper performing same function as above
Pweek_reducer.py : Week wise reducer performing same function as preducer.py

You will need to use Hadoop on a cloud service provider 
2. Interesting data sets have at least 100 thousand tuples up to a few million tuples.
At these web-sites there are schema/meta-data describing the data.
3. Using earthquakes as an example, we would like to know: are magnitude 1 or 2
(or others) increasing, week-by-week? Day-by-day? Is there a relationship between
magnitude and depth? Location and magnitude? Week-by-week?
We want to take large amounts of data and categorize into groups (ranges),
for example magnitude groups (1-2, 2-3, 3-4,…) or latitude groups (20-25, 25-30, …)
using Hadoop.
4. Try with different numbers of mappers and reducers. (1 mapper, 1 reducer (1,1),
then: (2,1), (2,2), (10,1), (10,2)
Run with 1, 2, and 3 instances.
5. “Instrument” (time) running.
