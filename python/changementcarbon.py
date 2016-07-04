import bpy,bmesh

#Résoud les problèmes de scaling inverse

def scaling() :
	if bpy.context.active_object.scale.y < 0 :
		bpy.ops.object.transform_apply(location=False , rotation=False , scale=True)
		obj=bpy.context.active_object
		bpy.ops.object.mode_set(mode='EDIT')
		bpy.ops.mesh.select_all(action = 'SELECT')
		bpy.ops.mesh.normals_make_consistent(inside=False)
		bpy.ops.object.mode_set(mode='OBJECT')

		
def couleurcarb() :
	mat = bpy.data.materials.new('noir')
	mat.diffuse_color = (0,0,0)
	mat.diffuse_shader = 'LAMBERT' 
	mat.diffuse_intensity = 1.0
	mat.specular_color = (1,1,1)
	mat.specular_shader = 'COOKTORR'
	mat.specular_intensity = 0.032
	mat.ambient = 1
	return mat
	

def setcouleur(obj,mat):
	ob = obj.data
	ob.materials.append(mat)

	
def changementcarbon() :
#sélectionne tout
	bpy.ops.object.select_grouped(type='TYPE')
	mat=couleurcarb()
#sert de conteur pour créer nbr objet
	nbr = 0
#liste modele
	listem = []
#ajoute dans la liste les objets modele
	for objet in bpy.context.selected_objects :
		bpy.context.scene.objects.active = objet
#on vérifie si le nom de l'objet contient Hydro , pour vérifier que c'est un hydrogène 
		if 'Carb' in objet.name:
			nbr=nbr+1
			bpy.context.scene.objects.active = objet
			listem.append(bpy.context.active_object)
#création des nbr objets
	for k in range(0,nbr):
		bpy.ops.mesh.primitive_uv_sphere_add()
		obj=bpy.context.active_object
#valeur absolue du scaling
		x=listem[k].scale.x
		y=listem[k].scale.y
		z=listem[k].scale.z
#modification scaling
		obj.scale = [x,y,z]
		scaling()
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
	
	
		
	
			
			
	
	
	