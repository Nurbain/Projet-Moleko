def changementvalence():
#sélectionne tout
	bpy.ops.object.select_grouped(type='TYPE')
#liste modele
	listev = []
#ajoute dans la liste les objets modele
	for objet in bpy.context.selected_objects :
		bpy.context.scene.objects.active = objet
#on vérifie si le nom de l'objet contient Hydro , pour vérifier que c'est un hydrogène 
		if 'Valence' in objet.name:
			bpy.context.scene.objects.active = objet
			listev.append(bpy.context.active_object)
		if 'Model' in objet.name:
			bpy.context.scene.objects.active = objet
			model = bpy.context.active_object
#création des nbr objets
	bpy.ops.object.select_all(action='DESELECT')
	bpy.context.scene.objects.active = model
	model.select=True
	for k in range(0,len(listev)):
		bpy.ops.object.duplicate_move()
		obj=bpy.context.active_object
#valeur absolue du scaling
		x=listev[k].scale.x
		y=listev[k].scale.y
		z=listev[k].scale.z
#modification scaling
		obj.scale = [x,z,y]
#scaling()
#modification location
		obj.location = [listev[k].location.x,listev[k].location.y,listev[k].location.z]
#modification rotation, le 1.5708 rad correspond a 90° 
		obj.rotation_euler = [listev[k].rotation_euler.x+1.5708,listev[k].rotation_euler.y,listev[k].rotation_euler.z]
#smooth de l'objet
		bpy.ops.object.shade_smooth()
#couleur de l'objet
#supression des modèles 
	bpy.ops.object.select_all(action='DESELECT')
	for n in range(0,len(listev)):
		listev[n].select = True
		bpy.ops.object.delete(use_global=False)
		
		
def scaling() :
	if bpy.context.active_object.scale.y < 0 :
		bpy.ops.object.transform_apply(location=False , rotation=False , scale=True)
		obj=bpy.context.active_object
		bpy.ops.object.mode_set(mode='EDIT')
		bpy.ops.mesh.select_all(action = 'SELECT')
		bpy.ops.mesh.normals_make_consistent(inside=False)
		bpy.ops.object.mode_set(mode='OBJECT')		