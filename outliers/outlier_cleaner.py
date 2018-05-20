#!/usr/bin/python
import numpy

def outlierCleaner(predictions, ages, net_worths):
    """
        Clean away the 10% of points that have the largest
        residual errors (difference between the prediction
        and the actual net worth).

        Return a list of tuples named cleaned_data where 
        each tuple is of the form (age, net_worth, error).
    """
    residual_errors = [prediction - net_worth for prediction,net_worth in zip(predictions, net_worths)]
    # get a list of tuples, each formed from each element of the 3 arrays; works somehow even though ages is a 2D array (but with second dimension equal to 1)
    cleaned_data = zip(ages, net_worths, residual_errors)
    # sort cleaned_data by the 3rd element in the tuple, i.e. residual_errors
    cleaned_data.sort(key=lambda tup: tup[2])
    num_elements = len(cleaned_data) - int(0.1 * len(cleaned_data))
    # get the first "num_elements" elements from the sorted cleaned_data
    cleaned_data = cleaned_data[:num_elements]

    ### your code goes here
    print(num_elements, len(ages))

    return cleaned_data

ages = [1, 2]
predictions = [100, 200]
net_worths = [101, 201]
ages = numpy.reshape(ages, (2, 1))
predictions = numpy.reshape(predictions, (2, 1))
net_worths = numpy.reshape(net_worths, (2, 1))

outlierCleaner(predictions, ages, net_worths)


