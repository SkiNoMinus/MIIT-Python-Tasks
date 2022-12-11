with open(r"C:\Users\79683\Desktop\ev\variant12_m.txt", 'r') as file:
    events = [file.readline().split() for i in range(15)]

first_event, second_event = [], []

# Events
 
for event_chance in events:
    first_event.append(int(event_chance[0]))
    second_event.append(int(event_chance[1]))

# Ranking

def ranking(array):
    ranked = list()
    values = []

    for i in array:
        rank = 1
        for j in array:
            if i > j:
                rank += 1
        rank += values.count(i) # Работает в случае повторения 

        ranked.append(rank)
        values.append(i)

    return ranked
        
first_event_ranks = ranking(first_event)
second_event_ranks = ranking(second_event)

#  Main part

def find_correlation(ranks1, ranks2, operation):
    values_count = len(first_event)
    sum_di = sum((ranks1[i] - ranks2[i])**2 for i in range(values_count))

    events_correlation = 1 - ((6 * sum_di) / (values_count * (values_count ** 2 - 1)))
    if operation == 'correlation':
        return  events_correlation
    elif operation == 'correlation_num':
        return events_correlation
    else:
        return 'Choose another operation'

correlation = find_correlation(first_event_ranks, second_event_ranks, 'correlation')
correlation_num = find_correlation(first_event_ranks, second_event_ranks, 'correlation_num')

def interpretation(correlation):
    value = abs(correlation)

    if 1 >= value > 0.7:
        return 'Strong correlation'
    elif 0.7 >= value > 0.5:
        return 'Sufficient strong correlation'
    elif 0.5 >= value > 0.2:
        return 'Medium correlation'
    elif 0.2 >= value > 0:
        return 'Weak correlation'
    elif value == 0:
        return 'No correlation'
    else:
        return "Data isn't correct"

print('Correlation: ', interpretation(correlation), '|', 'Correlation value: ', correlation_num)