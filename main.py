import os
from evaluation_pipeline import Pipeline
from unbalanced_dataset import SMOTE, UnderSampler, OverSampler, NearMiss

## SETTINGS ##
location = 'data/rivm/'
content_index = 9
label_index = 11
folds = os.listdir(location)
delimiter = '\t'
folds[:] = [location + i for i in folds]
verbose = True

## LOAD RAW DATA ##
raw_data = []
feat_content = []
labels = []
for fold_nr in range(0, len(folds)):
    file = open(folds[fold_nr], 'r')
    raw_data.append([])
    feat_content.append([])
    labels.append([])
    for line in file.readlines():
        raw_data[fold_nr].append(line.split(delimiter))
        feat_content[fold_nr] = [row[content_index] for row in raw_data[fold_nr]]
        labels[fold_nr] = [row[label_index] for row in raw_data[fold_nr]]
        labels[fold_nr] = [0 if label == 'f' else 1 for label in labels[fold_nr]]
    file.close()

## EVALUATE ##
resampler = SMOTE(verbose=verbose)
pip = Pipeline(feat_content, labels, resampler, verbose)
f1_complete = pip.validation()
