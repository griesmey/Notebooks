
def get_reviews():
    for review in open('test.txt'):
        review = review.replace('\n', '')
        yield review

if __name__ == '__main__':
    f = open('trainingset.json', 'w')
    classes = {}
    for train_pair in open('words.txt'):
        train_pair = train_pair.lower().replace('\n' , '').split()
        s[train_pair[0]] = train_pair[1]
    
    for review in get_reviews():
        for word in review.lower().split():
            if word in s:
                f.write('{0}\t{1}
            

