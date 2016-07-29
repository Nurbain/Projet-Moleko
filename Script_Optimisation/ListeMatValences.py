#Nathan URBAIN
#Script listant et sauvgardant les valences d'une molécule pour changement de modèle dans l'optimisation general

#Utilisation : Selection d'un mesh , puis lancement de script dans la console python

import bpy

def matvalence():
#Séléction de tout les Meshs
	bpy.ops.object.select_grouped(type='TYPE')
#Couleurs des valences (présent dans le script d'optimisation)
	carb = couleurcarb()
	azote = couleurazote()
	oxy = couleuroxy()
	chlore = couleurchlore()
	fluor = couleurfluor()
	soufre = couleursoufre()
#Liste pour la sauvgarde des valences, associé aux atomes correspondant 
	listec = [carb]
	listea = [azote]
	listeo = [oxy]
	listechl = [chlore]
	listef = [fluor]
	listes = [soufre]
#Liste Générale 
	liste = []
#Parcours des atomes, et sauvgarde des valences dans la bonne liste
	for objet in bpy.context.selected_objects :
			bpy.context.scene.objects.active = objet
			if 'Carb' in objet.name:
				bpy.context.scene.objects.active = objet
				listec.append(bpy.context.active_object.children)
			if 'Azo' in objet.name :
				bpy.context.scene.objects.active = objet
				listea.append(bpy.context.active_object.children)
			if 'Oxy' in objet.name :
				bpy.context.scene.objects.active = objet
				listeo.append(bpy.context.active_object.children)
			if 'Chlo' in objet.name :
				bpy.context.scene.objects.active = objet
				listechl.append(bpy.context.active_object.children)
			if 'Flu' in objet.name :
				bpy.context.scene.objects.active = objet
				listef.append(bpy.context.active_object.children)
			if 'Souf' in objet.name :
				bpy.context.scene.objects.active = objet
				listes.append(bpy.context.active_object.children)
	liste.append(listec)
	liste.append(listea)
	liste.append(listeo)
	liste.append(listechl)
	liste.append(listef)
	liste.append(listes)
#Liste générale des valences 
	return liste