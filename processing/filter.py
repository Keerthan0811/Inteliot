def filter_dataset(dataset):

    return [item for item in dataset if len(item["output"]) >= 2]