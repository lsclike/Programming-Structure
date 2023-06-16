# The difference between is and ==

# The is operator to compare object
# identical objects always equal but not vice versa
t1 = [1,2]
t2 = t1
t3 = [1,2]
identical_true_result = t1 is t2
identical_false_result = t1 is t3
equal_true = t1==t3
#
