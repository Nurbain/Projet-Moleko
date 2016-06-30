#L'objet actif prend les caractéristiques de l'objet séléctionné avant 
#donc l'objet actif prend la place de l'ancien ( en gros )

#UTILISATION :
#sélectionner les hydrogènes a changer, lancer la commande "changementhydro()" dans la console python

#ne pas oublier de run toute les fonctions

import bpy

#création de la couleur d'hydrogène
def couleurhydro() :
	mat = bpy.data.materials.new('blanc')
	mat.diffuse_color = (1,1,1)
	mat.diffuse_shader = 'LAMBERT' 
	mat.diffuse_intensity = 1.0
	mat.specular_color = (1,1,1)
	mat.specular_shader = 'COOKTORR'
	mat.specular_intensity = 0.032
	mat.ambient = 1
	return mat

#sous-fonction pour set la couleur 
def setcouleur(obj,mat):
	ob = obj.data
	ob.materials.append(mat)


def changementhydro():
	mat=couleurhydro()
#sert de conteur pour créer nbr objet
	nbr = 0
#liste modele
	listem = []
#ajoute dans la liste les objets modele
	for objet in bpy.context.selected_objects :
		nbr=nbr+1
		bpy.context.scene.objects.active = objet
		listem.append(bpy.context.active_object)
#création des nbr objets
	for k in range(0,nbr):
		bpy.ops.mesh.primitive_uv_sphere_add()
		obj=bpy.context.active_object
#valeur absolue du scaling
		x=abs(listem[k].scale.x)
		y=abs(listem[k].scale.y)
		z=abs(listem[k].scale.z)
#modification scaling
		obj.scale = [x,y,z]
#modification location
		obj.location = [listem[k].location.x,listem[k].location.y,listem[k].location.z]
#modification rotation
		obj.rotation_euler = [listem[k].rotation_euler.x,listem[k].rotation_euler.y,listem[k].rotation_euler.z]
#smooth de l'objet
		bpy.ops.object.shade_smooth()
#couleur de l'objet
		setcouleur(bpy.context.object,mat)
		obj.select = False
#supression des modèles 
	for n in range(0,nbr):
		listem[n].select = True
		bpy.ops.object.delete(use_global=False)