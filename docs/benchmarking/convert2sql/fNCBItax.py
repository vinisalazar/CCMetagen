#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
UPDATE v1.4.3 - This script has been deprecated. See ccmetagen/fNCBItax.py for the latest version.

Function that takes a taxid as input and returns a class containing the taxonomic info and taxids 
for multiple taxonomic ranks. 

Required to parse the results of KMA and store them in the SQLite3 'bench.db'

@ V.R.Marcelino
Created on 12 Jul 2018

"""

from ete3 import NCBITaxa
ncbi = NCBITaxa()
import cTaxInfo # where we define classes used here


def lineage_extractor(query_taxid, TaxInfo_object):
    list_of_taxa_ranks = ['superkingdom', 'kingdom', 'phylum', 'class', 'order', 'family','genus', 'species']
    lineage = ncbi.get_lineage(query_taxid)
    ranks = ncbi.get_rank(lineage)
    names = ncbi.get_taxid_translator(lineage)

    for key, val in ranks.items():
        
        if val == list_of_taxa_ranks[0]:
            TaxInfo_object.Superkingdom = names[key]
            TaxInfo_object.Superkingdom_TaxId = key            
             
        elif val == list_of_taxa_ranks[1]:
            TaxInfo_object.Kingdom = names[key]
            TaxInfo_object.Kingdom_TaxId = key
            
        elif val == list_of_taxa_ranks[2]:
            TaxInfo_object.Phylum = names[key]
            TaxInfo_object.Phylum_TaxId = key
            
        elif val == list_of_taxa_ranks[3]:
            TaxInfo_object.Class = names[key]
            TaxInfo_object.Class_TaxId = key
            
        elif val == list_of_taxa_ranks[4]:
            TaxInfo_object.Order = names[key]
            TaxInfo_object.Order_TaxId = key
        
        elif val == list_of_taxa_ranks[5]:
            TaxInfo_object.Family = names[key]
            TaxInfo_object.Family_TaxId = key
            
        elif val == list_of_taxa_ranks[6]:
            TaxInfo_object.Genus = names[key]
            TaxInfo_object.Genus_TaxId = key
            
        elif val == list_of_taxa_ranks[7]:
            TaxInfo_object.Species = names[key]
            TaxInfo_object.Species_TaxId = key
    return TaxInfo_object


