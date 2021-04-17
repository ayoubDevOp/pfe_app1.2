# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = True` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models

class Niveau(models.Model):
    desig_nv = models.CharField(db_column='DESIG_NV', max_length=32, blank=True, null=True)  
    desc_nv = models.CharField(db_column='DESC_NV', max_length=255, blank=True, null=True)  

    class Meta:
        managed = True
        db_table = 'NIVEAU'
    
    def __str__(self):
        return self.desc_nv

class Groupe(models.Model): 
    niveau = models.ForeignKey(Niveau,  on_delete=models.CASCADE)  
    desig_grp = models.CharField(db_column='DESIG_GRP', max_length=32, blank=True, null=True)  
    desc_grp = models.CharField(db_column='DESC_GRP', max_length=255, blank=True, null=True)  

    class Meta:
        managed = True
        db_table = 'GROUPE'
    
    def __str__(self):
        return self.desig_grp

class Eleve(models.Model): 
    nom_elv = models.CharField(db_column='NOM_ELV', max_length=255, blank=True, null=True)  
    pwd_elv = models.CharField(db_column='PWD_ELV', max_length=255, blank=True, null=True)   
    date_nai_elv = models.DateField(db_column='DATE_NAI_ELV', blank=True, null=True)  
    groupe = models.ForeignKey(Groupe, on_delete=models.CASCADE)  

    class Meta:
        managed = True
        db_table = 'ELEVE'
        
    def __str__(self):
        return self.nom_elv

class Enseignant(models.Model):
    nom_ens = models.CharField(db_column='NOM_ENS', max_length=255, blank=True, null=True)  
    pwd_ens = models.CharField(db_column='PWD_ENS', max_length=255, blank=True, null=True)  
    date_nai_ens = models.DateField(db_column='DATE_NAI_ENS', blank=True, null=True)  

    class Meta:
        managed = True
        db_table = 'ENSEIGNANT'

    def __str__(self):
        return self.nom_ens

class Message(models.Model):
    subject = models.CharField(db_column='SUBJECT', max_length=255, blank=True, null=True)   
    content = models.TextField(db_column='CONTENT', blank=True, null=True)  
    type = models.IntegerField(db_column='TYPE', blank=True, null=True)# 0 ens -> elv; 1 : elv -> ens
    at_time = models.DateTimeField(db_column='AT_TIME', blank=True, null=True)
    eleve = models.ForeignKey(Eleve, on_delete=models.CASCADE) 
    enseignant = models.ForeignKey(Enseignant, on_delete=models.CASCADE) 

    class Meta:
        managed = True
        db_table = 'MESSAGE'
    
    def __str__(self):
        return self.subject

class Repertoire(models.Model):
    desig_rep = models.CharField(db_column='DESIG_REP', max_length=255, blank=True, null=True)  
    type = models.IntegerField(db_column='TYPE', blank=True, null=True)  
    lien = models.CharField(db_column='LIEN', max_length=255, blank=True, null=True)  
    enseignant = models.ForeignKey(Enseignant, on_delete=models.CASCADE) 
    
    class Meta:
        managed = True
        db_table = 'REPERTOIRE'

    def __str__(self):
        return self.desig_rep

class Exercice(models.Model): 
    desig_ex = models.CharField(db_column='DESIG',max_length=255, blank=True, null=True) 
    descr_ex = models.TextField(db_column='DESCR', blank=True, null=True)  
    lien = models.CharField(db_column='LIEN', max_length=255, blank=True, null=True)  
    repertoire = models.ForeignKey(Repertoire, on_delete=models.CASCADE)
    
    class Meta:
        managed = True
        db_table = 'EXERCICE'
    
    def __str__(self):
        return self.desig_ex


class Instance(models.Model):
    desig_ins = models.CharField(db_column='DESIG', max_length=255, blank=True, null=True) 
    descr_ins = models.TextField(db_column='DESCR', blank=True, null=True)   
    lien = models.CharField(db_column='LIEN', max_length=255, blank=True, null=True)
    outputgeneration = models.TextField(db_column='outputGeneration', blank=True, null=True)   
    repertoire = models.ForeignKey(Repertoire, on_delete=models.CASCADE)
    exercice = models.ForeignKey(Exercice, on_delete=models.CASCADE)    

    class Meta:
        managed = True
        db_table = 'INSTANCE'

    def __str__(self):
        return self.descr_ins

class Virtualmachine(models.Model):
    desig_vm = models.CharField(db_column='DESIG_VM', max_length=255, blank=True, null=True)  
    desc_vm = models.CharField(db_column='DESC_VM', max_length=255, blank=True, null=True) 
    lien = models.CharField(db_column='LIEN', max_length=255, blank=True, null=True)   
    repertoire = models.ForeignKey(Repertoire, on_delete=models.CASCADE)
    instance = models.ForeignKey(Instance, on_delete=models.CASCADE)  

    class Meta:
        managed = True
        db_table = 'VIRTUALMACHINE'

    def __str__(self):
        return self.descr_vm


class Imagedocker(models.Model):
    desig_doc = models.CharField(db_column='DESIG_Doc', max_length=255, blank=True, null=True)  
    desc_doc = models.CharField(db_column='DESC_Doc', max_length=255, blank=True, null=True) 
    repertoire = models.ForeignKey(Repertoire, on_delete=models.CASCADE)  
    instance = models.ForeignKey(Instance, on_delete=models.CASCADE) 

    class Meta:
        managed = True
        db_table = 'IMAGEDOCKER'
    
    def __str__(self):
        return self.desig_doc

class Score(models.Model):
    eleve = models.ForeignKey(Eleve, on_delete=models.CASCADE) 
    exercice = models.ForeignKey(Exercice, on_delete=models.CASCADE)  
    value = models.IntegerField(db_column='VALUE')  
    at_time = models.DateTimeField(db_column='AT_TIME', blank=True, null=True)  

    class Meta:
        managed = True
        db_table = 'SCORE'