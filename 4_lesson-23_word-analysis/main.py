from lib import *

def main():
    # read dataset
    dataset = read_json_file("reviews.json")
    print(dataset[0])

    # tokenize dataset
    dataset_tokenized = tokenize_dataset(dataset)
    print("Words of the first review: ")
    print(dataset_tokenized[0]['words'])
    print("Words of the second review: ")
    print(dataset_tokenized[1]['words'])
    print(type(dataset_tokenized))

    # compute word count
    dataset_word_count = compute_word_count_dataset(dataset_tokenized)
    print("Word count for first review: ")
    print(dataset_word_count[0]['word_count'])
    print("Word count for second review: ")
    print(dataset_word_count[1]['word_count'])

# run program
if __name__ == '__main__':
    main()