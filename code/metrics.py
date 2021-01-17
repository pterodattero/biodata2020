import pandas as pd
import math


def metrics(true_positive, true_negative, false_positive, false_negative, show=True):
   
    #compute metrics reqested
    accuracy = (true_positive + true_negative) / (true_positive + true_negative + false_negative + false_positive)
    precision = true_positive / (true_positive + false_positive)
    sensitivity = true_positive / (true_positive + false_negative)
    specificity = true_negative / (true_negative + false_positive)
    f1 = 2 * (precision * sensitivity) / (precision + sensitivity)
    mcc = (true_positive*true_negative - false_positive*false_negative) / (math.sqrt(
        (true_positive + false_positive) * (true_positive + false_negative) * 
        (true_negative + false_positive) * (true_negative + false_negative)
    ))

    #function returns a dictionary with all the needed metrics
    return {
        "Accuracy" : accuracy,
        "Precision": precision,
        "Sensitivity": sensitivity,
        "Specificity": specificity,
        "F1-score": f1,
        "MCC": mcc
    }


def seq_metrics(model_hits, ground_truth, db_num):

    model_hits = set(model_hits.keys())
    ground_truth = set(ground_truth.keys())
    
    true_positive = len(model_hits.intersection(ground_truth))
    false_negative = len(ground_truth - model_hits)
    false_positive = len(model_hits - ground_truth)
    true_negative = db_num - true_positive - false_positive - false_negative

    return metrics(
        true_positive,
        true_negative,
        false_positive,
        false_negative
    )


def pos_metrics(model_hits, ground_truth):
    
    tp_list = []
    tn_list = []
    fp_list = []
    fn_list = []

    common_prots = set(model_hits.keys()).intersection(set(ground_truth.keys()))
    for prot in common_prots:
        position_set_h = create_position_set(model_hits[prot])
        position_set_g = create_position_set(ground_truth[prot])
        sequence_length = ground_truth[prot][0]['length']

        true_positive = len(position_set_h.intersection(position_set_g))
        false_negative = len(position_set_g - position_set_h)
        false_positive = len(position_set_h - position_set_g)
        true_negative = sequence_length - true_positive - false_positive - false_negative

        tp_list.append(true_positive)
        tn_list.append(true_negative)
        fp_list.append(false_positive)
        fn_list.append(false_negative)

    true_positive = sum(tp_list)
    true_negative = sum(tn_list)
    false_positive = sum(fp_list)
    false_negative = sum(fn_list)
        
    return metrics(
        true_positive,
        true_negative,
        false_positive,
        false_negative
    )   


def create_position_set(fragment_list):
    
    position_set = set()

    for fragment in fragment_list:
        fragment_set = set(range(fragment['start'], fragment['end'] + 1))
        position_set = position_set.union(fragment_set)

    return position_set
