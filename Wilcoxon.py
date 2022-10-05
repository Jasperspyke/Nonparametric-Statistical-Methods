import numpy as np
import scipy.stats as sp

pos_rank_sum = 0
neg_rank_sum = 0

# Parameters: Group 1 and Group 2 must be given in order!
group_1 = np.array([125,132,138,120,125,127,136,139,131,132,135,136,128,127,130])
group_2 = np.array([118,134,130,124,105,130,130,132,123,128,126,140,135,126,132])
two_tailed = False
alpha = 0.05


if group_2.size != group_1.size:
    raise ValueError

arr = np.empty(shape=(len(group_1), 6))

arr[:, 0] = group_1
arr[:, 1] = group_2
arr[:, 2] = group_2 - group_1
arr[:, 3] = np.abs(arr[:, 2])
arr[:, 4] = np.array(arr[:, 2] > 0)
arr[:, 5] = np.zeros(len(group_1))

rank = sp.rankdata(arr[:, 3])

arr[:, 5] = rank

for rank, sign in zip(arr[:, 5], arr[:, 4]):
    if sign:
        pos_rank_sum += rank
    else:
        neg_rank_sum += rank

print('positive sum is', pos_rank_sum)
print('negative rank sum is:', neg_rank_sum)

if pos_rank_sum < neg_rank_sum:
    w_score = pos_rank_sum
else:
    w_score = neg_rank_sum
print(arr)
print('w score is: ', w_score)

if len(group_1) <= 30:
    print('Small sample size detected. Table-based threshold initialized')
    if two_tailed:
        rej_column = 1
    else:
        rej_column = 3
    if alpha == 0.01:
        rej_column += 1
    rej = np.genfromtxt('/Users/JasperHilliard/Documents/Git testing Project/rejection_table.csv', delimiter=',')
    threshold = rej[len(group_1)-1, rej_column]
    print('The threshold is', threshold)
if threshold < w_score:
    print('the w_score is larger than threshold. We cannot reject the null')
elif threshold > w_score:
    print('the w_score is smaller than threshold. There is significant evidence to reject the null')
else:
    print('the w_score matches threshold')
