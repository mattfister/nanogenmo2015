import sys
from wordtools import conceptnet_searcher
import random
from wordtools import aOrAn

all_relations = ('RelatedTo', 'IsA', 'PartOf', 'MemberOf', 'HasA', 'UsedFor', 'CapableOf', 'AtLocation', 'Causes', 'HasSubevent', 'HasFirstSubevent', 'HasLastSubevent', 'HasPrerequisite', 'HasProperty', 'MotivatedByGoal', 'ObstructedBy', 'Desires', 'CreatedBy', 'Synonym', 'Antonym', 'DerivedFrom', 'TranslationOf', 'DefinedAs')

relations = ('RelatedTo', 'IsA', 'PartOf', 'HasA', 'UsedFor', 'CapableOf')
#relations = ('IsA', 'PartOf', 'HasA', 'UsedFor')


def related_to_sentence(concept, subject, person=None):
    relation = random.choice((' was ', ' was related to ', ' was kind of like ', ' was similar to '))
    if person == None:
        sentence = "The " + concept + relation + aOrAn.aOrAn(subject) + " " + subject + "."
    else:
        sentence = person + ' thought about how a ' + concept + relation + aOrAn.aOrAn(subject) + " " + subject + '.'
    return sentence

def is_a_sentence(concept, subject, person=None):
    if person == None:
        sentence = "The " + concept + " was " + aOrAn.aOrAn(subject) + " " + subject + "."
    else:
        relation_verb = random.choice(('is', 'can be'))
        sentence =  person + ' considered how a ' + concept + ' ' + relation_verb + ' '  + aOrAn.aOrAn(subject) + " " + subject + '.'
    return sentence

def part_of_sentence(concept, subject, person=None):
    if person == None:
        sentence = "The " + concept + " was part of " + aOrAn.aOrAn(subject) + " " + subject + "."
    else:
        sentence =  person + ' noticed the ' + concept + ' was part of ' +  aOrAn.aOrAn(subject) + ' ' + subject + '.'
    return sentence 

def has_a_sentence(concept, subject, person=None):
    if person == None:
        sentence = "The " + concept + " had " + aOrAn.aOrAn(subject) + " " + subject + "."
    else:
        sentence = person + ' noticed the ' + concept + ' had ' + aOrAn.aOrAn(subject) + ' ' + subject + '.'
    return sentence

def used_for_sentence(concept, subject, person=None):
    if person == None:
        sentence = "The " + concept + " was used for " + aOrAn.aOrAn(subject) + " " + subject + "."
    else:
        sentence = person + ' considered using the ' + concept + " to " + subject + "."
    return sentence

def capable_of_sentence(concept, subject, person=None):
    if person == None:
        sentence = "The " + concept + " could " + subject + "."
    else:
        sentence = person + ' could tell the ' + concept + ' could ' + subject + "."
    return sentence


def generate_concept_sentence(person, concept, relation):
    pass

def prep_part(part):
    return part.replace('_', ' ').replace('build', 'building')

def generate_concept_sentence(person, concept):
    concept_relations = conceptnet_searcher.get_concept_relations(concept)
    relation = ""
    while not relation in relations:
        concept_relation = random.choice(concept_relations)
        relation = concept_relation[0]
        subject = concept_relation[1]
    #print (concept, relation, subject)
    concept_part = prep_part(concept)
    subject_part = prep_part(subject)
    if relation == 'RelatedTo':
        sentence = related_to_sentence(concept_part, subject_part, person)
    elif relation == 'IsA':
        sentence = is_a_sentence(concept_part, subject_part, person)
    elif relation == 'PartOf':
        sentence = part_of_sentence(concept_part, subject_part, person)
    elif relation == 'HasA':
        sentence = has_a_sentence(concept_part, subject_part, person)
    elif relation == 'UsedFor':
        sentence = used_for_sentence(concept_part, subject_part, person)
    elif relation == 'CapableOf':
        sentence = capable_of_sentence(concept_part, subject_part, person)
    return sentence

if __name__ == '__main__':
    generate_concept_sentence(random.choice((sys.argv[1], None)), sys.argv[2])

