#L'objet actif prend les caractéristiques de l'objet séléctionné avant 
#donc l'objet actif prend la place de l'ancien ( en gros )

#UTILISATION :
#sélectionner l'objet modèle , puis le nouvelle objet voulant prendre sa place 

import bpy

def changement():
#liste sauvgardant les objets selectionnés ( ca sera tjs 2)
	liste = []
#ajoute dans la liste les objets dans l'ordre de leur selection
	for objet in bpy.context.selected_objects :
		bpy.context.scene.objects.active = objet
		liste.append(bpy.context.active_object)
#les modifications peuvent etre faites par boucle mais comme on manipule tjs 2 objets pas trés grave
#modification scaling
	liste[0].scale.x = liste[1].scale.x
	liste[0].scale.y = liste[1].scale.y
	liste[0].scale.z = liste[1].scale.z
#modification location
	liste[0].location.x = liste[1].location.x
	liste[0].location.y = liste[1].location.y
	liste[0].location.z = liste[1].location.z
#modification rotation
	liste[0].rotation_euler.x = liste[1].rotation_euler.x
	liste[0].rotation_euler.y = liste[1].rotation_euler.y
	liste[0].rotation_euler.z = liste[1].rotation_euler.z
#desactivation bon objet ( au cas ou )
	liste[0].select = False
#activation objet modèle
	liste[1].select = True
#supression objet
	bpy.ops.object.delete(use_global=False)